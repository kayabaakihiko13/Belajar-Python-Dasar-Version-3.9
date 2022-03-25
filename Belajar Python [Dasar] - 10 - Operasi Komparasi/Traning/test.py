print("logika Proporsional".center(50,"="))
print("Entar The Value")
a=int(input("1/0:"))
b=int(input("1/0:"))
print(f"""Choice your operator
1.AND
2.OR
3.Impelies
4.bi-Implikasi""")
in_=int(input())
if in_ == 1:
    print(f"a AND b ={a & b}")
elif in_ == 2:
    print(f"a AND b ={a & b}")
elif in_ ==3:
    print(f"a AND b ={~a & b}")
elif in_ ==4:
    print(f"a AND b ={~a & b}")

    

