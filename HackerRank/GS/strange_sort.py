mapping = [2, 1, 4, 8, 6, 3, 0, 9, 7, 5]
nums = ['12', '02', '4', '023', '65', '83', '224', '50']


def map_number(mapping, digit):
    for index in range(len(mapping)):
        if digit == mapping[index]:
            return index
    return 0


def get_occurance(sorted_values, index, value):
    return sorted_values[:index].count(value)


def find_the_rank(stock, new_numbers):
    index_list = [index for index, value in enumerate(new_numbers) if value == stock]
    return index_list


def strangeSort(mapping, nums):
    # Write your code here
    new_numbers = []
    final_numbers = []
    for number in nums:
        new_number = []
        for char in number:
            new_number.append(str(map_number(mapping, int(char))))
        new_number_int = int("".join(new_number))
        new_numbers.append(new_number_int)
    sorted_values = new_numbers.copy()
    sorted_values.sort()

    for index in range(len(sorted_values)):
        value = sorted_values[index]
        index = find_the_rank(value, new_numbers)[get_occurance(sorted_values, index, value)]
        final_numbers.append(nums[index])
    return final_numbers


print(strangeSort(mapping, nums))
