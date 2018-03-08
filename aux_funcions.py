import numpy as np

def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """

    # Creating a list of pairs for each 2 adjacent chars
    list_of_pairs = zip(word[0:len(word)-1],word[1:len(word)])

    # Check if two pairs are equal
    result = [x == y for x,y in list_of_pairs]

    # Find locations of matching pairs
    ind = [i for i,x in enumerate(result) if x]

    # If there are 3 elements of odd jumps or 3 elements of even jumps return True, else, return False
    diff = np.diff(ind)
    final_result = [ x == y for x,y in zip(diff[0:len(diff)-1],diff[1:len(diff)])]

    if True in final_result:
        return True
    else:
        return False

