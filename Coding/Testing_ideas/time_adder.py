def add_time(start, duration, start_day=None):
  base=0
  spoint=0
  
  weekday=None
  weekdays={"sunday":0,"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"saturday":6} 
  if start_day:
      print(start_day.lower())
      day=start_day.lower()
      if day in weekdays:
          spoint=(weekdays[day])
          print(spoint)
  h_hour=int(start.split(":")[0])
  if h_hour==12:
      h_hour=0
  antipasti=start.split(" ")[1].upper()
  if antipasti=="PM":
      h_hour+=12
  m_min=int(start.split(":")[1].split(" ")[0])    
  base+=m_min+(h_hour*60)
  add_hour=int(duration.split(":")[0])
  add_min=int(duration.split(":")[1])
  add_min+=add_hour*60
  total_min=base+add_min
  day=int(total_min/1440)
  print(day)
  total_min=(total_min%1440)
  hour=int(total_min/60)
  if hour>=12:
      meridian="PM"
  else:
      meridian="AM"
  hour=(hour%12)
  if hour==0:
    hour=12
  min=str(total_min%60).zfill(2)

  
  if start_day:
      new_day=(spoint+(day%7))%7
      print(new_day)
      for key, value in weekdays.items():
          if value == new_day:
            weekday=str(key).capitalize()
            print(weekday) 
  if day<1:
      days_later=None
  elif day==1:
      days_later="(next day)"
  else:
      days_later=f"({day} days later)"

  
  time_out=f"{hour}:{min} {meridian}"
  
  new_time=time_out
  if days_later:
      new_time=f"{time_out} {days_later}"
  if start_day:
      if days_later:
          new_time=f"{time_out}, {weekday} {days_later}"
      else:
          new_time=f"{time_out}, {weekday}"
  return new_time
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("8:16 PM", "466:02", "monday"))