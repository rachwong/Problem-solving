input_file = open("input1.txt", "r")
file = input_file.read()
file = file.split()
input_file.close()

integer = int(file[0]) + 1
Case = 1
found = False
tidynumber = 0

#tidy number is where numbers are ascending. we want to find highest tidy number up to a certain given number
#my code iterates down from certain given number, generates what the tidy number would be by sorting the numbers so they are ascending and then comparing with the actual number to see whether
#that number is tidy.

for text in file[1:integer]:
    #checking for number ending in 0??
    if (str(text)[-1:]) == str(0) and (str(text)[-2:]) == str(1):
        string = 1
        for i in range(len(str(text))):
            string = str(string) + str(0)
         
        #actual code here
        #Checks each number against a sorted version of the number to see whether tidy or not
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
        
    #if number is length 1 it is tidy
    elif len(str(text)) == 1:
            print("Case #" + str(Case) + ": " + str(text))#final string
            found = True

    
                        
    found = False
    Case += 1     
    
