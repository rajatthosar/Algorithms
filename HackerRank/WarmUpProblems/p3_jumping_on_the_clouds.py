def jumpingOnClouds(c):
    index = 0
    jump_count = 0
    total_clouds = len(c)

    while index < total_clouds:
        if (index + 2 < total_clouds) and (c[index + 2] == 0):
            index += 2
            jump_count += 1
        elif (index + 1 < total_clouds) and (c[index + 1] == 0):
            index += 1
            jump_count += 1
        else:
            index += 1

    return jump_count


c = [0, 0, 0, 1, 0, 0]
print(jumpingOnClouds(c))
