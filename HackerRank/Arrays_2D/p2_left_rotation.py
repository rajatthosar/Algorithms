def rotLeft(a, d):
    n = len(a)
    if d > n:
        return rotLeft(a, d % n)
    else:
        new_list = [0] * n

        for index in range(n):
            new_index = (n - d + index) % n
            new_list[new_index] = a[index]

    return new_list


a = [1,2,3,4,5]
d = 10
print(rotLeft(a,d))
