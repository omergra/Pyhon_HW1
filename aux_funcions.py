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
    two_equal = [x == y for x,y in list_of_pairs]

    # Find locations of matching pairs
    ind = [i for i,x in enumerate(two_equal) if x]
    odd = [i for i in ind if i%2]
    even = [i for i in ind if not(i%2)]

    # If there are at least 3 elements of odd jumps or 3 elements of even jumps return True, else, return False
    diff_odd = [y - x for x, y in zip(odd[0:len(odd) - 1], odd[1:len(odd)])]
    diff_even = [y - x for x, y in zip(even[0:len(even) - 1], even[1:len(even)])]

    # Check for consecutive pairs
    if (diff_odd.count(2) >= 2) or (diff_even.count(2) >= 2):
        return True
    else:
        return False


def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.

    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """


    for sample in range(100000,999997):
        return_val = is_sample_4_philandrome(sample)
        if (return_val != False):
            print(return_val)

def is_sample_4_philandrome(sample):
    """
    Checks a single six digit number for all 4 for stages
    input: 6 digit number, a list
    output: if number is philandrome - thr first stage of the number
            else False
    """
    return_value = False
    assert (len(str(sample)) == 6) & (sample < 999997)
    # Checks the first step - last 4 digits
    if (str(sample)[2:6] == str(sample)[2:6][::-1]):
        sample = sample + 1
        if (str(sample)[1:6] == str(sample)[1:6][::-1]):
            sample = sample + 1
            if (str(sample)[1:5] == str(sample)[1:5][::-1]):
                sample = sample + 1
                if (str(sample) == str(sample)[::-1]):
                    return_value = sample - 3
    return return_value

def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    # Extracting the subjects name from both dictionaries
    subject_list = [subj1_all_students.pop('Subject', None), subj2_all_students.pop('Subject', None)]


    # For each key in first dictionary, check if key appears in second dictionary and find max value index
    for key, value in subj1_all_students.items():
        if key in subj2_all_students.keys():
            max_elements = list((max(value), max(subj2_all_students[key])))
            print(key+' preffered subject is '+ subject_list[max_elements.index(max(max_elements))])


def get_student_list():
    # generates a dictionary containing the students name and grades in two
    history = {'Subject':'History', 'Mark': [90, 100], 'Alice': [50, 70], 'Ruth': [90, 85], 'Alex': [85, 80]}
    math = {'Subject': 'Math', 'Mark': [70, 71], 'Alice': [90, 85], 'Ruth': [76, 87]}
    return history, math