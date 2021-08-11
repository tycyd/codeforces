from sys import stdin, stdout


# 100^1 + 100^0
# 2^17 + 2^16 + 2^15 + 2^14 +……… + 2^0
#
# 3^11 + 3^10 + 3^9 + ….. 3^0
#
# A.     B.     C         D
# 0 => g1 => 1 => g2 => 1 => g3 => 2 => g4 => 2 => g5 => 3 => g6 => 3
# 1 => g1 => 0 => g2 => 2 => g3 => 1 => g4 => 3 => g5 => 2 => g6 => 4
# 2 => g1 => (X-1) => g2 => (X)
# a g => (a + x) % k = g =>
# if g - a < 0 => x = (g1 - a + k)
# if 0 <= g - a < k => x = (g1 - a)

# g2 - (g1 - a)
# g2 - (g1 - a + k)
# g2 - (g1 - a) + k
# g2 - (g1 - a + k) + k