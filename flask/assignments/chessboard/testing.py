

arr = []


def make_matrix(x,y):
    for i in range(y):
        arr.append([])
        for j in range(x):
            arr[i].append(0)
    
    return arr

a = make_matrix(4,4)
print(a)