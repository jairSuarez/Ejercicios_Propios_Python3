fibonacci = [0,1]

for i in range(10):
    num = fibonacci[i] + fibonacci[i+1]
    fibonacci.append(num)

for f in fibonacci:
    print(f)
    