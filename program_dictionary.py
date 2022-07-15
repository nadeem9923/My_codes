#Python Program to print dictioary in table format in zip

my_dict = {'C1':[1,2,3], 'C2':[4,5,6], 'C3':[7,8,9]}
for row in zip(*([key] + (value) 
	           for key, value in my_dict.items())):
	print(*row, " ")