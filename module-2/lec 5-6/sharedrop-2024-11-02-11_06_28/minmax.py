import math
def minimax (curDepth, nodeIndex,
			maxTurn, scores, 
			targetDepth):
	if (curDepth == targetDepth): 
		return scores[nodeIndex]
	if (maxTurn):
		return max(minimax(curDepth + 1, nodeIndex * 2, 
					False, scores, targetDepth), 
				minimax(curDepth + 1, nodeIndex * 2 + 1, 
					False, scores, targetDepth))
	else:
		return min(minimax(curDepth + 1, nodeIndex * 2, 
					True, scores, targetDepth),     
				minimax(curDepth + 1, nodeIndex * 2 + 1, 
					True, scores, targetDepth))
# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]
treeDepth = math.log(len(scores), 2)
print(treeDepth)

print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))

"""
                    [Root]
                      0
                   (Max)
                    /   \
                  /       \
                /           \
              1               2
           (Min)            (Min)
           /     \          /     \
         /         \      /         \
       3             4   5            6
    (Max)         (Max) (Max)       (Max)
     /   \         /   \   /   \       /   \
   7       8     9    10  11    12   13    14
 (Leaf) (Leaf) (Leaf) (Leaf) (Leaf) (Leaf) (Leaf) (Leaf)
   3       5     2      9     12      5     23      23
"""
