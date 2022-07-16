string = input()  
flag = True;   
   
#Converts the given string into lowercase  
string = string.lower();  
   
#Iterate the string forward and backward, compare one character at a time   
#till middle of the string is reached  
for i in range(0, len(string)//2):  
    if(string[i] != string[len(string)-i-1]):  
        flag = False;  
        break;  
   
if(flag):  
    print("True");  
else:  
    print("False");  