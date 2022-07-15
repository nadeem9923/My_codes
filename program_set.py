# python Program to check a given set has no element in common with other given set.

sn1 = {1,2,3}
sn2 = {4,5,6}
sn3 = {3}

print("Original sets:")
print (sn1)
print (sn2)
print (sn3)

print("Check sn1 has no elements in common with set sn2 set:")
print(sn1.isdisjoint(sn2))
print("Check sn1 has no elements in common with set sn3 set:")
print(sn1.isdisjoint(sn3))