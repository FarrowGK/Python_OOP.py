class card(object):
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return"{} of {}".format(self.value, self.suit)
class deck(card):
    def __init__(shuffle, deal, display):
        cards = []
        suites = ["Hearts", "Spades", "Clubs", "Diamonds"]
        count = -1
        for suite in suites:
            count += 1
            for number in range(2, 15):
                if number <= 10:
                    word = suites[count]
                    push = number, "of " + word
                    cards.append(push)
                elif number == 11:
                    word = suites[count]
                    push = "J " + "of " + word
                    cards.append(push)
                elif number == 12:
                    word = suites[count]
                    push = "Q " + "of " + word
                    cards.append(push)
                elif number == 13:
                    word = suites[count]
                    push = "K " + "of " + word
                    cards.append(push)
                elif number == 14:
                    word = suites[count]
                    push = "A " + "of " + word
                    cards.append(push)
                else:
                    continue            
        print cards
    def shuffle(self):
        import random
        self.value = random.randint(0,53)
        print cards[value]
        return self
    
#   def shuffle(self):
#     import random
#         self.value = random.randint(2,15)
#         self.suit = random.randint(1,5)
#         return self
#     def deal_card(self):

#     def display_deck(self):
#         __repr__()
cards.shuffle()
    

