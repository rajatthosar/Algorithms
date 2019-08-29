def swap(lIdx, rIdx):
    """

    :param lIdx: Left Index
    :param rIdx: Right Index
    :return: nothing
    """

    temp = array[lIdx]
    array[lIdx] = array[rIdx]
    array[rIdx] = temp


def partition(array, firstIdx, lastIdx):
    """

    :param array: array being partitioned
    :param firstIdx: head of the array
    :param lastIdx: tail of the array
    :return: index of pivot element after sorting
    """

    pivot = array[lastIdx]

    # Counter i is used as a marker to fill the array with all
    # elements smaller than pivot. At the end of the loop
    # pivot is swapped with the next position of i as all the
    # elements before pivot are smaller than it
    lowIdx = firstIdx - 1

    # Note that range function stops the sequence generation at
    # lastIdx. This means that there will be
    # (lastIdx - firstIdx) - 1 elements in the sequence.
    # The last item generated in the sequence will be lastIdx - 1
    for arrayIdx in range(firstIdx, lastIdx):
        if array[arrayIdx] <= pivot:
            lowIdx += 1
            swap(lowIdx, arrayIdx)

    swap(lowIdx + 1, lastIdx)

    return lowIdx + 1


def quickSort(array, firstIdx, lastIdx):
    """

    :param array: Array to be sorted
    :param firstIdx: head of the array
    :param lastIdx: tail of the array
    :return: sorted array
    """

    if firstIdx < lastIdx:
        pivot = partition(array, firstIdx, lastIdx)
        quickSort(array, firstIdx, pivot - 1)
        quickSort(array, pivot + 1, lastIdx)
    print(array)


if __name__ == "__main__":
    array = [10, 80, 30, 90, 40, 50, 70]
    firstIdx = 0
    lastIdx = len(array) - 1
    quickSort(array, firstIdx, lastIdx)
