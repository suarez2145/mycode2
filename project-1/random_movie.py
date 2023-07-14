#!/usr/bin/python3
def main():
    # im prompting the user for an answer so i can proceed
   userAnswer = input("Are you in the mood for a Movie? (yes/no)").lower()
   # my first if statement if yes then ill launch into my while loop
   if(userAnswer == "yes"):
       print("Ok lets get started...")
       userAge = input("Are you over 18? (yes/no)").lower()
       # setting my variable to True so i can stop my while loop later
       userThinking = True

       while userThinking == True:
           if(userAge == "yes"):
               userScifi = input("You like SciFi stuff? (yes/no)").lower()
               if(userScifi == "yes"):
                   print("Well then i recommend The CloverField Paradox")
                   # Setting to False to stop the code 
                   userThinking = False
               if(userScifi == "no"):
                   userNewQ = input("Please choose 1 of the following Genres or were done here...thanks (Romantic/Documentary/Action)").lower()
                   if(userNewQ == "romantic"):
                       print("I really cant help you here bud...sorry bye")
                       userThinking = False
                   if(userNewQ == "documentary"):
                       print("Ok yea i can work with this..I recommend The Secrets Of Hillsong")
                       userThinking = False
                   if(userNewQ == "action"):
                       print("Ok this is a good one... Extraction2 on netflix")
                       userThinking = False
           if(userAge == "no"):
               print("Your too young see ya...")
               userThinking = False

   if(userAnswer == "no"):
               print("Very well... Ill leave you alone")
               restart = input("you Sure ?(yes/no)")
               if(restart == "no"):
                   main()
               else:
                   print("Ok bye LOSER!")


if __name__ == "__main__":
    main()
