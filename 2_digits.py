two_digits = int(input("enter a number of 2 digits "))
asarot = int(two_digits/10)
ahadot = two_digits-asarot*10
print("Asarot digit = ",asarot,"\nAhadot digit = ",ahadot)


three_digits = int(input("enter a number of 3 digits "))
meot   = int(three_digits/100)
asarot = int((three_digits-meot*100)/10)
ahadot = three_digits-(meot*100+asarot*10)
print("Meot   digit = ",meot,"\nAsarot digit = ",asarot,"\nAhadot digit = ",ahadot)