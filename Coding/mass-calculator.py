proton=1.0073
mode="P"
while True:
    mz=input("Please give the m/z of the ion seen in Thompsons:\n>")
    if not mz or mz=="":
        continue
    try:
        mz=float(mz)
    except(ValueError):
        print("Invalid value")
        continue
    else:
        break
while True:
    charge=input("What charge does your ion have?\n>")
    if not charge or charge=="":
        continue
    try:
        charge=int(charge)
    except(ValueError):
        print("Invalid value")
        continue
    else:
        break
while True:
    charge_states=input("Please enter the highest charge state you would like to calculate. (All charge states from +1 to +n will be given)\n>")
    if not charge_states or charge_states=="":
        charge_states=5
        break
    try:
        charge_states=int(charge_states)
    except(ValueError):
        print("Invalid value")
        continue
    else:
        break

def calc_neutral(mz, charge):
    if charge>0:
        neutral_mass=(mz*charge)-(charge*proton)
    if charge==0:
        neutral_mass=mz
    if charge<0:
        return False
    return neutral_mass

nm=calc_neutral(mz, charge)
print(f"Neutral mass: {nm}")
for i in range(charge_states):
    targetmz=(nm+(i+1)*proton)/(i+1)
    print(f"For a charge of: {i+1}\nIon has m/z of: {targetmz}")
