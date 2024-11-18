d="2024-01-31 12:05:15" #date time data
"2024-01-01" #date data
"15:15:20" #time data
 
ans='2024-01-35'


class samay:

    def __init__(self,year,month,day,hour,min,sec):
        if month>12:
            print('wrong month')
            return 0
        self.year=year
        self.month=month
        self.day=day
        self.hour=hour
        self.min=min
        self.sec=sec

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.min}:{self.sec}"
    

d1=samay(2024,15,1,15,45,2)
print(d1)