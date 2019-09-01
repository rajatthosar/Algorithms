def sockMerchant(ar):
    count_list = []
    visited_list = []
    accumulator = 0

    for element in ar:
        if element not in visited_list:
            visited_list.append(element)
            count_list.append(1)
        else:
            index = visited_list.index(element)
            count_list[index] += 1

    for count_val in count_list:
        accumulator += count_val // 2

    return accumulator


ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(ar))
