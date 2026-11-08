



def minimax(depth, index, max_turn, scores, target_depth, counter):
    if depth == target_depth:
        counter[0] += 1
        return scores[index]

    if max_turn:
        return max(
            minimax(depth + 1, index * 2, False,
                    scores, target_depth, counter),
            minimax(depth + 1, index * 2 + 1, False,
                    scores, target_depth, counter)
        )
    else:
        return min(
            minimax(depth + 1, index * 2, True,
                    scores, target_depth, counter),
            minimax(depth + 1, index * 2 + 1, True,
                    scores, target_depth, counter)
        )


def alphabeta(depth, index, max_turn, scores,
              target_depth, alpha, beta, counter):

    if depth == target_depth:
        counter[0] += 1
        return scores[index]

    if max_turn:
        value = float('-inf')

        for child in [index * 2, index * 2 + 1]:
            value = max(value, alphabeta(
                depth + 1, child, False, scores,
                target_depth, alpha, beta, counter
            ))

            alpha = max(alpha, value)

            if beta <= alpha:
                break

        return value

    else:
        value = float('inf')

        for child in [index * 2, index * 2 + 1]:
            value = min(value, alphabeta(
                depth + 1, child, True, scores,
                target_depth, alpha, beta, counter
            ))

            beta = min(beta, value)

            if beta <= alpha:
                break

        return value



scores = [3, 5, 2, 9, 0, 0, 0, 7]

treeDepth = 3


minimax_count = [0]

minimax_value = minimax(
    0, 0, True, scores, treeDepth, minimax_count
)

alpha_count = [0]

alpha_value = alphabeta(
    0, 0, True, scores, treeDepth,
    float('-inf'), float('inf'), alpha_count
)

print("Reordered Branches")
print("Minimax Value:", minimax_value)
print("Minimax Leaf Evaluations:", minimax_count[0])

print("Alpha-Beta Value:", alpha_value)
print("Alpha-Beta Leaf Evaluations:", alpha_count[0])

