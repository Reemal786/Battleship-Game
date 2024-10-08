# Reemal Hoor Manhattan College Software Engineering Project

numberOfTurns = 0
#variable that updates the number of times the user takes a turn
numberOfHits = 0
#variable for the number of times the users input is a hit

correctGuesses = []
#variable that intakes a string of how many times the users guess was correct
incorrectGuesses = []
#variable that intakes a string of how many times the users guess was incorrect

def main():
    nameofFile = OpenFile()
    #here we are using the OpenFile function to open the file
    boatPlacementsList = PlaceBoats(nameofFile)
    #placing the boards onto the grid from the information of the file
    initializeBoard()
    #using fucntion to create the board for the user
   
    while numberOfTurns < 15 and numberOfHits < 12:
        #creating a loop asking the user for their guess up until the number of turns is less than 15
        #and the number of the hits is less than 12
        #less than 15 and 12 because I'm starting the variables from 0

        playerGuess = ObtainMove()
        #uses function above to obtain the players move
        CheckMove(playerGuess, boatPlacementsList)
        #checks the players move against the list of the boat placements. runs the function
        #checkmove to print a hit or miss and also removes the arrray from the boat list if its a hit

    if numberOfHits == 12:
        print("CONGRATS, YOU WON!")
        #if the number of hits is equal to 12, display message above. player has won the game
        print("Your percentage is ", calculatePercentage(numberOfHits,numberOfTurns),"%")
        #displays the users percentages by calling the the calculatePercentage function
    else:
        print("GAME OVER, SORRY")
        #if users turns reaches its limit but the hits are under 12, displays message above
        print("Your percentage is ", calculatePercentage(numberOfHits,numberOfTurns),"%")

    # PrintBoard()

def OpenFile():
    fileName = input("Enter the name of your file now: ")
    #asks user to input the file name, continues asking user the file name until it is correct
    openedFile=open(fileName,'r')
    #opens the file in read mode to obtain the information inside the file
   
    while (openedFile):

        fileLines = openedFile.readlines()
        #used readlines to return a list of each line in the file
        numberofLines = len(fileLines)
        #variable numberofLines is equal to the length of the lines read in the file
       
        if numberofLines ==13:
            #once the correct file has been inserted.the following statements are printed.
            print("Initializing Board....\n")
            print("Game Board Has Been Initialized...\n")
            print("WELCOME TO BATTLESHIP :)\n")
            openedFile.close() #close file then return
            return fileName

        elif numberofLines == 0:
            #in order to determine whether the file is correct or not the program makes sure that there are 13 lines in the txt file
            print("File Is Empty. Try Again")
            #if there aren't, the code prints the message above
            openedFile.close()
            OpenFile()
            #returns back to OpenFile function where it asks the user to enter the name
        elif numberofLines>13:
            print("Bad File. Try Again")
            openedFile.close()
            OpenFile()


def PlaceBoats(nameofFile):
    openedFile=open(nameofFile,'r')

    if(openedFile):
        next(openedFile) #skips first line which contains (rows, columns, and boats)
        boatsPlacementMap = {}
   
        readLines = [1,2,3,4,5,6,7,8,9,10,11,12]
        #skips the fist line of (row, column, and boats) and starts counting the lines at 1 with the placement of the first boat
       
        for line in readLines:
            # for each line in the file do below
            currentLine = openedFile.readline()
            #readline means that it reads the line on the row, column, and boat placement horizontally
            currentLine = currentLine.strip() #strip means the space between the row, column, and boat so it doesn't actually read it
            #without removing these lines, the compiler would read the spaces
            currentLine = currentLine.split()#split removes the spaces between the integars by removing the whitespace (no need for parameters, whitespace is default)
            #1  1   1 ----> ['1','1','1']

            boatRow = int(currentLine[0])
            boatColumn = int(currentLine[1])
            boatNumber = int(currentLine[2])
            # for currentLine the reason is starts at 0 is because thats the index of the first row of values
            #1 1 1 --> 0 1 2. then it continues in numerical values as you go further in the list
            boatRowColumn = [boatRow,boatColumn]
            #creates a 1x2 array of the position of each boat by taking in its row and column location
           
            if boatsPlacementMap.get(boatNumber) == None:
                #creates a list of the boat places by assigning each placement of the boat to the boatnumber
                boatsPlacementMap[boatNumber] = []
           
            boatsPlacementMap[boatNumber].append(boatRowColumn)
            #adds the placement of the boat location of the list of the boats. adds it to the end
           
        openedFile.close()

    boatPlacementList = list(boatsPlacementMap.values())
    #boatPlacementMap is used to create a list of the boats positions which each boat having its own 'key'
    #boatPlacementList is used to create a list of the boats but without the keys present.
    # print("Boat Placement Map:",boatsPlacementMap)
    # print("Boat Placement List:", boatPlacementList)
    return boatPlacementList #maybe return the map instead of the map values

def initializeBoard():
    print("====>Current Board Status<====\n")
    print("     0 1 2 3 4 5 6 7 8 9")
    print("     -------------------")
    #creating the 10x10 grid. prints the statement above

    columnNumbers = [0,1,2,3,4,5,6,7,8,9]
    #for the side numbers, displats a column from 0 to 9

    for number in columnNumbers:
        print(number, ": ",". . . . . . . . . .")
        #prints colon, followewd by ten '.'

    print("For your guess, enter the row and column positions.\n")

def ObtainMove():
    playerRow = input("Enter a row value from 0-9: ")
    #asks user to enter the row value
    playerColumn = input("Enter a column value from 0-9: ")
    #asks the user to inser their guess of the row and column

    row = int(playerRow)
    column = int(playerColumn)
    #change string to int

    if 0<=row<=9 and 0<=column<=9:
        #if the row and column is between -1 and 10, creatd a list of the players guess
        playerGuessList = [row,column]
        print("\nPlayer Guess:",playerGuessList)
       
        return playerGuessList
   
    else:
        print("Invalid Input. Try Again")
        #if the input of the row and column is incorrect, the function ObtainMove() is run again until
        #a valid input is inserted by the user
        ObtainMove()


def CheckMove(playerGuessList, boatPlacementsList):
 
    row = playerGuessList[0]
    #row index is zero
    column = playerGuessList[1]
    #column index is zero
    global numberOfHits
    #global variables are variables that are declared and initialized outside of all the functions. that way we can use them whenever we want
    global numberOfTurns

    # correctGuess = False
    # boatNumber = 1

    for boatHitList in boatPlacementsList:
        # print("boat Number:", boatNumber, "Boat Before:", boatHitList)

        if boatHitList.count(playerGuessList) !=0:
            #check if player guess is in boats hit list
            correctGuesses.append(playerGuessList)
            #when the players guess is correct it includes it into the list of correctGuesses
            numberOfHits = numberOfHits+1
            numberOfTurns=numberOfTurns+1
            #everytime the player takes a turn the count is increased by 1
            #everytime the players guess is correct  the count is increased by 1
            boatHitList.remove(playerGuessList)
            #when the players guess is correct, remove that specific coordinate from the boat list
            print("......Hit!!!\n")

            # print("boat Number:", boatNumber, "Boatlist After:", boatHitList)

            if len(boatHitList) ==0:
                #is the length of the list is equal to zero meaning there aren't any more postitions for
                #that boat, print the statement below
                print("You Sank Boat:",boatNumber)
            correctGuess = True
            break #break from for loop since a boat was hit
           
        boatNumber=boatNumber+1
    # if after the for loop has checked all boats and the boat hit flag is still false then user miss
    if correctGuess == False:
        print("......Miss!!!\n")
        numberOfTurns=numberOfTurns+1
        incorrectGuesses.append(playerGuessList)
        #if the players guess is incorrect, add it to the list of the incorrectGuesses list

    PrintBoard()  
    #prints the board with the updated grid including the H and X

def PrintBoard():
    print("Number of Hits: ", numberOfHits)
    print("Number of Turns: ", numberOfTurns)

    print("\n====>Current Board Status<====\n")
    print("    0 1 2 3 4 5 6 7 8 9")
    print("    -------------------")

    for row in range(10):
        print(row,":",end=" ")
        for column in range(10):
            if correctGuesses.count([row,column]) !=0:
                print("H",end=" ")
            #this counts the existence of the specified [row, column] in the correctGuess list.
            #if that specific coordinant is available in the list (i.e not equal to 0) print an H in place of the '.'
            elif incorrectGuesses.count([row,column]) !=0:
                print("X",end=" ")
            #here the same thing happens where the coordinate is checked if it exists within the incorrectGuess list
            #and if it does to print an X
            else:
                print(".",end=" ")
            #if the two conditions above are false, print a .

        print("")
        #allows for spaces at the end of each row

def calculatePercentage(numberofHits,numberofTurns):
    percentage = (numberOfHits/numberOfTurns) * 100
    #calculates the percentage of hits and turns
    return percentage

main()


