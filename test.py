current = (0, 0)
c = (0.5, 0.1)

for i in range(10) :
    current = (current[0] * current[0] - current[1] * current[1] + c[0], 2 * current[0] * current[1] + c[1])

print(current)