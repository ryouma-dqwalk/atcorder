N= int(input())
A= list(map(int,input().split()))

P=0
pin=[0,0,0,0]

for i in A:
  pin[0]=1

  pin_tmp=[0,0,0,0]
  for j in range(4):
    if pin[j]==1:
      if (j+i) >=4:
        P+=1
      else:
        pin_tmp[j+i]=1
  pin=pin_tmp

print (P)