import random
from hangman_word import word_list
from hangman_logo import Hangman_stages,logo
lives=len(Hangman_stages)-1
end_of_hangman=False
print(logo)




data=random.choice(word_list)

def split(word):
    return list(word)
data=split(data)

#BLANK _ DISPLAYED HERE
display=[]
blank="_"
for letter in data:
  display.append(blank)



# repeat until lives go down
while not end_of_hangman:

    guess=input('Guess a letter:\n')
    guess=guess.lower()

    if guess in display:
        print(f'You have already guessed {guess}, Guess again')




    #check guessed letter in data
    for position in range(len(data)):
        letter=data[position]

        if letter == guess:
        # print('correct')
           display[position]=letter
    
    
    if guess not in data:

        print(f'You guessed {guess}, which is not present in the word.You lost a life')
        lives-=1
        if lives==0:
            print('Game over! You lose!')
            quit()

    print(f"{' '.join(display)}")        
    if blank not in display:
        end_of_hangman=True
        print('You win')

    


    
    
    print(Hangman_stages[lives])      