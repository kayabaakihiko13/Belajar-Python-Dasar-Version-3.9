# operasi komperasi

#setiap hasil dari operasi komperaso adalah boolean

# >,<,>=,<=,!=.==,is,is not
a=4
b=2

# lebih besar dari
print("======Lebih Besar Dari=====")
hasil=a>3
print(a,'>',3,"=",hasil)
hasil=b>3
print(b,'>',3,"=",hasil)
hasil=b>2
print(b,'>',2,"=",hasil)

# kurang dari <
print("=======Kurang Dari======")
hasil=a<3
print(a,'<',3,"=",hasil)
hasil=b<3
print(b,'<',3,"=",hasil)
hasil=b<2
print(b,'<',2,"=",hasil)

# Lebih dari sama Dengan >=
print("=======Lebih Dari Sama Dengan======")
hasil=a>=3
print(a,'>=',3,"=",hasil)
hasil=b>=3
print(b,'>=',3,"=",hasil)
hasil=b>=2
print(b,'>=',2,"=",hasil)
# Kurang dari sama dengan <=
print("=======Kurang  Dari Sama Dengan======")
hasil=a<=3
print(a,'<=',3,"=",hasil)
hasil=b<=3
print(b,'<=',3,"=",hasil)
hasil=b<=2
print(b,'<=',2,"=",hasil)

# Sama Dengan  (==)
print("=======Sama Dengan======")
hasil=a==4
print(a,'==',4,"=",hasil)
hasil = b==4
print(b,'==',4,"=",hasil)
# Tidak sama dengan
print("=======Kurang  Dari Sama Dengan======")
hasil=a!=4
print(a,'!=',4,"=",hasil)
hasil=b!=4
print(b,'!=',4,"=",hasil)

# "is" sebagai obj komperasi object indentity

print("=======Object Identity======")
x = 5 # ini adalah membuat object
y =5 
print("nilai x",x,", id x = ",hex(id(x)))
print("nilai x",y,", id x = ",hex(id(y)))
hasil = x is y 
print(x,'is', y,"=",hasil)

# "is not" sebagai obj komperasi object indentity
print("=======Object Identity is not======")
x = 5 # ini adalah membuat object
y =6 
print("nilai x",x,", id x = ",hex(id(x)))
print("nilai x",y,", id x = ",hex(id(y)))
hasil = x is not y
print(x,'is', y,"=",hasil)

