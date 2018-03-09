from aux_funcions import trifeca, check_palindrome, get_student_list, compare_subjects_within_student


# Question 1
words = ['aaaa' ,'aabbcc','abccddee0123', 'llkkbmm', 'aaaazz', 'bbcCdd', 'AAA','112233', '', 'jskdfhgaa3424bb435cc53422bb52345cc']
print('\nQuestion 1:\n')
for string in words:
    result =  trifeca(string)
    print('The word '+ string + ' result is ' + str(result))

# Question 2:
print('\nQuestion 2:\n')
print('The resulting numbers were found to be palindromes for all 4 cases:')
check_palindrome()

#Question 3:
print('\nQuestion 3:\n')
# mock student list
studet_grades = get_student_list()
# Run on all students and grades
compare_subjects_within_student(studet_grades[0],studet_grades[1])