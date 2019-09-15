scores = [290, 290, 300, 153, 290]
sorted_scores = scores.copy()
sorted_scores.sort(reverse=True)


def get_occurance(rank, score):
    return sorted_scores[:rank].count(score) - 1

def find_the_rank(score):
    index_list = [index for index, value in enumerate(scores) if value==score]
    return index_list


rank = 3
score = sorted_scores[rank - 1]
index = find_the_rank(score)[get_occurance(rank, score)]
print(index)
