def generator3():
    for i in range(0, 101):
        if i % 11 == 0:
            yield i
def main():
    a = generator3()
    for i in a:
        print(i)