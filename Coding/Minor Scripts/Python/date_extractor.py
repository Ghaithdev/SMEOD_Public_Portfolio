from datetime import datetime

monthconvdict={
    "Jan":"01",
    "Feb":"02",
    "Mar":"03",
    "Apr":"04",
    "May":"05",
    "Jun":"06",
    "Jul":"07",
    "Aug":"08",
    "Sep":"09",
    "Oct":"10",
    "Nov":"11",
    "Dec":"12",
}

dates=["05Oct29","01Jan22","33May19","31Obt65"]
for date in dates:
    try:
        day=(date[:2])
        month=date[2:5]
        year=date[5:]
        date_string=f"{day}, {month}, {year}"
        date_format = '%y-%b-%d %H:%M:%S'
        numdate=datetime.strptime(date_string, '%d, %b, %y')
        print(numdate)
    except(ValueError):
        print("Date in unexpected format")
