new_cards=int(input("Number of new cards daily: "))
card_interval=[1]
card_increase=2.5
for i in range(365):
    card_interval.append(round((card_interval[i]*card_increase)+.5))
n_days=int(input("Please enter an integer number of days: "))
day_temp=n_days
interval_selecteed=0
for interval in card_interval:
    day_temp-=interval
    if day_temp<=0:
        print(f"After {n_days} days there would be {interval_selecteed*new_cards+new_cards} cards to review")
        break
    interval_selecteed+=1
12
