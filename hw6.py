def geom_prog(mult):
    if not isinstance(mult, (int, float)):
        raise TypeError("Множитель должен быть числом")
    if mult == 0:
        raise ValueError("Множитель не может равняться нулю")
    b = 1
    while True:
        yield b
        b *= mult

def my_range(start, stop, step = 1):
    if step == 0:
        raise ValueError("Шаг не может быть нулем!")
    if stop > start and step > 0:
        while start < stop:
            yield start
            start += step
    if stop > start and step < 0:
        raise ValueError("Шаг должен быть положительным числом!")
    if stop < start and step < 0:
        while start > stop:
            yield start
            start += step
    if stop < start and step > 0:
        raise ValueError("Шаг должен быть отрицательним числом!")

def prime_number(limited):
    digit = 1
    while digit < limited:
        for div in range(2, digit):
            if not digit % div:
                digit += 1
                break
        else:
            yield digit
            digit += 1



if __name__ == "__main__":
    print("Exercise 1:")
    x = geom_prog(3)
    for i in x:
        if i > 100:
            x.close()
            break
        print(i)

    print("\nExercise 2:")
    rng = my_range(0, 10, 2)
    for item in rng:
        print(item)

    print("\nExercise 3:")
    prm_num = prime_number(100)
    for item in prm_num:
        print(item)

    print("\nExercise 4:")
    lim = 10
    a = [x**3 for x in range(2, lim + 1)]
    print(a)
