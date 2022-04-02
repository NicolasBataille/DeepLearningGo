from DeepLearningGo import gotypes
from DeepLearningGo.gotypes import Player



#Arbitrary values for the example
MAX_SCORE = 10
MIN_SCORE = 1


def capture_diff(game_state):
	black_stones = 0
	white_stones = 0
	for r in range(1, game_state.board.num_rows + 1):
		for c in range(1, game_state.board.num_cols + 1):
			p = gotypes.Point(r, c)
			color = game_state.board.get(p)
			if color == gotypes.Player.black:
				black_stones += 1
			elif color == gotypes.Player.white:
				white_stones += 1
	diff = black_stones - white_stones
	if game_state.next_player == gotypes.Player.black:
		return diff
	return -1 * diff

def best_result(game_state, max_depth, eval_fn):
	if game_state.is_over():
		if game_state.winner() == game_state.next_player:
			return MAX_SCORE
		else:
			return MIN_SCORE
	if max_depth == 0:
		return eval_fn(game_state)
	best_so_far = MIN_SCORE
	for candidate_move in game_state.legal_moves():
		next_state = game_state.apply_move(candidate_move)
		opponent_best_result = best_result(next_state, max_depth - 1, eval_fn)
		our_result = -1 * opponent_best_result
		if our_result > best_so_far:
			best_so_far = our_result
	return best_so_far

def alpha_beta_result(game_state, max_depth, best_black, best_white, eval_fn):
	if game_state.is_over():
		if game_state.winner() == game_state.next_player:
			return MAX_SCORE
		else:
			return MIN_SCORE

	if max_depth == 0:
		return eval_fn(game_state)

	best_so_far = MIN_SCORE
	for candidate_move in game_state.legal_moves():
		next_state = game_state.apply_move(candidate_move)
		opponent_best_result = alpha_beta_result(next_state, max_depth - 1, best_black, best_white, eval_fn)
		our_result = -1 * opponent_best_result
		if our_result > best_so_far:
			best_so_far = our_result
		if game_state.next_player == Player.white:
			if best_so_far > best_white:
				best_white = best_so_far
			outcome_for_black = -1 * best_so_far
			if outcome_for_black < best_black:
				return best_so_far
		elif game_state.next_player == Player.black:
			if best_so_far > best_black:
				best_black = best_so_far
			outcome_for_white = -1 * best_so_far
			if outcome_for_white < best_white:
				return best_so_far
	return best_so_far