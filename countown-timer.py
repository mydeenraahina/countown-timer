from datetime import datetime,date
class CountownTimer:
    
    def __init__(self):
        print(f"Set Countown Timer!")
        print(datetime.now())
        try:
            self.getting_year=int(input(f"Enter year(YYYY) "))
            self.getting_month=int(input(f"Enter month(MM) "))
            self.getting_day=int(input(f"Enter day(DD) "))
            self.getting_hour=int(input(f"Enter hour(HH) "))
            self.getting_minute=int(input(f"Enter minute(MM) "))
            self.getting_second=int(input(f"Enter second(SS) "))
        except ValueError:
            print(f"Enter a valid date/time value")
            exit()
    def time_and_date_calculation(self):
        dt=datetime(self.getting_year,self.getting_month,self.getting_day,self.getting_hour, self.getting_minute, self.getting_second)
        current_datetime=datetime.now()
        if self.getting_year<current_datetime.year:
            return f"Times up!"
        else:
            result=dt-current_datetime
            return "Remaining Time!..",result

obj=CountownTimer()
print(obj.time_and_date_calculation())
getting_choice=input("Do you want to continue setting the countown timer[yes\no]")
if  getting_choice.casefold()=="yes":
    obj=CountownTimer()
    print(obj.time_and_date_calculation())
elif getting_choice.casefold()=="no":
    print("Countdown timer setup complete. Exiting...")
    exit()
else:
    print(f"please check your input!")
    exit()

                    
        
    
    
                     
