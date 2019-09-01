"""
All test cases passed
"""

def countingValleys(s):
    valley_count = 0
    track = 0
    prev_step = 0

    for step in s:
        if step.lower() == 'u':
            track += 1
            prev_step = 1
        else:
            track -= 1
            prev_step = -1
        if track == 0 and prev_step == 1:
            valley_count += 1

    return valley_count


print(countingValleys("UDDDUDUU"))