import random

theWords=['boy','girl','beautiful', 'loyalty', 'Royal', 'Rolls Royce', 'Aston Martin', 'supercar', 'hypercar']
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

