import string
import random

HANGMAN_STAGES = [
    ''
    '''
    +---+
    |   |
        |
        |
        |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
        |
    ========='''
]
# the list of random blockbuster movies"""""""
input(f'This is a game called Movie Hangman. You will be playing a variation of hangman, where the word is a movie.  enter to begin')
movies = [
  "The Shawshank Redemption", "The Godfather", "The Dark Knight",
  "The Lord of the Rings The Return of the King", "Pulp Fiction",
  "Forrest Gump", "Star Wars Episode IV A New Hope", "The Matrix",
  "The Silence of the Lambs", "Jurassic Park", "The Lion King",
  "The Terminator", "Jaws", "Rocky", "Back to the Future",
  "Indiana Jones and the Raiders of the Lost Ark", "Titanic", "The Exorcist",
  "Alien", "The Shining", "Blade Runner", "ET the ExtraTerrestrial",
  "Fight Club", "Goodfellas", "The Green Mile", "The Princess Bride",
  "Schindlers List", "The Wizard of Oz", "Gone with the Wind", "Casablanca",
  "One Flew Over the Cuckoos Nest", "Apocalypse Now", "The Godfather Part II",
  "The Deer Hunter", "Platoon", "Full Metal Jacket", "Saving Private Ryan",
  "Gladiator", "The Departed", "No Country for Old Men", "There Will Be Blood",
  "The Social Network", "The Grand Budapest Hotel", "La La Land",
  "The Shape of Water", "The Joker", "Avengers Endgame", "The Lion King",
  "Joker", "Bohemian Rhapsody", "Black Panther", "The Irishman",
  "Once Upon a Time in Hollywood", "Parasite"
]


def get_word():
  bob = random.choice(movies)
  return bob.lower()


def formatword(a):
  bob = ''
  for b in a:
    if b in string.ascii():
      bob += '_'
    else:
      bob += '  '


#creates the format for telling use
def format(word, use_letters, alphabet, score):
  #I need to make something that basically replaces all letters with an underscore, but the instances of the letters the user has used.
  new_word = ''
  for subset in word:
    if subset == ' ':
      new_word += subset
    elif subset in use_letters:
      new_word += subset
    else:
      new_word += '_'
    bob_w = ' , '.join(use_letters)
    bob_l = ' , '.join(alphabet - use_letters)
    bob_s = 5 - score
  print(
    
    f'{HANGMAN_STAGES[score]}\nYou have used these letters {bob_w}\n You still have letters {bob_l} \n Movie: {new_word}\n You have {bob_s} tries left \n \n \n'
  )

def format2(word, use_letters):
  new_word = ''
  for subset in word:
    if subset == ' ':
      new_word += subset
    elif subset in use_letters:
      new_word += subset
    else:
      new_word += '_'
  print(f'{HANGMAN_STAGES[0]}\nYour Movie is {new_word}')


  
  def balls(word):
    fstr = (word.replace(' ', '')).lower
    return fstr


    
def hangman():
  the_word = (get_word())
  alphabet = set(string.ascii_lowercase)
  used_letters = set()
  thy = set(the_word.replace(' ', ''))
  format2(the_word, used_letters)
  score = 0
  
  while len(thy) != 0:
    if score == 5:
      guess = input("Ugh, FINE. You get 1 final guess to get the right word or you lose!!! Enter your movie guess: ")
      guess = guess.replace(' ', '').lower()
      score += 1
      if guess == the_word.replace(' ', '').lower():
        score -= 3
        break
      else:
        break
    new_letter = input("Enter a letter or enter 'gu' to guess: ").lower()
    if new_letter == 'gu':
      score += 1
      guess = input("enter your movie guess: ")
      guess = guess.replace(' ', '').lower()
      
      if guess == the_word.replace(' ', '').lower():
        break
      else:
        print("The guess is wrong")
        format(the_word, used_letters, alphabet, score)
    if len(new_letter) > 1:
      print("Enter 1 letter please")
    if not new_letter.isalpha():
      print("please type a letter")
    if new_letter in used_letters:
      print("You have already used this letter before")
    elif new_letter in alphabet - used_letters:
      used_letters.add(new_letter)
      if new_letter in thy:
        thy.discard(new_letter)
        format(the_word, used_letters, alphabet, score)
      else:
        print("Sowwy, your letter is not in the word:")
        score += 1 
        format(the_word, used_letters, alphabet, score)
        
  if score > 5:
    print(f" LLLL. You Lose. The movie was <<{the_word}>>\n {HANGMAN_STAGES[5]}")
  else:
    print(f"  CONGRATS YOU WON. The movie was <<{the_word}>>\n{HANGMAN_STAGES[score - 1]} ")        


hangman()