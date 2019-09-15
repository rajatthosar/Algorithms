data = [1, 1, 1, 1, 1, 1, 1, 7, 7, 7, 7, 7, 7, 7]

def whatever():
    running_avg_list = []
    for index in range(6, len(data)):
        avg = sum(data[index - 6:index + 1]) / 7
        running_avg_list.append(str(round(avg, 2)))

    return running_avg_list
