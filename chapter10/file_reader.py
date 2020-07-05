# with open('chapter10\pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())
#路径为：python chapter9\file_reader.py


with open('pi_digits.txt') as file_object:#file_object = open('pi_digits.txt')
    contents = file_object.read()
    print(contents.rstrip())
#路径为：cd chapter10
#       python file_reader.py
