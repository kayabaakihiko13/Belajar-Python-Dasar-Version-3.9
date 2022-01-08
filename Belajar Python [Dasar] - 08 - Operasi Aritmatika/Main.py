# operasi aritmatika

a=10
b=3

# operasi tambah +
hasil=a+b
print(a,"+",b,"=",hasil)

# operasi pengkuranagn -
hasil=a-b
print(a,"-",b,"=",hasil)

# operasi perkalian *
hasil=a*b
print(a,"*",b,"=",hasil)

# operasi pembagian /
hasil=a/b
print(a,"/",b,"=",hasil)

# operasi eksponen (pangkat)
hasil=a**b
print(a,"**",b,"=",hasil)

# operasi modulus (%)
hasil=a%b
print(a,"%",b,"=",hasil)

# operasi flor division //
hasil=a//b
print(a,"//",b,"=",hasil)

# prioritas operasi,operational precedence
"""
    1.


"""
x=3
y=2
z=4

hasil=x ** y * z + x / y -y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,"=",hasil)


hasil= x + y *z
print(x,"+",y,"*",z,"=",hasil)
hasil= (x + y) *z
print((x,"+",y),"*",z,"=",hasil)