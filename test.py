def gen():
    yield from range(5)


gen_li = [gen() for i in range(5)]
while True:
    num = len(gen_li)
    if num <= 0:
        break
    for gen in gen_li:
        try:
            next(gen)
        except StopIteration:
            gen_li.

print('end')
