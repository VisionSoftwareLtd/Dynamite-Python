from bot import Bot
import random
import constants


class RajBot(Bot):
    def __init__(self):
        self.d_left = constants.NUM_DYNAMITE
        self.memory = 5
        self.chaos = 10
        self.opp_d = 0
        self.round = 0
        self.name = "RajBot"

    def make_move(self, gamestate):

        output = self.choose_move(gamestate['rounds'])

        output = self.check_dynamite(output)

        output = self.check_water(output)

        output = self.check_random(output)

        return output

    def choose_move(self, rounds):
        opp_moves = ['R', 'P', 'S']
        for turn in rounds:
            opp_moves.append(turn['p2'])

        self.round = len(opp_moves)
        self.opp_d = opp_moves.count('D')

        opp_moves = opp_moves[-self.memory:]
        counters = {
            'R': 'P',
            'P': 'S',
            'S': 'R',
            'W': 'X',
            'D': 'W',
        }
        move = counters[random.choice(opp_moves)]

        return move

    def check_dynamite(self, move):
        if random.randint(1, 100) < self.chaos:
            move = 'D'

        if move == 'D':
            if self.d_left < 1:
                return 'X'
            else:
                self.d_left -= 1
                return 'D'

        return move

    def check_water(self, move):
        if self.opp_d >= constants.NUM_DYNAMITE and move == 'W':
            move = 'X'
        return move

    def check_random(self, move):
        if move not in ['R', 'P', 'S', 'D', 'W']:
            return random.choice(['R', 'P', 'S'])
        else:
            return move


class RajBotPT(RajBot):
    def __init__(self):
        self.d_left = constants.NUM_DYNAMITE
        self.memory = 5
        self.chaos = 100
        self.opp_d = 0
        self.name = "ProtoType"
