# module imports
import random

# global variables
_quit = ['quit', 'QUIT', 'q']
restart = ['yes', 'YES', 'y']

# item pick
class Pick(object):
    rock = ['rock', 'ROCK', 'r', '1']
    paper = ['paper', 'PAPER', 'p', '2']
    scissors = ['scissor', 'SCISSOR', 's', '3']
    botChoice = ['Rock', 'Paper', 'Scissor']

    def __init__(self, score, player='Human'):
        self.player = player
        if player.strip().lower() == 'human':
            while True:
                self.choice = str(input('Rock, Paper, Scissor => ')).lower()
                if self.choice.strip() in Pick.rock: 
                    self.choice = 'Rock'
                    break
                elif self.choice.strip() in Pick.paper:
                    self.choice = 'Paper'
                    break
                elif self.choice.strip() in Pick.scissors:
                    self.choice = 'Scissor'
                    break
                elif self.choice.strip() in _quit:
                    score.winner()
                    exit()
                else:
                    print('\n')
                    print('Invalid Response')
                    print('\n')
        else:
            self.choice = Pick.botChoice[(random.randint(0, 2))]

    def __str__(self):
        return str(self.choice)

# game engine
class Game(object):
    def __init__(self, players):
        self.players = players
        self.p1 = None
        self.p2 = None
        self.score = Scoreboard()

    def draw(self):
        self.p1 = Pick(score=self.score)
        if (self.players == '1'):
            self.p2 = Pick(player='BOT', score=self.score)
            print('\n')
            print('BOT Choose => ' + str(self.p2))
        else:
            self.p2 = Pick(score = self.score)
        return self

    def compare(self):         
        if (self.p1.choice == self.p2.choice):
            print('\n')
            print('Match Tie')
        elif (self.p1.choice == 'Rock' and self.p2.choice == 'Scissor' or self.p1.choice == 'Paper' and self.p2.choice == 'Rock' or self.p1.choice == 'Scissor' and self.p2.choice == 'Paper'):
            self.score.updatescore(s1=1, s2=0)
            print('\n')
            print('Player 1 Win')
        else:
            self.score.updatescore(s1=0, s2=1)
            if (self.players == '1'):
                print('\n')
                print('BOT Win')
            else:
                print('\n')
                print('Player 2 Win')
        print('\n')
        return self

# score board
class Scoreboard(object):
    def __init__(self):
        self.s1 = 0
        self.s2 = 0

    def updatescore(self, s1, s2):
        if (s1 > s2):
            self.s1 += 1
        else:
            self.s2 += 1

    def clear(self):
        self.s1 = 0
        self.s2 = 0

    def winner(self):
        if (self.s1 > self.s2):
            print('\n')
            print('Player 1 Win Game')
        if (self.s1 < self.s2):
            print('\n')
            print('Player 2 Win Game')
        if (self.s1 == self.s2):
            print('\n')
            print("Tie Game")

    def iscomplete(self):
        if (self.s1 == 5 or self.s2 == 5):
            return True
        else:
            return False

    def gamestatus(self):
        print('Player 1: ' + str(self.s1) + '/5')
        print('Player 2: ' + str(self.s2) + '/5')
        print('\n')

# start function 
def start():
    print('\n')
    numOfplayer = input('Number Of Players? (1/2) => ')
    print('\n')

    if (numOfplayer.strip() in ['1', '2']):
        game = Game(players=numOfplayer.strip())
        while (True):
            game.draw().compare()
            game.score.gamestatus()
            if (game.score.iscomplete()):
                game.score.winner()
                break
        print('\n')

        rematch = input('Restart? (Y/N) => ')
        
        if (rematch in restart):
            start()
        else:
            print('\n')
            print('Thank You For Playing')
            exit()
    elif (numOfplayer.strip() in _quit):
        print('Thank You For Playing')
        exit()
    else:
        print('Invalid Response')
        print('\n')
        start()


# check entry
if (__name__ == '__main__'):
    start()