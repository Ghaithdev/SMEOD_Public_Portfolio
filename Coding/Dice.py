from random import randint
class Dice():
    def __init__(self, ndx):
        self.n_dice=int(ndx.split("d")[0].strip())
        self.size=int(ndx.split("d")[1].strip())
    
    def roll(self, mod=0):
        result=0
        for i in range(self.n_dice):
            result+=randint(1,self.size)
        result +=mod
        return result

class Check(Dice):
    def __init__(self,ndx="1d20", mod=0, dc=10, skill_crit=False,adv=0):
        super().__init__(ndx)
        self.adv=adv
        self.mod=mod
        self.can_crit=skill_crit 
        self.dc=dc
          
    def test(self):
        n=1
        if abs(self.adv)>0:
            n+=1
        lowest=None
        highest=None
        for i in range(n):
            result=self.roll()
            if not highest or result>highest:
                highest=result
            if not lowest or result<lowest:
                lowest=result
        if self.adv<0:
            result=lowest
        elif self.adv>0:
            result=highest
        if self.can_crit:
            if result==20:
                crit=1
            elif result==1:
                crit=-1
            else:
                crit=0
        else:
            crit=0
        self.raw_roll=result
        result+=self.mod
        return result, crit
    
    def get_result(self, creature="you"):
        self.result, self.crit = self.test()
        if self.can_crit:
            if self.crit>0:
                return "Crit"
            elif self.crit<0:
                return "Crit Fail"
        print(f"{creature} rolled a {self.raw_roll}, after modifiers that is a {self.result}")
        if self.result>=self.dc:
            outcome="pass"
            print(f"The DC was {self.dc} so {creature} {outcome}ed the roll")
            return True
        else:
            outcome="fail"
            print(f"The DC was {self.dc} so {creature} {outcome}ed the roll")
            return False

class Creature():
    creatures=[]

    def __init__(self, 
            name, 
            ac, 
            proficiency_bonus, 
            proficiencies=None, 
            hp_dice=None, 
            hp=None, 
            max_hp=None, 
            cr=1, 
            stats=None, 
            attacks=None, 
            resistances=None,
            condition_immunities=None,
            important=False,
            alive=1) -> None:
        self.name=name
        self.hp_dice=hp_dice
        self.hp=hp
        self.max_hp=max_hp
        self.proficiency_bonus=proficiency_bonus
        if proficiencies==None:
            proficiencies=[]
        self.proficiencies=proficiencies
        self.ac=ac
        self.cr=cr
        if stats==None:
            stats={
                'Str': 10,
                'Dex': 10,
                'Con': 10,
                'Int': 10,
                'Wis': 10,
                'Cha': 10
                }
        self.stats=stats
        self.str=self.get_stat_modifier('Str')
        self.dex=self.get_stat_modifier('Dex')
        self.con=self.get_stat_modifier('Con')
        self.int=self.get_stat_modifier('Int')
        self.wis=self.get_stat_modifier('Wis')
        self.cha=self.get_stat_modifier('Cha')
        self.str_score=stats['Str']
        self.dex_score=stats['Dex']
        self.con_score=stats['Con']
        self.int_score=stats['Int']
        self.wis_score=stats['Wis']
        self.cha_score=stats['Cha']
        if attacks==None:
            attacks={}
        self.attacks=attacks
        if resistances==None:
            resistances={}
        self.resistances=resistances
        self.important=important
        self.stable=True
        self.prone=False
        self.conscious=True
        self.conditions=[]
        if not condition_immunities:
            self.condition_immunites=[]
        self.alive=alive
        Creature.creatures.append(self)
    
    def get_stat_modifier(self, stat_name):
        stat_value = self.stats.get(stat_name)
        modifier = (stat_value - 10) // 2
        return modifier
    
    def roll_hp(self):
        if self.hp_dice and not self.hp:
            hp=Dice(self.hp_dice)
            self.hp=hp.roll(hp.n_dice*self.con)
            self.max_hp=self.hp

    def check(self, stat, skill, dc=10, skill_crit=False, adv=0 ):
        mod=0
        if stat in self.stats:
            mod = self.get_stat_modifier(stat)
        if skill in self.proficiencies:
            mod+=self.proficiency_bonus
        check=Check(ndx="1d20", mod=mod, dc=dc, skill_crit=skill_crit,adv=adv)
        result=check.get_result(self.name)
        return result

    def take_damage(self, amount, type=None, multiplier=1):
        if type in self.resistances:
            factor=self.resistances.get(type)
            if factor==0:
                print(f"{self.name} has an immunity to {type} damage")
            elif factor<1:
                print(f"{self.name} has a resistance to {type} damage")
            elif factor>1:
                print(f"{self.name} has a vulnerability to {type} damage")
        else:
            factor=1
        amount*=(factor*multiplier)
        amount=int(amount)
        if self.hp-amount<=self.max_hp:
            self.hp-=amount
        elif self.hp-amount>self.max_hp:
            self.hp=self.max_hp
        if (self.max_hp-self.hp)>=(2*self.max_hp):
            self.die()
        elif self.hp<0:
            self.hp=0
        if amount>0:
            print(f"{self.name} has taken {amount} point(s) of {type} damage")
            if self.hp<=0:
                print(f"{self.name} has died")
                self.conscious=False
            else:
                print(f"{self.name}'s remaining hp is {self.hp}")
        elif amount==0:
            print(f"{self.name} is immune to {type} damage")
        else:
            print(f"{self.name} has healed {amount*(-1)} point(s) of damage")
            print(f"{self.name}'s remaining hp is {self.hp}")
    
    def unconscious(self):
        if not self.important:
            self.die()
        self.death_saves={"Passes":0,"Failures":0}
        while True:
            death_save=Check(dc=10,skill_crit=True)
            result=death_save.get_result()
            if result=="Crit":
                self.hp=1
                break
            elif result=="Crit Fail":
                self.death_saves["Failures"]+=2
            elif result:
                self.death_saves["Passes"]+=1
            elif not result:
                self.death_saves["Failures"]+=1
            if self.death_saves["Passes"]==3:
                self.stable=True
            elif self.death_saves["Failures"]>=3:
                self.die()
    
    def die(self):
        self.alive=0
        self.conscious=False
    
    def attack(self, attack, target, adv=False):
        mod=self.get_stat_modifier(attack.stat)
        if attack.proficiency:
            mod += self.proficiency_bonus
        hit=Check(dc=target.ac,mod=mod,adv=adv)
        if not hit.get_result() or hit.get_result()=="Crit Fail":
            return False
        elif hit.get_result()=="Crit":
            crit=True
        else:
            crit=False
        damage=0






class Attack():
    def __init__(self,name, stat, proficiency, damage, damage_type,range=(5,5),  magical=False):
        self.name=name
        self.stat=stat
        self.proficiency=proficiency
        self.d_type=damage_type
        self.damage=damage

    
    


output=Check("1d20",-5, 20, False,1)
print(output.get_result())