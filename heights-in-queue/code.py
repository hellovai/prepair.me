import copy

if __name__ == "__main__":
    n = int(raw_input())
    a = [0] * n
    b = [0] * n
    for i in xrange(0,n):
        tmp = raw_input().split(' ')
        x = [int(j) for j in tmp]
        a[i] = x[0]
        b[i] = x[1]
	shift = [0 for i in range(n)]
	d = [0 for i in range(n)]
	queue = [-1 for i in range(n)]

	c = copy.deepcopy(a)
	c.sort()
	for i in range(n):
		temp = c.index(a[i])
		d[temp] = b[i]

	for i in range(n):
		queue[d[i]+shift[d[i]]] = c[i]
		shift[d[i]] += 1

    for x in queue:
        print x,