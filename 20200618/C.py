from pytz import common_timezones


h1,h2,h3,w1,w2,w3 = map(int,input().split())

def slove(n):
  ans=[]
  for i in range(1,n-1):
    if i > w1-2:
      continue
    for j in range(1,n-1):
      if j > w2-2:
        continue
      for k in range(1,n-1):
        if k > w3-2:
          continue
        if (i+j+k)==n:
          ans.append([i,j,k]) 
  return ans

p1=slove(h1)
p2=slove(h2)
p3=slove(h3)
# new_p1=[e for e in p1 if e[0]<= w1-2 and e[1] <= w2-2 and e[2]<= w3-2]
# new_p2=[e for e in p2 if e[0]<= w1-2 and e[1] <= w2-2 and e[2]<= w3-2]
# new_p3=[e for e in p3 if e[0]<= w1-2 and e[1] <= w2-2 and e[2]<= w3-2]

def slove_w(p1,p2,p3,w1,w2,w3):
  cnt=0
  for i in range(len(p1)):
    for j in range(len(p2)):
      for k in range(len(p3)):
        if p1[i][0]+p2[j][0]+p3[k][0]==w1 and \
          p1[i][1]+p2[j][1]+p3[k][1]==w2 and \
          p1[i][2]+p2[j][2]+p3[k][2]==w3:
          cnt+=1
  return cnt
print (slove_w(p1,p2,p3,w1,w2,w3))
# print (slove_w(new_p1,new_p2,new_p3,w1,w2,w3))