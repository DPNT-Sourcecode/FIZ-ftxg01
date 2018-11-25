# noinspection PyUnusedLocal
def fizz_buzz(number):

    if (number % 3 == 0 or '3' in str(number)) and (number % 5 == 0 or '5' in str(number)):
        if number > 10 and (str(number) == len(str(number)) * str(number)[0]):
            return "fizz buzz deluxe"
        return "fizz buzz"
    if number > 10 and (str(number) == len(str(number)) * str(number)[0]):
        return "deluxe"
    if number % 3 == 0 or '3' in str(number):
        return "fizz"
    if number % 5 == 0 or '5' in str(number):
        return "buzz"
    return str(number)