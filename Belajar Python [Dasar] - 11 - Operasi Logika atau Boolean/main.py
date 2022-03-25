# operasi logika atau boolean

# not, or ,and ,xor

# not
a=True
c = not a
print("data a: ",a) 
print('--------NOT-----')
print("data c: ",c) 

# OR jika salah satu True maka hasilnya True
print('-------OR-----')
a=True
b=True
c = a or b
print(a,"OR",b,"=",c)
a=True
b=False
c = a or b
print(a,"OR",b,"=",c)
a=False
b=True
c = a or b
print(a,"OR",b,"=",c)
a=False
b=False
c = a or b
print(a,"OR",b,"=",c)
# and jika dua buah True maka hasilnya True
print('-------and-----')
a=True
b=True
c = a and b
print(a,"and",b,"=",c)
a=True
b=False
c = a and b
print(a,"and",b,"=",c)
a=False
b=True
c = a and b
print(a,"and",b,"=",c)
a=False
b=False
c = a and b
print(a,"and",b,"=",c)

# ^ dia akan True jika salah satu True
print('-------^-----')
a=True
b=True
c = a ^ b
print(a,"^",b,"=",c)
a=True
b=False
c = a ^ b
print(a,"^",b,"=",c)
a=False
b=True
c = a ^ b
print(a,"^",b,"=",c)
a=False
b=False
c = a ^ b
print(a,"^",b,"=",c)