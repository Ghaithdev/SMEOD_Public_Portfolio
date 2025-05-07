from random import randint
class Dice():
    def __init__(self, ndx):
        self.n_dice=int(ndx.split("d")[0].strip())
        self.size=int(ndx.split("d")[1].strip())
    
    def roll(self):
        result=0
        for i in range(self.n_dice):
            result+=randint(1,self.size)
        return result

class Check(Dice):
    def __init__(self,ndx="1d20", mod=0, dc=10, skill_crit=False,adv=0):
        super().__init__(ndx)
        self.adv=adv
        self.mod=mod
        self.can_crit=skill_crit
        self.dc=dc
        print(self.n_dice,f"d{self.size}",self.mod,self.can_crit,self.dc,self.adv)
        
        
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
    
    def get_result(self):
        self.result, self.crit = self.roll()
        if self.can_crit:
            if self.crit>0:
                pass
            elif self.crit<0:
                pass
        if self.result>=self.dc:
            outcome="pass"
        else:
            outcome="fail"
        print(f"You rolled a {self.raw_roll}, after modifiers that is a {self.result} \nThe DC was {self.dc} so you {outcome}ed the roll")
            
class Attack():
    def __init__(self, attacker, target, attack_name):
        self.stat=attacker.attacks[attack_name]["attack_stat"]
        self.damage=attacker.attacks[attack_name]["damage_dice"]
    

output=Check("1d20",-5, 20, False,1)
print(output.get_result())