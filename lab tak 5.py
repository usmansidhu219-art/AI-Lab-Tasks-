import math

leaf_count = 0

def alpha_beta(curDepth, nodeIndex, maxTurn,
               scores, targetDepth, alpha, beta):

    global leaf_count

    # Base case
    if curDepth == targetDepth:
        leaf_count += 1
        return scores[nodeIndex]

    if maxTurn:
        best = float("-inf")

        for child in [nodeIndex * 2, nodeIndex * 2 + 1]:
            value = alpha_beta(
                curDepth + 1, child, False,
                scores, targetDepth, alpha, beta
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float("inf")

        for child in [nodeIndex * 2, nodeIndex * 2 + 1]:
            value = alpha_beta(
                curDepth + 1, child, True,
                scores, targetDepth, alpha, beta
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


scores = [3, 5, 2, 9, 0, 7]
treeDepth = math.ceil(math.log2(len(scores)))

scores += [0] * (2**treeDepth - len(scores))

result = alpha_beta(
    0, 0, True, scores, treeDepth,
    float("-inf"), float("inf")
)

print("Alpha-Beta optimal value:", result)
print("Leaf evaluations:", leaf_count)
