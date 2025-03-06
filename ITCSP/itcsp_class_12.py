student_grades = {'Ana': 'B', 'Katy': 'A', 'John': 'B'}
# print(student_grades)
# s_grade = student_grades['Ana']
# print(s_grade)
# # s_grade = student_grades[0] ERROR

# s_grade = student_grades.get('Rob', 'No such key...')
# print(s_grade)

# print(student_grades)

student_grades['Bob'] = 'A'
# print(student_grades)
# student_grades["Ana"] = 2
# print(student_grades)

# enumerate function

# a = enumerate('Hello')
# print(a)
# print(type(a))
# print(list(a))
# b = enumerate(['a', 'b', 'c'])
# print(list(b))
# a1 = list(a)
# for e in a1:
#     print(str(e[0]+1)+'. '+e[1])
# DELETING AN ENTRY
# print(student_grades)
# del (student_grades['Katy'])
# s_grade = student_grades.pop('Bob')
# print(s_grade)
# print(student_grades)

# cc = {}
# cc['Poland'] = 'Warsaw'
# cc['France'] = 'Paris'

# print(cc)

# test if key in dictionary
# print('John' in student_grades)

# print(student_grades.keys())
# print(list(student_grades.keys()))

# for k in student_grades.keys():
#     print(k)


# print(student_grades.values())
# print(list(student_grades.values()))
# for v in student_grades.values():
#     print(v)


# print(student_grades.items())
# print(list(student_grades.items()))
# for i in student_grades.items():
#     print(i)


# for k, v in student_grades.items():
#     print(k, v)
# # len returns amount of pairs
# print(len(student_grades))

# clear removes all items

# student_grades.clear()
# print(student_grades)
# copy returns a copy of the dictionary
student_grades_01 = student_grades  # new name but the same object
# print(student_grades)
# print(student_grades_01)
# student_grades['Ana'] = 'C'
# print(student_grades)
# print(student_grades_01)
# student_grades_02 = student_grades.copy()
# print(student_grades_02)

data = {
    "key1": {
        "inner_key1": 1,
        "inner_key2": 2
    },
    "key2": {
        "inner_key1": 3,
        "inner_key2": 4
    }
}

# value = data.get("inner_key1").get("key1", "KEY NOT FOUND ERROR")
value = data['key1']['inner_key2']
print(value)
