# a = 10 ,a adalah variabel dengan nilai 10

# Tipe data: Angka satuan yang gak ada komnya (integer) 
data_integer=1

print("data:",data_integer,)
print("-bertipe:",type(data_integer))

# tipe data :angka dengan koma (float)
data_float=1.5
print("data:",data_float,)
print("-bertipe:",type(data_float))

# tipe data :kumpulan karater (string)
data_string="ucup 10"
print("data:",data_string,)
print("-bertipe:",type(data_string))

# tipe data :biner True/False (string)
data_bool= False
print("data:",data_bool,)
print("-bertipe:",type(data_bool))

## Tipe data Khusus 

# Bilangan kompleks
data_complex=complex(5,6)
print("data: ",data_complex)
print("Bertipe :",type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double
data_c_double=c_double(10.5)
print("data: ",data_c_double)
print("Bertipe :",type(data_c_double))
