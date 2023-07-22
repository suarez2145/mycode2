#!/usr/bin/python3


def main():
    #  declare function that will run to show the user the instructions for the game
    def showInstructions():
            print(''' Welcome to the Maze!
                        ========
                        Commands: go [direction] and get [item]
                ''')
            
            
    # declare and outline my maze rooms/ corridors dictionary
    maze = {
        
        'Main Entrance' : {
                'south' : 'South Entrance',
                'north' : 'North Entrance'
            },
        'North Entrance' : {
                'south' : 'Main Entrance'
            },
        'South Entrance' : {
                'north' : 'Main Entrance'
            }
    }
    
    currentRoom = 'Main Entrance'

    showInstructions()
    #  declare variable to hold the current steps the user has taken 
    paces = 0
    
    def showStatus():
        
        """determine the current status of the player"""
        # print the player's current location
        print('---------------------------')
        print('You are in the The Maze: ' + currentRoom)
        # print what the player is carrying
        print('Inventory: is empty')
        # check if there's an item in the room, if so print it
        print("---------------------------")
        print(" youve taken: " + str(paces) + " paces so far.... hurry up...bud")
    

    #  function that holds while loop that runs the game while its waiting on the user input (next move)
    def game():
            #  setting runGame variable to false so i can set it to True when  i want to end the game 
            runGame = False
            userEnter = input("Do you wish to enter? [Yes / No]")
            if userEnter == "no":
                runGame = False
                print(" Ok see you later aligator...")
            if userEnter == "yes":
                runGame = True
                print("Lets begin >>>>")
            while runGame == True:
                showStatus()
                move = ''
                while move == '':  
                    move = input('>')
                    move = move.lower().split(" ", 1)
                if move[0] == "go":
                    # using the nonlocal key word to declare and update the paces global variable
                    nonlocal currentRoom
                    if move[1] in maze[currentRoom]:
                        currentRoom = maze[currentRoom][move[1]]
                    # using the nonlocal key word to declare and update the paces global variable
                    nonlocal paces
                    paces += 1
                    print(" you moved")
                #  if the user TYPES 'q' runGame will be False and the while loop will terminate and the game will no longer prompt the user for an input ending the game
                if move[0] == "q":
                    runGame = False 
                    print("Goodbye")
                
            
    game()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()