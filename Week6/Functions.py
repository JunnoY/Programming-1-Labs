import random
#get words
# def GetWordsFromUser():
#     theWords =[]
#     while True:
#         word = input("Enter a word and press <enter>(or just press <enter> to finish) :")
#         if word != "":
#             theWords.append(word)
#         else:
#             return theWords

#creating an empty grid, we can use the normal way of creating a list such as:
#grid=[
        #['','a','b']
#] but we do something else
rowMax = int(input("Enter number of rows: "))
colMax = int(input("Enter number of columns: "))
placeWords = []
def GenerateGrid():
    grid=[['-' for x in range(colMax)] for y in range(rowMax)]
    return grid
grid = GenerateGrid()

def DisplayGrid():
    for row in range (rowMax):
        for col in range(colMax):
            print(grid[row][col]+'', end='') #end'' prevents a new line occurring
        print()#we want a new line after each row



#create a wordlist
def GetWords():
   theWords = ["happy","cheerful","chipper","effervescent","jaunty","jolly"]
   return theWords
GetWords()
words = GetWords()

#display words
def DisplayWords(words=words): #??? to skip words that cannot be placed; the default value of the words list of used if no other list is passed
    for word in words:
        print(word)

def PlaceWord(word, row, col, direction):
    for charOfWord in range(len(word)):
        grid[row][col]=word[charOfWord] #place each character in grid
        if direction == 0: col += 1  #to get the next square for the next character
        if direction == 1: col -= 1
        if direction == 2: row += 1
        if direction == 3: row -= 1
    placeWords.append(word) #at the end the accepted words is appended in the empty list

def CheckWordWillFit(word, row, col, direction):
    for charOfWord in range(len(word)):
        if grid[row][col] == '-' or grid[row][col]==word[charOfWord]: #if the square in the grid for the row and column is equal to a space(indicated by -)
    #or if the square in the gird is  equal to the current character in charofword the placement is valid. Move to the next square and perform the check again for the next character of the word
            if direction == 0: col += 1  # to get the next square for the next character
            if direction == 1: col -= 1
            if direction == 2: row += 1
            if direction == 3: row -= 1
        else:
            print("Word will not fit")
            return False
    return True #after checking, return True

#place words in grids;
def PlaceWords():
    for word in words: #determine direction for each word
        if len(word)>rowMax or len(word)>colMax:
            continue #it will skip the word with its length greater than col/rowMax
        count = 0
        foundValidLocation = False
        while not foundValidLocation and count < 10:  # this while loop could loop forever if there are no valid locations to place a word
            foundValidLocation = True
            count += 1
            direction = random.randint(0,3) #determine the direction the word will be placed
            if direction == 0:
                print("placing", word, "from left to right")
                min=0
                max=colMax-len(word)
            elif direction == 1:
                print("placing", word, "from right to left")
                min = len(word) - 1
                max = colMax -1  #because colMax is n, and starts from 0, so the last col is colMax-1
            elif direction == 2:
                print("placing", word, "from top to bottom")
                min=0
                max=rowMax-len(word)
            elif direction == 3:
                print("placing", word, "from bottom to top")
                min = len(word)-1
                max = rowMax-1
            print("Word length is", len(word), "so:")
            print("min:",min," max:",max) #min means the start position of the word should be at least row/col min
                                         #max means the start postion of the word should be at most row/col max
            square = random.randint(min,max) #randomly choose which square to start the word
            print("Square chosen is",square)
            if direction<2: #in the conditon of left to right or right to left
                row = random.randint(0,rowMax-1)
                col = square
                print("in row",row)
            else: #in the condition of bottom to top or top to bottom
                row = square
                col = random.randint(0,colMax-1)
                print("in column",col)
            foundValidLocation = CheckWordWillFit(word,row,col,direction)
            if foundValidLocation: #place the word after checking
                PlaceWord(word, row, col, direction)
PlaceWords()

def GridRandomFill():
    alphabet = "abcccdefghhijjjklllmnopqqqrstttuvwxyz"
    for row in range(rowMax):
        for col in range(colMax):
            if grid[row][col] =='-':
                letterFromAlphabet = random.randint(0, len(alphabet)-1) #because start from 0th
                grid[row][col] = alphabet[letterFromAlphabet]

GridRandomFill()
DisplayGrid()
DisplayWords(placeWords)



