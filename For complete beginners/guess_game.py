flag = True
while flag:
    print("Welcome to guessing game let's see how lucky you are ")
    print("HINT: Guess smartly and try to guess interval as big as posssible")

    import random  

    n=random.randint(1,100)    #in-built function that returns random integer between 1-100
    score = 7                  # This is your initial score, if your luck enough you can guess in first try
    guess_number=int(input("Enter an interger from 1 to 100: "))   

    while n!=guess_number:    #taking input untill you guess a right number.

      if guess_number<n:
        print("guess higher number than this.")
        score-=1
        guess_number=int(input("Enter an interger from 1 to 100: "))     

      elif guess_number>n:
        print("guess a lower number than this.")
        guess_number=int(input("Enter an interger from 1 to 100: "))
        score-=1
      else:
        break

    print("there you go !! you guessed it right \n.")
    print("your score is " , score)
    if score == 7:
        print("God is with you and within you You scored perfect 7")
    if score>=5 and score<7:
        print("You are lucky than most of other people \n")
        
        print("Wanna score perfect .Press R to replay \n ")
        
        print('Press Q to quit')
        s = input()

        if s == 'Q' or s=='q':
            flag = False

    else:
        print("you can do better than this .Want to play again! press R to play again")
        print("Press Q to quit the game")

        s = input()

        if s == 'Q' or s=='q':
            flag = False 

print("See you soon")
#You can always guess a number in maximum 7 guesses.Can you prove how ?
# I encourage you to think by your own and if you are not able to find the answer go to the link given below


#https://math.stackexchange.com/questions/512994/guessing-a-number-between-1-and-100-in-7-guesses-or-less




