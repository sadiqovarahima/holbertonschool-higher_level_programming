#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_lenght):
    res = []
    for i in range(list_lenght):
        try:
            res.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            res.append(0)
        except TypeError:
            print("wrong type")
            res.append(0)
        except ZeroDivisionError:
            print("division by 0")
            res.append(0)
        finally:
            pass
    return res
