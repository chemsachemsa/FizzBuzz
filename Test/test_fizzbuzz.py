from fizzbuzz import fizz_buzz


def test_retourne_nombre_comme_chaine():
    assert fizz_buzz(1) == "1"


def test_retourne_fizz_pour_multiples_de_3():
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(6) == "Fizz"


def test_retourne_buzz_pour_multiples_de_5():
    assert fizz_buzz(5) == "Buzz"
    assert fizz_buzz(10) == "Buzz"


def test_retourne_fizzbuzz_pour_multiples_de_3_et_5():
    assert fizz_buzz(15) == "FizzBuzz"
    assert fizz_buzz(30) == "FizzBuzz"
