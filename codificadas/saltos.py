import sys

MAX_VAL = 200000
dist = [4] * (MAX_VAL + 1)
dist[0] = 0
squares = [i*i for i in range(1, int(MAX_VAL**0.5) + 1)]

def precompute_distances():
  for s in squares: dist[s] = 1
  for a in squares:
    for b in squares:
      if a+b <= MAX_VAL: dist[a+b] = min(dist[a+b], 2)
      if abs(a-b) <= MAX_VAL: dist[abs(a-b)] = min(dist[abs(a-b)], 2)
  for i in range(MAX_VAL + 1):
    if dist[i] <= 2:
      for s in squares:
        if i+s <= MAX_VAL: dist[i+s] = min(dist[i+s], 3)
        if abs(i-s) <= MAX_VAL: dist[abs(i-s)] = min(dist[abs(i-s)], 3)

precompute_distances()

# Leitura da entrada: quantidade de casos t
line = sys.stdin.readline()
if line:
  t = int(line.strip())
  for _ in range(t):
    n, q = map(int, sys.stdin.readline().split())
    for _ in range(q):
      a, b = map(int, sys.stdin.readline().split())
      print(dist[abs(a - b)])