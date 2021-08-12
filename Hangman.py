# Simple hangman game using Python --- Jayen Lare

# Import getpass function from getpass module
from getpass import getpass

# Function that returns the current hangman board
def hangmanStages(attempts):
  display = [''' 
  -------
  |     |
  |     O
  |    /|\\
  |    / \\
  |
----- ''',''' 
  -------
  |     |
  |     O
  |    /|\\
  |    / 
  |
----- ''',''' 
  -------
  |     |
  |     O
  |    /|\\
  |    
  |
----- ''',''' 
  -------
  |     |
  |     O
  |    /|
  |    
  |
----- ''',''' 
  -------
  |     |
  |     O
  |     |
  |    
  |
----- ''',''' 
  -------
  |     |
  |     O
  |    
  |    
  |
----- ''',''' 
  -------
  |     |
  |     
  |    
  |    
  |
----- ''']
  return display[attempts];

# Function to display the hangman board and guesses
def display(attempts, blanks):
  print(hangmanStages(attempts))
  for i in range (0,len(blanks),1):
    print(blanks[i], end=" ")
  print("\n")

# Function to play hangman with user chosen word
def playGame(word):
  attempts = 6
  blanks = '_' * len(word)
  alreadyGuessed = []
  wordGuessed = False
  display(attempts,blanks)
  # Loops until player 2 is out of attempts or word is guessed
  while wordGuessed == False and attempts != 0:
    guess = input("Player 2, guess a letter or the word: ").upper()
    # Make sure guess consists of only letters
    if guess.isalpha() == True:
      # Ends game if player 2 correctly guesses the word
      if guess == word:
          print("Congrats, you guessed the word correctly!")
          wordGuessed = True
      # Checks if word or letter has already been guessed
      elif guess in alreadyGuessed:
        print("You already guessed " + guess)
        display(attempts,blanks)
      # Checks if guess is a letter
      elif len(guess) == 1:
        # Checks if letter guessed is in the word
        if guess in word:
          print("Good guess, " + guess + " is in the word!")
          alreadyGuessed.append(guess)
          # Replaces blank with correctly guessed letter
          listOfBlanks = list(blanks)
          indices = [i for i, letter in enumerate(word) if letter == guess]
          for index in indices:
              listOfBlanks[index] = guess
          blanks = "".join(listOfBlanks)
          display(attempts,blanks)
          # Word has been guessed
          if "_" not in blanks:
              print("Congrats, you guessed the word correctly!")
              wordGuessed = True
        # The letter guessed was not in the word
        else:
          print(guess + " is not in the word.")
          attempts -= 1
          alreadyGuessed.append(guess)
          display(attempts,blanks)
      # If word player 2 guessed is not the correct word, attempts left decreases by 1 
      else:
        print(guess + " is not the correct word.")
        attempts -= 1
        alreadyGuessed.append(guess)
        display(attempts,blanks)
    # Guess contains non-letter characters 
    else:
      print("Invalid guess...")
      display(attempts,blanks)
  # Player 2 ran out of attempts and did not guess the word 
  if wordGuessed == False:
    print("You've run out of attempts...")
    print("The correct word was " + word)

# Main function
def main():
  flag = True
  print("Welcome to Hangman!")
  print("Player 1 enter a word for player 2 to guess...")
  # Loops until player 1 enters a valid word
  while flag == True:
    # Hides word from player 2 using imported getpass function
    word = getpass("Your word will be hidden: ")
    if word.isalpha() == False :
        print("Sorry, invalid word.")
        print("Please enter a different word...")
    else:
      flag = False
      # Changes word to uppercase and calls playGame function
      word = word.upper()
      playGame(word)
  # Loops game, allowing users to play again
  while input("Would you like to play again? (Y/N) ").upper() == 'Y':
    flag = True
    print("Player 1 enter a word for player 2 to guess...")
    while flag == True:
      word = getpass("Your word will be hidden: ")
      if word.isalpha() == False :
          print("Sorry, invalid word.")
          print("Please enter a different word...")
      else:
        flag = False
        word = word.upper()
        playGame(word)
  print("Thanks for playing!")

# Runs main function
if __name__ == "__main__":
  main()

