
def f_plus(xi, ci):
    return xi + ci

def f_multi(xi, ci):
    return ci* xi

def f_square(xi):
    # print(xi**2)
    return xi**2

for x in range(500):
    print(x)
    for N in range(1, 100):
        Y = x % N

        for c in range(300):
            assert(f_plus(x, c) % N == f_plus(Y, c) % N)
            

            assert(f_multi(x, c) % N == f_multi(Y, c) % N)

        fx = f_square(x)
        fy = f_square(Y)
        assert(fx % N == fy % N)


