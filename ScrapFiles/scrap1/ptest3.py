import math


def minmax(curDepth, nodeIndex, maxTurn, scores, targetDepth):

    if curDepth == targetDepth:
        return scores[nodeIndex]

    if (maxTurn):
        return max(minmax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth), minmax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))

    else:
        return min(minmax(curDepth+1, nodeIndex*2, True, scores, targetDepth), minmax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))


scores = [3, 5, 2, 9, 12, 5, 23, 23]
treeDepth = math.log(len(scores), 2)

print("Optimal value is : ", end='')
print(minmax(0, 0, True, scores, treeDepth))
