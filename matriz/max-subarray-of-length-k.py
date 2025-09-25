from collections import deque

def max_subarray(arr, k):
  dq = deque()
  res = []

  for i, val in enumerate(arr):
    while dq and dq[0] <= i - k:
      dq.popleft()
    
    while dq and arr[dq[-1]] < val:
      dq.pop()

    dq.append(i)

    if i >= k - 1:
      res.append(arr[dq[0]])

  return res

def main():
  arr = list(map(int, input().split()))
  k = int(input())

  print(max_subarray(arr, k))

  return 0

if __name__ == "__main__":
  main()