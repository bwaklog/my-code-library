def greet():
    print("Hi there!")


def fxn(x):
    print(2 * x ** 2)


def facts(n):
    from functools import reduce

    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def add_num(n1, n2):
    print(n1 + n2)


def l_arg(*args):
    print(args)
    print(list(facts(i) for i in args))


def squaed(x, y, z):
    return x*x, y*y, z*z


def calc_sum(x, y):
    z = x + y
    return z



if __name__ == '__main__':
    # fxn(25)
    # print(facts(122))
    # add_num(n1=int(input("Enter 1:")), n2=int(input("Enter 2:")))
    # l_arg(1232,432,432,413321)
    # a = squaed(32, 27, 25).__iter__()
    #
    # try:
    #     print(a.__next__())
    #     print(a.__next__())
    #     print(a.__next__())
    # except:
    #     pass

    print(calc_sum(3, 2))

