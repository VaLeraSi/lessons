def val_checker(l_func):
    def val_checker_2(func):
        def wrapper(num):
            if l_func(num):
                print(func(num))
            else:
                raise ValueError(f"wrong val {num}")

        return wrapper

    return val_checker_2


@val_checker(lambda num: num > 0)
def calc_cube(num):
    return num ** 3


try:
    a = calc_cube(5)
except ValueError as err:
    print(err)
