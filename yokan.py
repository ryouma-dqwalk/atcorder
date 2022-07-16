N,L=map(int,input().split())
K=int(input())
A=list(map(int,input().split()))

def slove(mid):
  cnt=0; pre=0;
  for i in range(N):
    if A[i] -pre >= mid and L -A[i] >=mid:
      cnt += 1;
      pre=A[i]
  if cnt >= K:
    return True
  return False

def binary_search(list, item):
    low = 0                        # lowとhighを使ってリストの検索部分を追跡
    high = len(list) - 1
    while low <= high:             # 1つの要素に絞り込まれるまでの間は...
        mid = (low + high) // 2
        guess = list[mid]          # 真ん中の要素を調べる
        if guess == item:          # アイテムを検出
            return mid
        if guess > item:           # 推測した数字が大きすぎた
            high = mid - 1
        else:                      # 推測した数字が小さすぎた
            low = mid + 1
    return None                    # アイテムが存在しない
my_list = [1, 3, 5, 7, 9]          # テストしてみる
print binary_search(my_list, 3)    # 結果は1：リストは0始まりなので、
