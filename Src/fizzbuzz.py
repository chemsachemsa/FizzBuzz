def fizz_buzz(number: int) -> str:
    result = ""

    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"

    return result or str(number)
