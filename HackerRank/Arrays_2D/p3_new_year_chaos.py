def swap(ticket_queue, index):
    """
    This function swaps the values indicated at index with the next value

    :param ticket_queue: The list in which swapping is to be performed
    :param index: the index of the element to swap. This element is
                  swapped with the element at (index - 1)th position

    :return: updated queue after swapping
    """

    temp = ticket_queue[index]
    ticket_queue[index] = ticket_queue[index - 1]
    ticket_queue[index - 1] = temp

    return ticket_queue


def is_sorted(q):
    """
    Checks if the queue is sorted

    :param q: The queue to check
    :return: boolean
    """

    for index in range(len(q) - 1):
        if q[index] < q[index + 1]:
            continue
        else:
            return False
    return True


def minimumBribes(q):
    """
    This function returns the number of bribes needed to achieve the
    current state of the queue.

    :param q: Current queue

    :return: number of bribes -OR- "Too chaotic"
            type: String
    """

    swap_counter = 0

    # Number of people each person can bribe
    k = len(q)

    for step in range(k):
        # Complexity: THETA(2)

        for index in range(len(q) - 1, 0, -1):
            # Complexity: THETA(n)

            if q[index] < q[index - 1]:
                q = swap(q, index)
                swap_counter += 1
        print(q)

    if is_sorted(q):
        # Complexity: THETA(n)
        return swap_counter
    else:
        return "Too chaotic"
    # Total time complexity: THETA(2n) + THETA(n) = THETA(3n) => THETA(n)


q = [7, 1, 3, 2, 4, 5, 6]
print(minimumBribes(q))
