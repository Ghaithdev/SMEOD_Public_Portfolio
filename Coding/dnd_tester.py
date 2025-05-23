import random as rnd
crit_skill_checks=False

class creature():
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
                resistances=None) -> None:
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
        if attacks==None:
            attacks={}
        self.attacks=attacks
        if resistances==None:
            resistances={}
        self.resistances=resistances
        creature.creatures.append(self)
    
    def get_stat_modifier(self, stat_name):
        stat_value = self.stats.get(stat_name)
        modifier = (stat_value - 10) // 2
        return modifier
    
    def roll_hp(self):
        if self.hp_dice and not self.hp:
            parse=parse_dice(self.hp_dice)
            n_dice=parse[0]
            size=parse[1]
            result=dmg_roll(n_dice,size,size*(self.get_stat_modifier('Con')))
            self.hp=result
            self.max_hp=result

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
        elif amount<0:
            self.hp=self.max_hp
        if amount>0:
            print(f"{self.name} has taken {amount} point(s) of {type} damage")
            if self.hp<=0:
                print(f"{self.name} has died")
            else:
                print(f"{self.name}'s remaining hp is {self.hp}")
        elif amount==0:
            print(f"{self.name} is immune to {type} damage")
        else:
            print(f"{self.name} has healed {amount*(-1)} point(s) of damage")
            print(f"{self.name}'s remaining hp is {self.hp}")

            
def attack(attacker, target, attack_name):
    attack_stat=attacker.attacks[attack_name]["attack_stat"]
    attack_damage=attacker.attacks[attack_name]["damage_dice"]
    n_dice, dice_type=parse_dice(attack_damage)
    attack_damage_type=attacker.attacks[attack_name]["damage_type"]
    attack_stat_mod=attacker.get_stat_modifier(attack_stat)
    roll_result=basic_roll(attack_stat_mod,"adv")
    print(f"{attacker.name} rolled a {roll_result}")
    crit=crit_check(roll_result,attack_stat_mod)
    target_ac=target.ac
    if crit=="success":
        print("I got a critical hit")
        n_dice, dice_type= parse_dice(attack_damage)
        damage=n_dice*dice_type
        damage+=dmg_roll(n_dice, dice_type, attack_stat_mod)
        target.take_damage(damage, type=attack_damage_type)
    elif crit=="failure":
        print("I got as critical miss")
    elif roll_result>=target_ac:
        print(f"that hits {target.name}")
        target.take_damage(dmg_roll(n_dice, dice_type, attack_stat_mod), type=attack_damage_type, multiplier=1)
    else:
        print(f"that does not hit {target.name}")


def parse_dice(nds):
    n_dice=int(nds.split("d")[0].strip())
    size=int(nds.split("d")[1])
    return(n_dice, size) 

def dmg_roll(n_dice, size, mod=0):
    result=0
    for die in range(n_dice):
        result+=(rnd.randint(1,size))
    result+=mod   
    return(result)

def basic_roll(mod, advantage=None):
    i=1
    if advantage:
        i=2
    min=None
    max=None
    roll=0
    roll+=(rnd.randint(1,20))
    roll+=mod
    if not min or roll<min:
        min=roll
    if not max or roll>max:
        max=roll
    if advantage=="adv":
        return(max)
    elif advantage=="dis":
        return(min)
    elif advantage=="emp":
        if abs(min-10)>abs(max-10):
            return(min)
        else:
            return(max)
    return(roll)

def crit_check(roll, mod):
    if roll-mod==20:
        crit="success"
    elif roll-mod==1:
        crit="failure"
    else:
        crit=None
    return(crit)

def skill_check_result(roll, dc, crit=None):
    if crit_skill_checks:
        if crit:
            print("Crit Success")
            return(True)
        elif not crit:
            print("Crit Fail")
            return(False)
    if roll>=dc:
        print("Sucess")
        return(True)
    else:
        print("Failure")
        return(False)
        

# Goblin
Goblin = creature(
    name="Goblin",
    ac=15,
    proficiency_bonus=2,
    proficiencies=None,
    hp_dice='2d6',
    hp=None,
    cr=1/4,
    stats={"Str": 8, "Dex": 14, "Con": 10, "Int": 10, "Wis": 8, "Cha": 8},
    attacks={
    'Scimitar': {
        'attack_stat': 'Dex',
        'range': (5, 5),
        'damage_dice': '1d6',
        'damage_type': "slashing"
    },
    'Shortbow': {
        'attack_stat': 'Dex',
        'range': (80, 320),
        'damage_dice': '1d6',
        'damage_type': "piercing"
    }
    },
    resistances={}
)

# Lizardfolk
Lizardfolk = creature(
    name="Lizardfolk",
    ac=15,
    proficiency_bonus=2,
    proficiencies=None,
    hp_dice='3d6',
    hp=None,
    cr=1/2,
    stats={"Str": 15, "Dex": 10, "Con": 13, "Int": 7, "Wis": 12, "Cha": 7},
    attacks={
        'Bite': {'attack_stat': 'Str', 'range':(5,5), 'damage_dice': '1d6','damage_type': "piercing"},
        'Heavy Club': {'attack_stat': 'Str', 'range':(5,5), 'damage_dice': '1d8','damage_type': "blugeoning"}
    },
    resistances={}
)

# Owlbear
Owlbear = creature(
    name="Owlbear",
    ac=13,
    proficiency_bonus=2,
    proficiencies=None,
    hp_dice='5d10',
    hp=None,
    cr=3,
    stats={"Str": 20, "Dex": 12, "Con": 17, "Int": 3, "Wis": 12, "Cha": 7},
    attacks={
        'Beak': {'attack_stat': 'Str', 'range':(5,5), 'damage_dice': '2d8','damage_type': "piercing"},
        'Claws': {'attack_stat': 'Str', 'range':(5,5), 'damage_dice': '2d8','damage_type': "slashing"}
        },
    resistances={}
)
# Alchemist
Alchemist = creature(
    name="Alchemist",
    ac=12,
    proficiency_bonus=2,
    proficiencies={"Arcana", "Investigation", "Medicine"},
    hp_dice='13d8',
    hp=None,
    cr=4,
    stats={"Str": 10, "Dex": 14, "Con": 16, "Int": 18, "Wis": 12, "Cha": 14},
    attacks={
        'Staff': {'attack_stat': 'Dex', 'range': (5, 5), 'damage_dice': '1d4'},
        'Alchemical Bomb': {'attack_stat': 'Int', 'range': (30, 60), 'damage_dice': '3d6','damage_type': "fire"}
    },
    resistances={"poison":0.5,"fire":0.5}
)
for instance in creature.creatures:
    instance.roll_hp()
print("Goblin's turn")
for i in range(3):
    attack(Goblin, Owlbear, "Scimitar")
    if Owlbear.hp==0:
        break
print("Owlbear's turn")
for i in range(2):
    attack(Owlbear,Goblin, 'Claws')
    if Goblin.hp==0:
        break