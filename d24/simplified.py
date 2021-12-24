
from itertools import product

res = [0 for _ in range(14)]
def magic(attempt):
	z = 0
	idx = 0

	for i in range(14):

		if inc[i] > 0:
			z = (z * 26) + attempt[idx] + inc[i]
			res[i] = attempt[idx]
			idx += 1
		else:
			x = (z % 26) + inc[i]
			if x > 9 or x < 1:
				return False
			# just assume x == w
			res[i] = x
			z //= 26
	print(res)
	return True

def spell(possibilities, ex):
	print(ex, end='')
	for option in possibilities:
		if magic(option) == True:
			break

inc = [6, 7, 10, 2, -7, 8, 1, -5, 5, -3, -0, -5, -9, -0]
mod = [             15,       10,     3,  5, 11, 12, 10]
opt = product([9,8,7,6,5,4,3,2,1], repeat = 7)
sub = product([1,2,3,4,5,6,7,8,9], repeat = 7)

spell(opt, "ex00:")
spell(sub, "ex01:")
