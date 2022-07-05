var1 = "hello today i took {} rupees"
rs = 90
print(var1.format(rs))# here formating help to fill the blank in their.

date = 4
day = "Monday"
lang= "python"
var2 ="Today is {} june {} . Today i will start learing {}."
print(var2.format(date, day, lang))


var3 ="Today is {1} june {0} . Today i will start learing {2}."
print(var3.format(date, day, lang)) #here i used indexing of that was aloted to the values and rearranged them
#its like array but you can fill any thing at any place if you have its index.

