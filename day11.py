import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def blackjack_game():

  def start_deal(cards):
      shuffled = random.choice(cards)
      return shuffled

  def done_playing():
    player_sum = sum(player_cards)
    cpu_sum = sum(cpu_cards)
    print(f"Your hand is: {player_cards}, a total of {player_sum}.")
    print(f"The computer's hand is {cpu_cards}, a total of {cpu_sum}.")
    if sum(cpu_cards) > 21:
      print("The computer got a bust, you win!")
    elif sum(player_cards) != 21 and sum(cpu_cards) == 21:
      print("You lose.")
    elif sum(player_cards) == 21 and sum(cpu_cards) != 21:
      print("You lose!")
    elif sum(player_cards) == 21 and sum(cpu_cards) != 21:
      print("You win!")
    elif sum(player_cards) > 21:
      print("It's a bust, you lose.")
    elif player_sum == cpu_sum:
      print("It's a draw.")
    elif player_sum > cpu_sum:
      print("You win!")
    else:
      print("You lose.")
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again == 'y':
      clear()
      blackjack_game()
    else:
      if play_again == 'n':
        print("Goodbye.")

  def keep_playing():
    shuffled = start_deal(cards)
    player_cards.append(shuffled)
    cpu_cards.append(start_deal(cards))
    player_sum = sum(player_cards)
    cpu_sum = sum(cpu_cards)
    if 11 in player_cards and player_sum >= 21:
      ace = player_cards.index(11)
      player_cards[ace] = 1
      player_sum = sum(player_cards)
    if 11 in cpu_cards and cpu_sum >= 21:
      ace = cpu_cards.index(11)
      cpu_cards[ace] = 1
      cpu_sum = sum(cpu_cards)
    print(f"Your hand is: {player_cards}, a total of {player_sum}.")
    print(f"The computer's hand is {cpu_cards}, a total of {cpu_sum}.")
    if player_sum > 21:
      print("It's a bust, you lose.")
      play_again = input("Do you want to play again? Type 'y' or 'n': ")
      if play_again == 'y':
        clear()
        blackjack_game()
      elif play_again == 'n':
        print("Thanks for playing. Goodbye.")
    if player_sum <= 21:
      hit = input("Type 'y' to get another card, type 'n' to pass: ")
      if hit == 'y':
        keep_playing()
      elif hit == 'n':
        done_playing()
  
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player_cards = []
  cpu_cards = []
  player_cards.append(start_deal(cards))
  cpu_cards.append(start_deal(cards))
  print(f"Your cards: {player_cards}")
  print(f"The computer's first card: {cpu_cards}")
  hit = input("Type 'y' to get another card, type 'n' to pass: ")
  if hit == 'n':
    done_playing()
  elif hit == 'y':
    keep_playing()

blackjack_game()
