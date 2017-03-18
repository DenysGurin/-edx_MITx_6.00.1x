print ("Please think of a number between 0 and 100!")
low = 0
high = 100
guessed = False

while not guessed :
    guess = (high + low)/2
    print ("Is your secret number " + str(guess) + "?")
    var = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if var == 'l':
        low = guess    
    elif var == 'h':
        high = guess
    elif var == 'c':
        guessed = True
        print ("Game over. Your secret number was: " + str(guess))  
    else:
        print ("Sorry, I did not understand your input.")
    

    
        
        