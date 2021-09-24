from bot import Bot
import random
import numpy as np

class DanBot(Bot):

    def __init__(self):
        self.dynamite_count = 0
        self.opponent_dynamite_count = 0
        self.round_count = 0
        self.played_moves = []
        self.moves = {'rock': 'R', 'paper': 'P', 'scissors': 'S', 'water': 'W', 'dynamite': 'D'}
        self.prop_dist = np.array([0.3, 0.3, 0.3, 0.1, 0])

    def make_move(self, gamestate):
        self.opponent_dynamite_counter(gamestate)
        moves = self.moves
        if self.dynamite_count == 100:
            redistribute = self.prop_dist[4]
            self.prop_dist[4] = 0
            for i in range(0,3):
                self.prop_dist[i] += redistribute / 3
        np.random.seed()
        move = np.random.choice(list(moves.values()), 1, p=self.prop_dist)[0]
        self.dynamite_counter(move)
        self.played_moves.append(move)
        self.round_count += 1
        if self.prop_dist[4] < 0.4 and self.dynamite_count != 100:
            self.increase_dynamite_prop()
        return move

    def dynamite_counter(self, move):
        if move == 'D':
            self.dynamite_count += 1


    def opponent_dynamite_counter(self, gamestate):
        if self.round_count >= 1:
            if gamestate['rounds'][self.round_count - 1]['p2'] == 'D':
                self.opponent_dynamite_count += 1
                self.prop_dist[3] -= 0.01
                choice = np.random.randint(0, 3)
                self.prop_dist[choice] += 0.01


    def increase_dynamite_prop(self):
        self.prop_dist[4] += 0.01
        choice = np.random.randint(0,3)
        self.prop_dist[choice] -= 0.01





