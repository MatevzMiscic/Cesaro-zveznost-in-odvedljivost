

def seq(a, b, c):
    while True:
        yield a
        yield b
        yield c

def to_tikz(seq, n):
    sum = 0
    for i in range(1, n+1):
        a = next(seq)
        sum += a
        print(f'\draw [fill=exrurv] ({i},{sum/i}) circle (3.5pt);')
        print(f'\draw [fill=rvwvcq] ({i},{a}) circle (3.5pt);')