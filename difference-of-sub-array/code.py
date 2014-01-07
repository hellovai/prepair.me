def max_contiguous_subarray_abs_diff(A):
  n = len(A)
  assert n > 0
  left_min, left_max = left_min_max(A)
  right_min, right_max = left_min_max(A[::-1])
  max_diff = 0
  for i in xrange(n - 1):
    smallest = min(left_min[i], right_min[n - 2 - i])
    largest = max(left_max[i], right_max[n - 2 - i])
    diff = abs(largest - smallest)
    if max_diff < diff:
      max_diff = diff
  return max_diff

def left_min_max(A):
  n = len(A)
  pre_min = [0] * (n + 1)
  pre_max = [0] * (n + 1)
  pre = [0] * (n + 1) # :i
  for i in xrange(0, n):
    pre[i + 1] = pre[i] + A[i]
    pre_min[i + 1] = pre_min[i]
    if pre_min[i + 1] > pre[i + 1]:
      pre_min[i + 1] = pre[i + 1]
    pre_max[i + 1] = pre_max[i]
    if pre_max[i + 1] < pre[i + 1]:
      pre_max[i + 1] = pre[i + 1]
  left_min = [None] * (n - 1)
  left_max = [None] * (n - 1)
  for i in xrange(0, n - 1):
    left_min[i] = pre[i + 1] - pre_max[i]
    left_max[i] = pre[i + 1] - pre_min[i]
  return (left_min, left_max)

if __name__ == "__main__":
	_ = raw_input()
	A = [int(i) for i in raw_input().split(' ')[0:-1]][1:]
	print max_contiguous_subarray_abs_diff(A)
 