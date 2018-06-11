#creat with :PyCharm
#Author:Wilson
#Date:2018/5/14
#Time:16:53


def triangles():
    result = [1]
    while True:
        print("")
        yield result
        result = [1]+[result[x]+result[x+1] for x in range(len(result)-1)]+[1]
        n = 1
        while n <= len(result)-1:
            print(" ", end="")
            print("/", "\\", end="")
            n += 1
    return result


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

