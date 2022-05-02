def r_binSearch(array, target, track=0):
    left = 0
    right = len(array)-1

    if not array:
        return track
    elif len(array) == 1 and array[0] != target:
        return -1
    else:
        middle = (left + right) // 2

        if array[middle] == target:
            return track+middle
        elif array[middle] < target:
            return r_binSearch(array[middle+1:], target, track + middle + 1)
        else:
            return r_binSearch(array[:middle], target, track)

# end of r_binSearch

test_set = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

print('Search for 37:', r_binSearch(test_set, 37))
print('Search for 21:', r_binSearch(test_set, 21))