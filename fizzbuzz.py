primes = [3, 5, 7]
words = {3: "fizz", 5: "buzz", 7: "woof"}


def in_digits(number):
    result = {prime: 0 for prime in primes}
    while number:
        if number % 10 in primes:
            result[number % 10] += 1
        number //= 10
    return result


def multiplicities(number):
    result = {prime: 0 for prime in primes}
    for prime in primes:
        while number % prime == 0:
            result[prime] += 1
            number //= prime
    return result


def total_count(number):
    first = in_digits(number)
    second = multiplicities(number)
    return {prime: first[prime] + second[prime] for prime in primes}


def fizzbuzz(number):
    calculations = total_count(number)
    if any(calculations.values()):
        return " ".join((" ".join(words[prime] for _ in range(calculations[prime]))) for prime in primes).strip()
    return str(number)


def solve(limit):
    with open("fizzbuzz.txt", "w") as f:
        for number in range(1, limit+1):
            f.write("{} {}\n".format(number, fizzbuzz(number)))


solve(2000)
