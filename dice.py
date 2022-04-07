import random as r
# x = r.random(1,6)

## For printing random number between particular range, we use randint() for integer
x = r.randint(1,6)

## For printing random number between particular range, we use uniform() for float numbers
# x = r.uniform(1.0,6.0)

if x == 1:
    print("-------------")
    print("|           |")
    print("|     *     |")
    print("|           |")
    print("-------------")

elif x == 2:
    print("-------------")
    print("|           |")
    print("|     *     |")
    print("|     *     |")
    print("|           |")
    print("-------------")

elif x == 3:
    print("-------------")
    print("|           |")
    print("|     *     |")
    print("|     *     |")
    print("|     *     |")
    print("|           |")
    print("-------------")

elif x == 4:
    print("-------------")
    print("|           |")
    print("|   *   *   |")
    print("|   *   *   |")
    print("|           |")
    print("-------------")

elif x == 5:
    print("-------------")
    print("|           |")
    print("|   *   *   |")
    print("|     *     |")
    print("|   *   *   |")
    print("|           |")
    print("-------------")

elif x == 6:
    print("-------------")
    print("|           |")
    print("|   *   *   |")
    print("|   *   *   |")
    print("|   *   *   |")
    print("|           |")
    print("-------------")