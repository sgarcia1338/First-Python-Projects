

def fibonacci_generator():
  x = 0
  y = 1
  while True:
    yield x
    z = x + y
    x = y
    y = z

r = []
for n in fibonacci_generator():
    print(n)
    r.append(n)
    if n > 100:
        break
check_equal(r, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
