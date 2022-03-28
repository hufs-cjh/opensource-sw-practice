# 컴퓨터 전자시스템공학 202004520 최준혁

print("HELLO WORLD!")


def some_func(a, b):
    print(a)
    a = a + b
    print(b)
    b = b + b
    c = a+b+a+b
    print(c)

    return c+c+c

x, y=map(int, input().split())
print(some_func(x, y))
