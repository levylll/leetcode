


total = 1
m = 4
n = 4
def process(i, j):
    if i < m-1 and j < n-1:
        return total * process(i+1, j) + process(i, j+1)
    else:
        return 1

print(process(0, 0))
