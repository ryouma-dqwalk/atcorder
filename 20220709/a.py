N,M,X,T,D = map(int,input().split())

def main (M):
  if M >=X :
    ans = T
  else:
    ans = T- (X-M)*D
  return ans 

print (main(M))

