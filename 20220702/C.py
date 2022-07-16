N,Q = map(int,input().split())
S=input()

def q1 (S,x):
  ans=S
  num=x//N
  ans = ans[N-num:]+ ans[:N-num]
  return ans

for _ in range (Q):
  qi,x = map(int,input().split())
  
  if qi == 1:
    S= q1(S,x)
  elif qi == 2:
    print (S[x-1])