c1, c2 = input().split(' ')
c1_rvsd = int("".join(reversed(c1)))
c2_rvsd = int("".join(reversed(c2)))
if c1_rvsd > c2_rvsd:
  print(c1_rvsd)
else:
  print(c2_rvsd)