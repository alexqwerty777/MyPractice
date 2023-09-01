import random



class Card:
    '''
    Номинал: 2,3,4,5,6,7,8,9,10,J,Q,K,A
    Масть: (S)Spades, (C)Clubs, (D)Diamonds, (H)Hearts  
    '''
    def __init__(self, fvalue, suit):
        self.fvalue = fvalue
        self.suit = suit

    def get_value(self):
        if self.fvalue.isdigit():
            return(int(self.fvalue))
        elif self.fvalue == 'A':
            return(11)
        else:
            return(10)

    def __repr__(self):
        return('%s (%s)' % (self.fvalue, self.suit))


class Deck:
    def  __init__(self):
        self.cards = []
        for fvalue in '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(','):
            for suit in 'SCDH':
                self.cards.append(Card(fvalue,suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def give_card(self):
        return(self.cards.pop() if self.cards else None)

    def __repr__(self):
        return(str(self.cards))


class Player:
    def __init__(self,name):
        self.name = name
        self.cards = []

    def __repr__(self):
        return('Name: %s, CardNumber: %d \nCards:%s'    % (self.name, len(self.cards), str(self.cards)))

    def take_card(self,card):
        self.cards.append(card)

    def clear_hand(self):
        self.cards = []

    def count_of_a(self):
        #numbers of 'A' in hand. Could be 11 or 1 points
        return([card.fvalue for card in self.cards].count('A'))

    def count_value(self):
        summ = sum([card.get_value() for card in self.cards])
        #if more then 21 point, count A as 1 point
        A_num = self.count_of_a()
        while summ > 21 and A_num:
            summ -= 10
            A_num -= 1
        return(summ)


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []

    def add_player(self, name):
        self.players.append(Player(name))

    def start_round(self):
        self.deck = Deck()
        self.deck.shuffle()
        for player in self.players:
            player.clear_hand()     
            player.take_card(self.deck.give_card())
            player.take_card(self.deck.give_card())
            print(player.name)


    def add_cards(self):
        for player in self.players:
            #input('Player %s move' % player.name)
            print('>>Player %s move' % player.name)
            print(player)
            while player.count_value() < 21:                
                #answer = input('Do you want one more card? [y/n]')

                #testing
                print('>>Your points: %d' % player.count_value())
                print('>>Do you want one more card? [y/n]')

                if player.count_value() < 18:
                    print('>>y')
                    answer = 'y'
                else:
                    print('>>n')
                    answer = 'n'


                if answer == 'y':
                    #give one card
                    if self.deck.cards:
                        player.take_card(self.deck.give_card())
                    else:
                        print('>>Card in deck end')
                        break
                    print(player)
                elif answer == 'n':
                    break
                else:
                    print('>>Dont undertand you answer. Please write "y" or "n"')
            print('>>Your points: %d, ending turn.' % player.count_value())


    def end_round(self):        
        win_points = sorted([player.count_value()-21 for player in self.players])[0]
        winners = [player for player in self.players if player.count_value() == win_points+21] 
        if len(winners) == 1:
            print('>>Player %s win the game with %d point' % (winners[0].name, win_points+21))
        else:
            print('>>Players: ' + ' & '.join([win.name for win in winners]) + ' win the game with %d points' % (win_points+21))
        for player in self.players:
            player.clear_hand()


def main():
    new_game = Game()
    new_game.add_player('Alex')
    new_game.add_player('John')
    new_game.add_player('Bob')
    new_game.start_round()
    new_game.add_cards()
    new_game.end_round()


if __name__ == '__main__':
    main()
