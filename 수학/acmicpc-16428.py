a,b = map(int, input().split())
if b<0:
    mok = a//-b
    r = a+b*mok
    print(-mok,r,sep='\n')
else:
    print(a//b,a%b,sep='\n')
# 또는 나머지가 음수인 경우만 처리

m = a//b
r = a%b
if r<0:
    m = m + 1
    r = r - b
print(m)
print(r)