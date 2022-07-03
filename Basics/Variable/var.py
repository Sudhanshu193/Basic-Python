var1 = "hello sir "
var2 ="hi"
print(var1 + var2) #here we done concetination of two string
var3 = 10
var4 = "20\n"
#print(var3 + var4)
#  # it show error because two different data type cannot be concetinate 
# For doing we have to typecast our variable 
print(var3 + int(var4)) 

#want to print a same line multiple time then we have to do

print(10* var4)# if we multiply it by integer data type it will give product value eg: print(10*var3)
#if you want to print 10 time then you have to typecast it in str
print(10*str(int(var4)+var3))