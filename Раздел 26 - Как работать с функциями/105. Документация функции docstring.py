"""
DOCSTRING - ИСПОЛЬЗУЕТСЯ ДЛЯ ДОКУМЕНТИРОВАНИЯ ФУНКЦИЙ, КЛАССОВ, МОДУЛЕЙ
"""


def mult_by_factor(value, mult=1):
    """Multiplies number by multiplicator"""
    return value * mult


print(mult_by_factor(5))


def print_number_info(num):
    """
    Prints num inforamtion      

    Args:
        num (int):int number

    Returns:
        int: number
    """
    if (num % 2) == 0:
        print("Num is even")
    else:
        print("Num is odd")
    return num


print_number_info(20)
