import random
import os
theWords=[]
print("1.Easy 2.Medium 3.Difficult")
difficulty = input("Enter 1, 2 or 3 to choose your difficulty.")
file = open("englishWords.txt", "r")
for line in file: # for a line in the file, copy the contents into a variable called line and then do something. Repeat the process for the next line until there's no more line
    line = line.rstrip() #!!! it reads and strips of  any spaces to the right of the value that is stored in the variable line
                        #when the spaces have been stripped from the value, copy the new value into line
                        #cuz in the file each line has only one word so the new value will have one word only. line=word

    if difficulty == '1' and len(line) >= 10: #we set the length condition as this
        theWords.append(line)#we append the processed lines to the list of our words called "theWords".
    elif difficulty == '2' and 6<=len(line)<=9:
        theWords.append(line)
    elif difficulty == '3' and len(line)<=5:
        theWords.append(line)
word = random.choice(theWords)
count = 0
win = False
guesses = ""
answer = ("_"*len(word))
while(count<10 and win is False):
    count = count +1
    guess = input('Enter guess ' + str(count) + ":")
    guesses = guesses+guess #showing you what you've typed
    tmp = ""
    i = 0
    while i<len(word):
        if(word[i]==guess):
            tmp = tmp + guess #it stores all the guesses that you've input to tmp, not just the current balue
        else:
            tmp = tmp + answer[i] #then answer still remains as '_'
        i = i+1 #this while loop continues until i=len(word), then it goes to the next if
    if (answer != tmp):
        print("good guess")
        count = count-1
        answer = tmp #so if word[i]==guess, tmp = tmp + guess, and here answer is replaced by some of the temp values
    else:
        print("Not a good guess")

    if (answer == word):
        print("Well done you win!")
        win = True
    print(str(10-count)+"/10 guesses left")
    print("your guesses: " + guesses)
    print("The word so far: " + answer)
