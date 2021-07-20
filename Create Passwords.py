
import random
Password_list = []
while True:
    
    q1 = input("Enter your name: ")
    q2 = input("Enter your favourite color: ")
    q3 = input("Enter your pet name: ")
    q4 = input("Enter your favorite hobby: ")
    q5 = input("Enter your favorite food: ")
    while True:
       
        length= input("Give the length of password you want (only numbers,greater or equally 4):")
      
        try:
            val = int(length)
            if val>=4:
                print("Valid.Input number is: ", val)
                break;
            elif val<4:
                print("Please enter a greater number!Input number is smaller than 4: ", val)
        except ValueError:
            print ("This is not a number! Please enter a valid number!")
    
    q_list=[q1,q2,q3,q4,q5]#Λιστα που κραταει ολα τα string που εδωσε ο χρηστης

    
    Lower_Characters = [i for q in q_list for i in q] 
    Upper_Characters = [x.upper() for x in Lower_Characters]
    Symblos = [ '@', '%', '#',':','$', '?', '/', '|','>','=', '*', '(', ')']
    Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    myList=[Lower_Characters,Upper_Characters,Symblos,Digits]
    
    while True:
        password = '' 
        if val==4:
            
            password += random.choice(Lower_Characters)
            password += random.choice(Upper_Characters)
            password += random.choice(Symblos)
            password += random.choice(Digits)
        elif val>4:
            len=val-4 
            password += random.choice(Lower_Characters)
            password += random.choice(Upper_Characters)
            password += random.choice(Symblos)
            password += random.choice(Digits)
            for i in range(len):
                random_List = random.choice(myList) 
                password += random.choice(random_List)
        print(password)
        Password_list.append(password)

       
        q_choice=input("Do you like this password press y to confirm or press n to create new password: ")
        if q_choice=='y':
            print("Your password is: "+password)
            print("All your password we have create is:")
            print(Password_list)
            break;
      
    q_choice_1=input("Do you want to start from the beginning press y to confirm or press n to exit: ")
    if q_choice_1=='y':
        print("You press y,now you answer the questions")
    elif q_choice_1=='n':
        print("Your password is: "+password)
        print("All your password we have create is:")
        print(Password_list)
        print("You press n,exit! Good bye!")
        break;
      
    
    
   
    
            