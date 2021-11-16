a = int(input("How many students are in Class A? "))
b = int(input("How many students are in Class B? "))
c = int(input("How many students are in Class C? "))
#collects data from user
totdesks = a+b+c
if totdesks % 2 == 1:
  totdesks += 1
#changes odd numbers into even
print (totdesks//2, "desks are needed")