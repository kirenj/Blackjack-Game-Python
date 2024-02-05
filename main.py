import random
from art import logo
from replit import clear


def card_pick():  
  card_drawn = int(random.choice(cards))
  return card_drawn

def win_check(n):
  if n == current_score_user:
    if current_score_user == 21:
      return True
    else:
      return False
  elif n == current_score_pc: 
    if current_score_pc == 21:
      return True
    else:
      return False
  else:
    return False

def score_count(n):
  if n == 'user':
    score_user = sum(your_cards)
    return score_user
  elif n == 'pc':
    score_pc = sum(pc_cards)
    return score_pc

def ace_check(cards, score): #cards = your_cards, score = current_score_user
  if 11 in cards:
    if score > 21:
      index = cards.index(11)
      cards[index] = 1
    else:
      index = cards.index(11)
      cards[index] = 11
      
def picking_cards(deck, turns): #deck = your_cards or pc_cards
  for j in range(0, turns):  
    picked_cards = card_pick()
    deck.append(picked_cards)

def winner_check():
  if current_score_user is not None and current_score_pc is not None:
    if current_score_user == current_score_pc:
      return "It's a tie"
    if current_score_user > 21:
      return "You went over. Computer Wins!"
    elif current_score_pc > 21:
      return "The computer went over. You win!"
    if current_score_user == 21:
      return "You win!"
      continue_game = False
    elif current_score_pc == 21:
      return "You lose. Computer wins!"    
    if current_score_user > current_score_pc:
      return "You win!"
    elif current_score_pc > current_score_user:
        return "You lose. Computer wins!"
  else:
    return "One or both of the scores is missing."


def final_score():
  current_score_user = score_count(n = 'user')
  current_score_pc = score_count(n = 'pc')
  print(f"Your final hand: {your_cards}, final score: {current_score_user}")
  print(f"Computer's final hand: {pc_cards}, final score: {current_score_pc}")
  print(winner_check())
  #continue_game = False

#create deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

to_play = True

while to_play == True:
  play = input("Do you wan't to play a game of Blackjack? Type 'y' or 'n': ").lower()
  clear()
  if play == 'y':
    #you take the first card and put it into a list
    print(logo)
    your_cards = []
    pc_cards = []
    current_score_user = 0
    current_score_pc = 0
    to_play = True
    
    picking_cards(deck=your_cards, turns=2)    
    #print(your_cards)
      
    #computer takes two card and puts it into a list. But only one card is displayed
    picking_cards(deck=pc_cards, turns=2)    
    #print(pc_cards)
    
    current_score_user = 0
    current_score_pc = 0
    
    current_score_user = score_count(n = 'user')
    current_score_pc = score_count(n = 'pc')
    
    current_status_user = win_check(current_score_user)
    continue_game = True
    #check the card count and if less than 21, ask user if they want to pick again
    if current_status_user == True:
      print("You got 21, you win")
      continue_game = False
    elif current_status_user == False:
      ace_check(cards = your_cards and pc_cards, score = current_score_user and current_score_pc)
      
      print(f"Your cards: {your_cards}, current score: {current_score_user}")
      print(f"Computer's first card: {pc_cards[0]}")
      
      while continue_game == True:
        pick_again = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if pick_again == 'y':
          picking_cards(deck=your_cards, turns=1)
          # picking_cards(deck=pc_cards, turns=1)
          
          current_score_user += your_cards[len(your_cards) - 1]
          current_score_pc += pc_cards[len(pc_cards) - 1]
          print(f"Your cards: {your_cards}, current score: {current_score_user}")
          print(f"Computer's first card: {pc_cards[0]}")
          # print(winner_check())
          if current_score_user is not None and current_score_user >= 21:
            final_score()
            continue_game = False
          else:
            continue_game = True
        
        elif pick_again == 'n':
          continue_game = False
          
          while current_score_pc is not None and current_score_pc < 17:
            if current_score_pc < 17:
              picking_cards(deck=pc_cards, turns=1)
              current_score_pc += pc_cards[len(pc_cards) - 1]
            else:
              final_score()    
          final_score()
          
        continue_game = False
  
  else:
    to_play = False
      