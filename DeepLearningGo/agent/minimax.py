import random

from DeepLearningGo.agent.base import Agent
from DeepLearningGo.gameresult import GameResult



#To implement
def reverse_game_result(opponent_best_result):
	pass


class MinimaxAgent(Agent):

	def select_move(self, game_state):
		winning_moves = []
		draw_moves = []
		losing_moves = []
		for possible_move in game_state.legal_moves():
			next_state = game_state.apply_move(possible_move)
			opponent_best_outcome = self.best_result(next_state)
			our_best_outcome = reverse_game_result(opponent_best_outcome)
			if our_best_outcome == GameResult.win:
				winning_moves.append(possible_move)
			elif our_best_outcome == GameResult.draw:
				draw_moves.append(possible_move)
			else:
				losing_moves.append(possible_move)
		if winning_moves:
			return random.choice(winning_moves)
		if draw_moves:
			return random.choice(draw_moves)
		return random.choice(losing_moves)


	def best_result(self, game_state):
		best_result_so_far = GameResult.loss
		for candidate_move in game_state.legal_moves():
			next_state = game_state.apply_move(candidate_move)
			opponent_best_result = self.best_result(next_state)
			our_result = reverse_game_result(opponent_best_result)
			if our_result.value > best_result_so_far.value:
				best_result_so_far = our_result
		return best_result_so_far