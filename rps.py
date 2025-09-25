import random



options = {"rock":"scissors","paper":"rock","scissors":"paper"} #We use dictionnaries to avoid making long if-else statements were the key is the choice
                                                                #The value is the choice the key would win against in example(rock would win on scissors)

options_list = ["rock","scissors","paper"]

running = True


while running: 
    choice = input("Enter your choice: ").lower()    #Enter user choice
    if choice in options_list:                     #Checks if the choice is valid
        
        bot_choice = random.choice(options_list)   #picks a random choice
        print(f"The computer chose {bot_choice}")
        
        if choice == bot_choice:
            print("Oh thats a draw!!")
        elif options.get(choice) == bot_choice:
            print("you won, well played")
        else:
            print("you lost...")
        
        if not input("Would you like to play again?(y/n): ").lower() == "y":
            print("Thank you for playing Python rock paper scissors game !!!!!!!")
            running = False
    else:
        print("Please enter a valid choice")

