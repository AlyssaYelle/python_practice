#  File: Poker.py

#  Description: Create a deck of cards, shuffle and deal them to a user-specified number of players.
#  Players will show their hand and program will determine a winner and break ties if necessary

#  Student's Name: Alyssa Jones

#  Student's UT EID: adj484

#  Partner's Name: Anna Williams

#  Partner's UT EID: alw3979

#  Course Name: CS 313E 

#  Unique Number: 51340

#  Date Created: 6 February 2018

#  Date Last Modified: 10 February 2018



import random

# here is a class which enables us to create card objects
class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12
    
    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)


# here is a class which allows us to create an entire deck of cards
# we create one card for each combination of suit & rank
class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  # shuffle the cards
  def shuffle (self):
    random.shuffle (self.deck)

  # deal the cards
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

# here is a class which allows us to play a game of poker
# we need players we need to create a deck of cards
class Poker (object):
  def __init__ (self, num_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 5

    # we deal five cards to each player
    for i in range (num_players):
      hand = []
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      self.players.append (hand)

  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players)):
      sortedHand = sorted (self.players[i], reverse = True)
      self.players[i] = sortedHand

      hand = ''
      for card in sortedHand:
        hand = hand + str (card) + ' '
      print ('Player ' + str (i + 1) + " : " + hand)

    # determine each type of hand and print
    points_hand = []
    for i in range (len(self.players)):
      if self.is_royal(self.players[i]):
      	points_hand.append(10)
      	print('Player ' + str(i+1) + ': Royal Flush')
      elif self.is_straight_flush(self.players[i]):
      	points_hand.append(9)
      	print('Player ' + str(i+1) + ': Straight Flush')
      elif self.is_four_kind(self.players[i]):
      	points_hand.append(8)
      elif self.is_full_house(self.players[i]):
      	points_hand.append(7)
      	print('Player ' + str(i+1) + ': Full House')
      elif self.is_flush(self.players[i]):
      	points_hand.append(6)
      	print('Player ' + str(i+1) + ': Flush')
      elif self.is_straight(self.players[i]):
      	points_hand.append(5)
      	print('Player ' + str(i+1) + ': Straight')
      elif self.is_three_kind(self.players[i]):
      	points_hand.append(4)
      	print('Player ' + str(i+1) + ': Three of a Kind')
      elif self.is_two_pair(self.players[i]):
      	points_hand.append(3)
      	print('Player ' + str(i+1) + ': Two Pair')
      elif self.is_one_pair(self.players[i]):
      	points_hand.append(2)
      	print('Player ' + str(i+1) + ': One Pair')
      elif self.is_high_card(self.players[i]):
      	points_hand.append(1)
      	print('Player ' + str(i+1) + ': High Card')
      else:
      	points_hand.append(0)
    
    # we want to determine the highest number of standard points
    max_points = max(points_hand)
    # initialize a list of winners
    list_winners = []

    # if there is only one winner we can declare them the winner and stop
    # otherwise we will have to figure out who ties and then break the tie
    for i in range (len(points_hand)):
    	if points_hand[i] == max_points:
    		list_winners.append(i)
    if len(list_winners) == 1:
    	winner = list_winners[0] + 1
    	print('Player ' + str(winner) + ' wins!')
    else:
    	for i in range(len(list_winners)):
    		player = list_winners[i]
    		tied_winner = list_winners[i] + 1
    		print ('Player ' + str(tied_winner) + ' ties!')
    	print('Breaking tie...')
    	points_list = []
    	for i in range(len(list_winners)):
    		player_index = list_winners[i]
    		
    		points_list.append((self.compute_points(self.players[player_index],max_points)))
    	
    	winner_points = max(points_list)
    	for i in range(len(points_list)):
    		if winner_points == points_list[i]:
    			winning_tied_player = list_winners[i]+1
    			print('Player ' + str(winning_tied_player) + ' wins!')



  # this computes points to break ties (different from the initial 1-10 points)
  def compute_points(self, hand, max_points):
  	h = max_points
  	if max_points == 2:
  	  if (hand[0].rank == hand[1].rank):
  	  	c1 = hand[0].rank
  	  	c2 = hand[1].rank
  	  	c3 = hand[2].rank
  	  	c4 = hand[3].rank
  	  	c5 = hand[4].rank
  	  elif (hand[1].rank == hand[2].rank):
  	  	c1 = hand[1].rank
  	  	c2 = hand[2].rank
  	  	c3 = hand[0].rank
  	  	c4 = hand[3].rank
  	  	c5 = hand[4].rank
  	  elif (hand[2].rank == hand[3].rank):
  	  	c1 = hand[2].rank
  	  	c2 = hand[3].rank
  	  	c3 = hand[0].rank
  	  	c4 = hand[1].rank
  	  	c5 = hand[4].rank
  	  else:
  	  	c1 = hand[3].rank
  	  	c2 = hand[4].rank
  	  	c3 = hand[0].rank
  	  	c4 = hand[1].rank
  	  	c5 = hand[2].rank
  	elif max_points == 3:
  	  if (hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank):
  	  	c1 = hand[0].rank
  	  	c2 = hand[1].rank
  	  	c3 = hand[2].rank
  	  	c4 = hand[3].rank
  	  	c5 = hand[4].rank
  	  elif (hand[0].rank == hand[1].rank) and (hand[3].rank == hand[4].rank):
  	  	c1 = hand[0].rank
  	  	c2 = hand[1].rank
  	  	c3 = hand[3].rank
  	  	c4 = hand[4].rank
  	  	c5 = hand[2].rank
  	  else:
  	  	c1 = hand[1].rank
  	  	c2 = hand[2].rank
  	  	c3 = hand[3].rank
  	  	c4 = hand[4].rank
  	  	c5 = hand[5].rank
  	elif max_points == 4:
  	  if (hand[0].rank == hand[1].rank):
  	  	c1 = hand[0].rank
  	  	c2 = hand[1].rank
  	  	c3 = hand[2].rank
  	  	c4 = hand[3].rank
  	  	c5 = hand[4].rank
  	  elif (hand[1].rank == hand[3].rank):
  	  	c1 = hand[1].rank
  	  	c2 = hand[2].rank
  	  	c3 = hand[3].rank
  	  	c4 = hand[0].rank
  	  	c5 = hand[4].rank
  	  else:
  	  	c1 = hand[2].rank
  	  	c2 = hand[3].rank
  	  	c3 = hand[4].rank
  	  	c4 = hand[0].rank
  	  	c5 = hand[1].rank
  	elif max_points == 7:
  	  if (hand[0].rank == hand[2].rank):
  	  	c1 = hand[0].rank
  	  	c2 = hand[1].rank
  	  	c3 = hand[2].rank
  	  	c4 = hand[3].rank
  	  	c5 = hand[4].rank
  	  else:
  	  	c1 = hand[2].rank
  	  	c2 = hand[3].rank
  	  	c3 = hand[4].rank
  	  	c4 = hand[0].rank
  	  	c5 = hand[1].rank
  	elif max_points == 8:
  	  if (hand[0] == hand[1]):
  	  	c1 = hand[0].rank
  	  	c2 = hand[1].rank
  	  	c3 = hand[2].rank
  	  	c4 = hand[3].rank
  	  	c5 = hand[4].rank
  	  else:
  	  	c1 = hand[1].rank
  	  	c2 = hand[2].rank
  	  	c3 = hand[3].rank
  	  	c4 = hand[4].rank
  	  	c5 = hand[0].rank
  	else:
  	  c1 = hand[0].rank
  	  c2 = hand[1].rank
  	  c3 = hand[2].rank
  	  c4 = hand[3].rank
  	  c5 = hand[4].rank
  	total_points = h*13**5 + c1*13**4 + c2*13**3 + c3*13**2 + c4*13 + c5
  	return (total_points)




      



  # determine if a hand is a royal flush
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return False

    rank_order = True
    for i in range (len(hand) - 1):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return False
    
    return True

  # determine if a hand is a straight flush
  def is_straight_flush (self, hand):
    
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i+1].suit)

    if (not same_suit):
      return False

    rank_order = True
    for i in range(len(hand) - 1):
    	rank_order = rank_order and (hand[i].rank == hand[i+1].rank + 1)

    if (not rank_order):
    	return False

    return True



  # determine if a hand is four of a kind 
  def is_four_kind (self, hand):
  	i = 0
  	if (hand[i].rank == hand[i+1].rank) and (hand[i+1].rank == hand[i+2].rank) and (hand[i+2].rank == hand[i+3].rank):
  	  return True
  	elif (hand[i+1].rank == hand[i+2].rank) and (hand[i+2].rank == hand[i+3].rank) and (hand[i+3].rank == hand[i+4].rank):
  	  return True
  	else:
  	  return False

  # determine if a hand is a full house
  def is_full_house(self, hand):
  	i = 0
  	if (hand[i].rank == hand[i+1].rank) and (hand[i+1].rank == hand[i+2].rank) and (hand[i+3].rank == hand[i+4].rank):
  	  return True
  	elif (hand[i+2].rank == hand[i+3].rank) and (hand[i+3].rank == hand[i+4].rank) and (hand[i].rank == hand[i+1].rank):
  	  return True
  	else:
  	  return False
  
  # determine if a hand is a flush
  def is_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
    	same_suit = same_suit and (hand[i].suit == hand[i+1].suit)

    if (not same_suit):
    	return False

  # determine if a hand is straight
  def is_straight (self, hand):
    rank_order = True
    for i in range(len(hand) - 1):
    	rank_order = rank_order and (hand[i].rank == hand[i+1].rank + 1)

    if (not rank_order):
    	return False

    return True

  # determine if a hand is three of a kind
  def is_three_kind (self, hand):
    i = 0
    if (hand[i].rank == hand[i+1].rank) and (hand[i+1].rank == hand[i+2].rank):
    	return True
    elif(hand[i+1].rank == hand[i+2].rank) and (hand[i+2].rank == hand[i+3].rank):
    	return True
    elif (hand[i+2].rank == hand[i+3].rank) and (hand[i+3].rank == hand[i+4].rank):
    	return True
    else:
    	return False

  # determine if a hand is two pairs
  def is_two_pair (self, hand):
    i = 0
    if (hand[i].rank == hand[i+1].rank) and (hand[i+2].rank == hand[i+3].rank):
    	return True
    elif(hand[i+1].rank == hand[i+2].rank) and (hand[i+4].rank == hand[i+3].rank):
    	return True
    elif (hand[i].rank == hand[i+1].rank) and (hand[i+3].rank == hand[i+4].rank):
    	return True
    else:
    	return False

  
  # determine if a hand is one pair
  def is_one_pair (self, hand):
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        return True
    return False

  # if a hand is not any of the above it must be high card so we can just return true
  def is_high_card (self, hand):
    return True


  

def main():
  # prompt user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))

  # create the Poker object
  game = Poker (num_players)

  # play the game (poker)
  game.play()

main()
















