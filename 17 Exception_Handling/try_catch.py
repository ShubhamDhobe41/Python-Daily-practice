# try:
#     result = 10 / 0   # This will raise ZeroDivisionError
# except ZeroDivisionError:
#     print("Cannot divide by zero!")


# try:
#     value = int(input('enter a number '))
# except (ValueError, TypeError) as e:
#     print("Invalid number:", e)
# else:
#     print("execute")
# finally:
#     print("cleaning..........")

# file = open("D:\\PythonDailyCode\\pythonwithVScode\\17 Exception_Handling\\data.txt")
# try:
#     data = file.read()
#     # process data...
# finally:
#     file.close()  # always closes file, even if an error occurred above



# lst = [1, 2, 3]
# try:
#     print(lst[5])
# except IndexError as e:
#     print("IndexError:", e)  # list index out of range


# d = {"a": 1}
# try:
#     print(d["b"])
# except KeyError as e:
#     print("KeyError:", e)  # 'b'


# try:
#     print("hello" + 5)
# except TypeError as e:
#     print("TypeError:", e)  # can only concatenate str (not "int") to str


# try:
#     num = int("abc")
# except ValueError as e:
#     print("ValueError:", e)  # invalid literal for int() with base 10: 'abc'

try:
    with open("nonexistent.txt") as f:
        f.read()
except (FileNotFoundError,TypeError) as e:
    print("FileNotFoundError:", e)
