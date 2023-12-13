

def pascal(n):
    if n==0:
        return
    elif n==1:
        print('[1]')
        return [1]
    else:
        line=[1]
        p1=pascal(n-1)
        for i in range(len(p1)-1):
            line.append(p1[i]+p1[i+1])
        line+=[1]
    print(line)
    return line
i=int(input())
pascal(i)
