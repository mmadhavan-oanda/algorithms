def unique_chars(string):
    """

    Check if all the chars are unique

    Note: the important thing is to not use any ds

    Idea is to shift bits equal to ord of a given
    character and then checking for overlap in that
    character's bit using the & operation, in this
    code the checker variable is constantly updated
    with the bits of all the chars so when a char is
    repeated and I perform & operation then eg:

    say we encounter 'h'. we first check if there is an
    overlap in the 'h' bit of the checker variable (note we
    get the 'h' bit by shifting 1 to ord(h) times to the
    left). If there is an overlap, it means we have
    previously seen 'h' before and the result will have a 1
    in the 'h' bit (1 & 1 = 1) which will cause the overall
    value to be greater than 0.

    Also note: The mask is not the result of bitwise left
               shift of 1, ord(num) times eg:

    mask = 0

    mask |= ord('a')

    mask:

    10000000000000000000000000000000000000000000000000000000000
    000000000000000000000000000000000000000

    mask |= ord('b')

    mask:

    11000000000000000000000000000000000000000000000000000000000
    0000000000000000000000000000000000000000

    and so on, so if I do a bitwise shift of all the alphabets then
    mask will be

    11111111111111111111111110000000000000000000000000000000000
    00000000000000000000000000000000000000000000000000000000000
    0000

    therefore if there is any repetitions then when you perform &
    operation then the result will be > 0

    If there is no overlap, then we do
    checker = checker | 1 << ord(h), this will store the 'h'
    bit in checker (which can be used for later checks)

    Note: This algorithm only works with either upper
    letters or lower letters since ord(h) != ord(H)
    """

    # We convert the string to lower to make this algorithm work
    string = string.lower()
    checker = 0
    for c in string:
        if (checker & 1 << ord(c)) > 0:
            print 'Not unique'
            print c
            break
        checker |= 1 << ord(c)


def unique_ints(myarray):
    """
    Same concept, for array of ints.

    Note, this may not work for very big ints
    """
    checker = 0

    for val in myarray:
        if checker & 1 << val:
            print 'Non unique'
            print val
            break
        checker |= 1 << val


if __name__ == '__main__':
    print '\nmohan'
    unique_chars('mohan')
    print '\nmohhan'
    unique_chars('mohhan')
    a = [1, 2, 3, 4, 55, 6, 7, 55]
    print
    print a
    unique_ints(a)
