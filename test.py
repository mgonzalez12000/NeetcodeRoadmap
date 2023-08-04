matrix = [[1,2,3],[4,5,6],[7,8,9]]
m = len(matrix)
n = len(matrix[0])


answer = []
for _ in range(len(matrix)):
    answer.append([None] * len(matrix[0]))
print(answer)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        answer[j][i] = matrix[i][j]
print(answer)

ans = [[None] * m for _ in range(n)]
print(ans)