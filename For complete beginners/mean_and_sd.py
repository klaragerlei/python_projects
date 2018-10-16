import pandas as pd

true = 1
sum = 0
file = open("Number_file.txt","w")

while(true):
	n = input("Enter the number you want to save in file. leave blank to escape :")
	if n == '':
		true = 0
	else:
		file.write(n)
		file.write("\n")

file.close()

file = open("Number_file.txt","r")
element_list = file.readlines()
file.close()

for element in element_list:                           #calculating mean by sum and divide method
	sum += element

mean1 = sum/len(element_list) 

l2 = list(map(lambda x : int(x), l2))
dataframe = pd.DataFrame(l2)

sd = dataframe.values.std(ddof=1)                      #calculating standard deviation
mean = dataframe[0].mean()                             #calculating mean using pandas library