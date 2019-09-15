string = "zzzxxzzzz"


def get_comm(string1, string2):
    count = 0
    checker = list(string2)
    for char in string1:
        if char in checker:
            count += 1
            checker.remove(char)
    return count


def max_comm(string):
    unique_elems = []
    comm_list = []
    if len(string) < 2:
        return 0
    chars = list(string)
    for index in range(len(chars)):
        if chars[index] not in unique_elems:
            unique_elems.append(chars[index])
        else:
            string1 = "".join(chars[:index])
            string2 = "".join(chars[index:])
            comm_list.append(get_comm(string1, string2))
    return max(comm_list)


print(max_comm(string))
