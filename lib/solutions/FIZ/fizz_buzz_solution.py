# noinspection PyUnusedLocal
def fizz_buzz(number):

    if (number % 3 == 0 or '3' in str(number)) and (number % 5 == 0 or '5' in str(number)):
        delux = deluxe(number)
        if delux:
            return "fizz buzz " + delux
        return "fizz buzz"

    if number % 3 == 0 or '3' in str(number):
        delux = deluxe(number)
        if delux:
            return "fizz " + delux
        return "fizz"

    if number % 5 == 0 or '5' in str(number):
        delux = deluxe(number)
        if delux:
            return "buzz " + delux
        return "buzz"

    delux = deluxe(number)
    if delux:
        return delux

    return str(number)

def deluxe(number):
    if number > 10 and (str(number) == len(str(number)) * str(number)[0]):
        if number % 2 == 0:
            return "fake deluxe"
        return "deluxe"
