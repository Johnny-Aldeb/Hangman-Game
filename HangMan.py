import random

logo = ''' 
__                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo+"\n")                   
word_list = ["ardvark", "baboon", "camel"]

word_chosen = random.choice(word_list)
print("The word is:",word_chosen)

Stages = ['''
*******************
           ----
          |    |
          |    |
          0    |
         /|\   |
         /|\   |
               |
               |
          ------
          ------
*******************''',
         '''
*******************
          +----+
          |    |
          |    |
          0    |
         /|\   |
         /|    |
               |
               |
          ------
          ------
*******************''',
         '''
*******************
          +----+
          |    |
          |    |
          0    |
         /|\   |
               |
               |
               |
          ------
          ------
*******************''',
         '''
*******************
          +----+
          |    |
          |    |
          0    |
         /|    |
               |
               |
               |
          ------
          ------
*******************''',
         '''
*******************
          +----+
          |    |
          |    |
          0    |
               |
               |
               |
               |
          ------
          ------
*******************''',
          '''
*******************
          +----+
          |    |
          |    |
               |
               |
               |
               |
               |
          ------
          ------
*******************''']


display = []
for num in range(0, len(word_chosen)):  #if ardvark the chosen word
  #num goes from 0 to 7 but not
  # include 7
  display += "_"
  

end_of_game = False
lives = 6
while not end_of_game:
  guess = input("enter a letter ").lower()
  
  
  if guess in display:
     print(f"you've already guessed {guess}")
     
  for num in range(0, len(word_chosen)):
      if (word_chosen[num] == guess):
        display[num] = guess
        
        
       
       
  if guess not in word_chosen:
        print(f"you've guessed {guess}, that's is not in the word. you lose a life.")
        lives=lives- 1
        print(Stages[lives])
        
        if(lives == 0):
          print("you lose")
          end_of_game = True
          
        
  print(display)       
        
  if "_" not in display:
      print("you won")
      end_of_game = True
  
  