for i in range(20):
    div3 = i % 3 == 0
    div5 = i % 5 == 0

    if div3 and div5:
        print("FizzBuzz")
    elif div3:
        print("Fizz")
    elif div5:
        print("Buzz")
    else:
        print(i)