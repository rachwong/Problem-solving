input_file = open("input1.txt", "r")
file = input_file.read()
file = file.split()
input_file.close()

integer = int(file[0]) + 1
Case = 1
found = False
tidynumber = 0

for text in file[1:integer]:
    #print(text)
    #print("Case #" + str(Case) + ": ")#final string
    #for number in range(int(text),0,-1): #my iterator going through numbers down

    if (str(text)[-1:]) == str(0) and (str(text)[-2:]) == str(1):
        string = 1
        for i in range(len(str(text))):
            string = str(string) + str(0)
            #print(string)
            
        for number in range(int(string),0,-1):
                    #print(number)
                    ascending = "".join(sorted(str(number)))
                    if found == False:
                        if str(number) == ascending:
                            print("Case #" + str(Case) + ": " + str(number))
                            found = True
    
    elif len(str(text)) != 1:
        
        for number in range(int(text),0,-1):
            ascending = "".join(sorted(str(number)))
            if found == False:
                if str(number) == ascending:
                    print("Case #" + str(Case) + ": " + str(number))
                    found = True
        #print(text)
    elif len(str(text)) == 1:
            print("Case #" + str(Case) + ": " + str(text))#final string
            found = True

    
                        
    found = False
    Case += 1     
    
