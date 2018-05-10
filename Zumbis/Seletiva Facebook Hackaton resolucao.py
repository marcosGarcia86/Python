def hack1(n, k):
  def f(s):
    return s.count('1')
  binários = []
  for x in range(2**n):
    binários.append(bin(x))
  binários.sort(key=f, reverse = True)
  return binários[k - 1]

def hack(n, k):
  return sorted([bin(x) for x in range(2**n)],
                key=lambda s: s.count('1'),
                reverse = True)[k-1]
  
