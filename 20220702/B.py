from numpy import around


N= int(input())
A = [[]]*N

for i in range(N):
  A[i] = list(str(input()))
# print (A)

def findMaxNum(A):
  num=0
  for i in range(N):
    for j in range(N):
      if num < int(A[i][j]):
        num =int(A[i][j])
  return num

def findIndex(num):
  ans=[]
  for i in range(N):
    for j in range(N):
      if num == int(A[i][j]):
        ans.append([i,j])
  return ans

Nmax=findMaxNum(A)

IM=findIndex(Nmax)
CD=len(IM)

# print (CD)

def addstring(A,N):
  for i in range(N):
    ans+=A[x+1][y]+A[x+1][y]+A[x+1][y]

def main (x,y,arrow):
  ans=A[x][y]
  if arrow == "N":
    xi=x 
    for _ in range(N-1):
      xi-=1
      ans+=A[xi][y]

  elif arrow == "S":
    xi=x 
    for _ in range(N-1):
      xi+=1
      if N <= xi:
        xi = xi - N
      ans+=A[xi][y]
      
  elif arrow == "E":
    yi=y
    for _ in range(N-1):
      yi+=1
      if N <= yi:
        yi = yi - N
      ans+=A[x][yi]
      
  elif arrow == "W":
    yi=y
    for _ in range(N-1):
      yi-=1
      ans+=A[x][yi]
      
  elif arrow == "NE":
    xi=x 
    yi=y
    for _ in range(N-1):
      xi-=1
      yi+=1
      if N <= yi:
        yi = yi - N
      ans+=A[xi][yi]
    
  elif arrow == "NW":
    xi=x
    yi=y
    for _ in range(N-1):
      xi-=1
      yi-=1
      ans+=A[xi][yi]
  elif arrow == "SE":
    xi=x
    yi=y
    for _ in range(N-1):
      xi+=1
      yi+=1
      if N <= xi:
        xi = xi - N
      if N <= yi:
        yi = yi - N
      ans+=A[xi][yi]
  elif arrow == "SW":
    xi=x
    yi=y
    for _ in range(N-1):
      xi+=1
      yi-=1
      if N <= xi:
        xi = xi - N
      ans+=A[xi][yi]
  return int(ans)


ans=0
for i in range (len(IM)):
  S=IM[i]
  X=main(S[0],S[1],"N")
  if X > ans:
    ans=X
  X=main(S[0],S[1],"S")
  if X > ans:
    ans=X
  X=main(S[0],S[1],"E")
  if X > ans:
    ans=X
  X=main(S[0],S[1],"W")
  if X > ans:
    ans=X
  X=main(S[0],S[1],"NE")
  if X > ans:
    ans=X
  X=main(S[0],S[1],"NW")
  if X > ans:
    ans=X
  X=main(S[0],S[1],"SE")
  if X > ans:
    ans=X
  X=main(S[0],S[1],"SW")
  if X > ans:
    ans=X
print (ans)