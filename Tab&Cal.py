#importing pyfiglet 
import pyfiglet

text=pyfiglet.figlet_format("Table & Calc")
                                                   

print(text)


#simple python table generator //
def table ():
    
    n= int(input("Type numbar which Table you want $ Ex =1,2,3 =="))

#we use loop 

    for i in range (1,101):
    
    
        print(n, "*",i ,"=",i*n)
      
    
    
        if i == 10:
            break
                  
            
 
print("Type For Table == 1 \n"\
        "Type For calculator == 2")   
          
a= int(input("Type select choice=="))              
        
        
if a==1:
    print(table())
    
elif a==2:
    print("wait.....\n"\
    
    "\n"\
    
    
    
    
    
    
    "Done")   
def name():
    
    print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    number_1+number_2)

elif select == 2:
    print(number_1, "-", number_2, "=",number_1- number_2)

elif select == 3:
    print(number_1, "*", number_2, "=",
                    number_1* number_2)

elif select == 4:
    print(number_1, "/", number_2, "=",
                    number_1/number_2)
else:
    print("Invalid input")
    
    


                
       
