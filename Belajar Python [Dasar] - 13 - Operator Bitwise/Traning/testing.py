# operasi bitwise 
# and,or,xor,or shiffting
a=int(input())
b=int(input())
print('--------(|)')
print(f"nilai {a} | nilai {b}={a|b},dengan binary {format(a|b,'08b')}")
print('--------(&)')
print(f"nilai {a} & nilai {b}={a&b},dengan binary {format(a&b,'08b')}")
print('--------(^)')
print(f"nilai {a} ^ nilai {b}={a^b},dengan binary {format(a^b,'08b')}")
print("----------(~)")
print(f"nilai {a} di not kan menjadi {~a}")