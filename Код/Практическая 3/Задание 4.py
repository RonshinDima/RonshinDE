def add ():
  a = int(input())
  b = int(input())
  L = int(input())
  N = int(input())
  s= 2 * L + (2 * N - 1) * a + 2 * (N - 1) * b
  return s
print("s=",add())

