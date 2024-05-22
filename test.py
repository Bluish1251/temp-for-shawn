list1 = []
list2 = []
list3 = []

#User chooses the list size for each list
listelem = int(input("How many elements do you want in each list? "))

#User inputs what they want in each list
for x in range(listelem):
    userinput1 = input("What do you want to be put in the first list? ")
    list1.append(userinput1) 

for x in range(listelem):
    userinput2 = input("What do you want to be put in the second list? ")
    list2.append(userinput2) 


#Prints the 2 list before merging them
print("The first list is: " + str(list1))
print("The second list is: " + str(list2))

#Merges the 2 list and merges them
list3 = list1 + list2
print("The merged list is: " + str(list3))