import os
import datetime as dt
print("Put Data".center(50,'='))
input_name=input("enter yourname\t:")
input_y,input_m,input_d=int(input("year:")),int(input('month:')),int(input("date:"))
input_add=input("addreas:")
input_bloTy=input("BloodType:")
os.system("cls")
age=(dt.date.today()-dt.date(input_y,input_m,input_d))
print("KTP".center(50,'='))
print(f"""Name:{input_name.title()}
DOB:{dt.date(input_y,input_m,input_d)}
Years:{age.days//365}
addreas:{input_add}
BloodType:{input_bloTy.upper()}
""")
