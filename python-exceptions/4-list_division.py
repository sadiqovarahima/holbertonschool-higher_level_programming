#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_lenght):
    new_list = []
    for i in range(list_lenght):
        try:
            res = 0
            num1 = my_list_[i]
            num2 = my_list_2[i]
            res = num1 / num2
        except IndexError:
            print("out of range")
            res = 0
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        finally:
            new_list.append(res)
    retun new_list
