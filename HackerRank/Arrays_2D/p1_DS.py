def get_hourglass(arr, first_row, first_col):
    hourglass = arr[first_row:first_row + 3]
    hourglass = [tow[first_col:first_col + 3] for tow in hourglass]
    hourglass[1][0], hourglass[1][2] = 0, 0
    return hourglass


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglasses = []
    hourglass_sums = []
    for row_index in range(len(arr) - 2):
        for col_index in range(len(arr[0]) - 2):
            hourglass = get_hourglass(arr, row_index, col_index)
            hourglasses.append(hourglass)
            temp_flat_list = [element for sublist in hourglass for element in sublist]
            hourglass_sums.append(sum(temp_flat_list))

    return max(hourglass_sums)


arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

print(hourglassSum(arr))
