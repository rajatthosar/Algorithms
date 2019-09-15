mat = [[3, 7, 5, 3, 4, 5],
       [4, 5, 2, 6, 5, 4],
       [7, 4, 9, 7, 8, 3]]

visited = []

for col_index in range(len(mat[0])):
    visited.append(max([columns[col_index] for columns in mat]))

visited.sort(reverse=True)

tom_score = 0
jerry_score = 0

for list_index in range(len(visited)):
    if list_index % 2 == 0:
        tom_score += visited[list_index]
    else:
        jerry_score += visited[list_index]

print(tom_score - jerry_score)
