import random

class MinimaxAgent(Agent):

	def select_move(self, game_state):
		winning_moves = []
		draw_moves = []
		losing_moves = []
		for possible_move in game_state.legal_moves():
			next_state = game_state.apply_move(possible_move)
			opponent_best_outcome = best_result(next_state)
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


	def best_result(game_state):
		if game_state.is_over():
			if game_state.winner() == game_state.next_player:
				return GameResult.win
			elif game_state.winner() is None:
				return GameResult.draw
			else:
				return GameResult.loss