import random as rnd
pool=[]

while True:
    new_name=input("Please enter name, if done type 'done'\n>")
    if new_name.lower() == "done" or not new_name:
        break #exit loop
    if new_name.lower().capitalize() not in pool:
        pool.append(new_name.lower().capitalize())
        print(f"{new_name} successfully added to pool")
    else:
        print("Name already in pool")

print(f"pool of names is: {pool}")
order=[]
while len(order)<24:
    working_pool=rnd.sample(pool, len(pool))
    for item in working_pool:
        order.append(item)

i=0
for item in order:
    i+=1
    print(f"Day {i} is {item}")