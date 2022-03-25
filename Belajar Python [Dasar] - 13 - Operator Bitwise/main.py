# Episodef operator bitwise,operasi biner,binary
a=9
b=5
# bitwise OR(|)
c=a|b
print("=======OR========")
print("nilai :",a,"Binary ",format(a,"08b"))
print("nilai :",b,"Binary ",format(b,"08b"))
print("------------ (|)")
print("nilai :",c,"Binary ",format(c,"08b"))

# bitwise AND(&)
c=a&b
print("=======AND========")
print("nilai :",a,"Binary ",format(a,"08b"))
print("nilai :",b,"Binary ",format(b,"08b"))
print("------------ (&)")
print("nilai :",c,"Binary ",format(c,"08b"))

# bitwise XOR(^)
c=a^b
print("=======AND========")
print("nilai :",a,"Binary ",format(a,"08b"))
print("nilai :",b,"Binary ",format(b,"08b"))
print("------------ (^)")
print("nilai :",c,"Binary ",format(c,"08b"))

# bitwise NOT(~)
c=~a
print("=======XOR========")
print("nilai :",a,"Binary ",format(a,"08b"))
print("--------- (~)")
print("nilai :",c,"binary :",format(c,"08b"))
print("------------------- (XOR)")
d=0b00001001
e=0b11111111
print("nilai :",e^d,",binary :",format(e^d,"08b"))

# shiffting right
c=a>>2
print('========>>=======')
print("nilai a:",a," binary :",format(a,"08b"))
print("------------ (>>)")
print("nilai a:",c," binary :",format(c,"08b"))
# shiffting left
c=a<<2
print('========>>=======')
print("nilai a:",a," binary :",format(a,"08b"))
print("------------ (>>)")
print("nilai a:",c," binary :",format(c,"08b"))

