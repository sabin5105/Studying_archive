import sys

n = sys.stdin.readline().split() # a = list
a = int(n[0])
b = int(n[1])
c = int(n[2])

def check_odd(n):
    if n%2 == 0:
        return True
    return False


if check_odd(b):
    # 짝수
    print((pow(a,b/2) * pow(a,b/2))%c)
else:
    # 홀수
    print((pow(a,(b-1)/2) * pow(a,(b-1)/2) * a)%c)