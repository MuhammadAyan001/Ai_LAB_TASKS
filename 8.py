import math

def minimax(depth, node_index, is_max_turn, scores, max_depth, alpha, beta):
    if depth == max_depth:
        return scores[node_index]

    if is_max_turn:
        best = -math.inf
        
        
        value = minimax(depth + 1, node_index * 2, False, scores, max_depth, alpha, beta)
        best = max(best, value)
        alpha = max(alpha, best)
        
        if beta <= alpha:
            return best
        
       
        value = minimax(depth + 1, node_index * 2 + 1, False, scores, max_depth, alpha, beta)
        best = max(best, value)
        alpha = max(alpha, best)
        return best
    
    else:
        best = math.inf
        
       
        value = minimax(depth + 1, node_index * 2, True, scores, max_depth, alpha, beta)
        best = min(best, value)
        beta = min(beta, best)
        
        if beta <= alpha:
            return best
        
       
        value = minimax(depth + 1, node_index * 2 + 1, True, scores, max_depth, alpha, beta)
        best = min(best, value)
        beta = min(beta, best)
        return best


scores = [3, 5, 2, 9, 3, 5, 2, 9]


max_depth = int(math.log(len(scores), 2))


optimal_value = minimax(
    depth=0,
    node_index=0,
    is_max_turn=True,
    scores=scores,
    max_depth=max_depth,
    alpha=-math.inf,
    beta=math.inf
)

print("Optimal Value:", optimal_value)