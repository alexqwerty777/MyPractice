import random



class Card():
	'''
	Номинал: 2,3,4,5,6,7,8,9,10,J,Q,K,A
	Масть: (S)Spades, (C)Clubs, (D)Diamonds, (H)Hearts	
	'''
	def __init__(self, fvalue, suit):
		self.fvalue = fvalue
		self.suit = suit

	def GetValue(self):
		if self.fvalue.isdigit():
			return(int(self.fvalue))
		elif self.fvalue == 'A':
			return(11)
		else:
			return(10)

	def __repr__(self):
		return('%s (%s)' % (self.fvalue, self.suit))


class Deck():
	def  __init__(self):
		self.cards = []
		for fvalue in '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(','):
			for suit in 'SCDH':
				self.cards.append(Card(fvalue,suit))

	def shuffle(self):
		random.shuffle(self.cards)

	def GiveCard(self):
		return(self.cards.pop() if self.cards else None)

	def __repr__(self):
		return(str(self.cards))


class Player():
	def __init__(self,name):
		self.name = name
		self.cards = []

	def __repr__(self):
		return('Name: %s, CardNumber: %d \nCards:%s'	% (self.name, len(self.cards), str(self.cards)))

	def TakeCard(self,card):
		self.cards.append(card)

	def ClearHand(self):
		self.cards = []

	def CountOfA(self):
		#numbers of 'A' in hand. Can be 
		return([card.fvalue for card in self.cards].count('A'))

	def CountValue(self):
		summ = sum([card.GetValue() for card in self.cards])
		#если перебор, туз считается за 1
		A_num = self.CountOfA()
		while summ > 21 and A_num:
			summ -= 10
			A_num -= 1
		return(summ)


class Game():
	def __init__(self):
		self.Deck = Deck()
		self.Players = []

	def AddPlayer(self, name):
		self.Players.append(Player(name))

	def StartRound(self):
		self.Deck = Deck()
		self.Deck.shuffle()
		for player in self.Players:
			player.ClearHand()		
			player.TakeCard(self.Deck.GiveCard())
			player.TakeCard(self.Deck.GiveCard())
			print(player.name)


	def AddCards(self):
		for player in self.Players:
			#input('Player %s move' % player.name)
			print('>>Player %s move' % player.name)
			print(player)
			while player.CountValue() < 21:				
				#answer = input('Do you want one more card? [y/n]')

				#testing
				print('>>Your points: %d' % player.CountValue())
				print('>>Do you want one more card? [y/n]')

				if player.CountValue() < 18:
					print('>>y')
					answer = 'y'
				else:
					print('>>n')
					answer = 'n'


				if answer == 'y':
					#give one card
					if self.Deck.cards:
						player.TakeCard(self.Deck.GiveCard())
					else:
						print('>>Card in deck end')
						break
					print(player)
				elif answer == 'n':
					break
				else:
					print('>>Dont undertand you answer. Please write "y" or "n"')
			print('>>Your points: %d, ending turn.' % player.CountValue())


	def EndRound(self):		
		win_points = sorted([player.CountValue()-21 for player in self.Players])[0]
		winners = [player for player in self.Players if player.CountValue() == win_points+21] 
		if len(winners) == 1:
			print('>>Player %s win the game with %d point' % (winners[0].name, win_points+21))
		else:
			print('>>Players: ' + ' & '.join([win.name for win in winners]) + ' win the game with %d points' % (win_points+21))
		for player in self.Players:
			player.ClearHand()


def main():
	New_Game = Game()
	New_Game.AddPlayer('Alex')
	New_Game.AddPlayer('John')
	New_Game.AddPlayer('Bob')
	New_Game.StartRound()
	New_Game.AddCards()
	New_Game.EndRound()


if __name__ == '__main__':
	main()
