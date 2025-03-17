s = input()

def clearDigits(s: str) -> str:
    y = []
    # print(x)
    for i in s:
        # print(i)
       if i.isdigit():
           y.pop()
       else:
           y.append(i)

    z = "".join(y)
    return z

print(clearDigits(s))