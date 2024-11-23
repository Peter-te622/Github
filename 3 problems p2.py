str1 = input("Please enter your line: ")
total = 0
for i in range(len(str1)):
    if(str1[i] == 'd'):
        if(str1[i+1] == 'o' and str1[i+2] == 'd'):
            total+=1
print("Number of times of dod occurs: " + str(total))