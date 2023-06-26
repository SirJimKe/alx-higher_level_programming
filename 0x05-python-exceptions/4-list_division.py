#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    a, b = my_list_1, my_list_2

    try:
        for i in range(list_length):
            try:
                if not isinstance(a[i], (int, float)) or \
                   not isinstance(b[i], (int, float)):
                    raise TypeError("wrong type")
                if b[i] == 0:
                    raise ZeroDivisionError("division by 0")
                result.append(a[i] / b[i])
            except IndexError:
                print("out of range")
                result.append(0)
            except (TypeError, ZeroDivisionError) as e:
                print(e)
                result.append(0)

    finally:
        return result
