def generator2(t):
    buffer = t.split(' ')
    for j in buffer:
        if j.find('\n') != -1:
            yield j
        else:
            yield j
def main():
    a = generator2
    for el in a:
        print(el)