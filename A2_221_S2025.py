
def solution():
    data = [[1, 2, 3, 4], 
            [1, 2, 3, 4], 
            [1, 2, 3, 4], 
            [1, 2, 3, 4]]

    for i in range(len(data)):
        for j in range(len(data[i])):
            neighbors = -data[i][j]
            top = max(0, i-1)
            bottom = min(len(data)-1, i+1)
            left = max(0, j-1)
            right = min(len(data[i])-1, j+1)
            # print(top, bottom, left, right, neighbors)
            for m in range(top, bottom+1, 1):
                for n in range(left, right+1, 1):
                    print(data[m][n], end=" ")
            print()

solution()