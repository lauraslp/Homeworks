# Decorators
# # 1. Write a decorator that will allow you to execute code of a decorated function only during the day
# # (between 7 and 22).
# from _datetime import datetime as d
#
# #function that decorates other function. Decorator
# def decorate_my_function(func):
#     def execute_function():
#         if int(d.now().strftime('%d')) > 7 and int(d.now().strftime('%d')) < 22:
#             func()
#             print(f'Today is {d.now().strftime("%Y-%m-%d")} and {func.__name__} was executed')
#         else:
#             print(f'Today is {d.now().strftime("%Y-%m-%d")} and {func.__name__} can not be executed!')
#     return execute_function
#
# # function that will be decorated
# @ decorate_my_function
# def my_function():
#     print(f'This is my function')
#
# my_function()
# #  iskvieciama dekoruota funkcija
# # my_function = decorate_my_function(my_function)()

# # 1a. Write a similar decorator, but have it take hour arguments that determine when the function is
# # unavailable.
# from datetime import datetime as d
#
# def decorate_function(func):
#     def execute_function():
#         if int(d.now().strftime("%H")) <= 7 and int(d.now().strftime("%H")) >= 22:
#             print(f'Time now is {d.now().strftime("%H:%M")} and {func.__name__} can not be executed!')
#         else:
#             func()
#             print(f'Time now is {d.now().strftime("%H:%M")} and {func.__name__} was executed')
#     return execute_function
#
# @decorate_function
# def my_function():
#     print('This is my function')
# my_function()

# 2. Write a decorator that will show the hour, minute and second before calling the code of the decorated
# function and after calling the code of the decorated function.

from _datetime import datetime as d
import time as t

def decorate_my_function(func):
    def print_time():
        print(f'Time before {func.__name__} {d.now().strftime("%H:%M:%S")}')
        func()
        print(f'Time after {func.__name__} {d.now().strftime("%H:%M:%S")}')
    return print_time

# @ leidzia nerasyti my_function = decorate_my_function(my_function)()
@decorate_my_function
def my_function():
    print(f'My function was executed')
    t.sleep(2)

# my_function = decorate_my_function(my_function)()
my_function()