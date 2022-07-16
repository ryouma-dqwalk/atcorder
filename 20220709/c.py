S=input()
X=input()


def main (s):
  tmp=""
  fl=""
  for i in range(len(s)):
    if s[i] == fl:
      continue
    elif i == len(s) -1:
      tmp+=s[i]
    elif s[i] ==s[i+1]:
      fl=s[i]
      tmp+=s[i].upper()
    else:
      tmp+=s[i]
  return (tmp)


if len(S) > len(X):
  print ("No")
elif main(S) == main(X):
  print ("Yes")
else:
  print ("No")

print (main(S),main(X))
# print ("No" if len(S) < len(X) elif main(S) == main(X) else "No")