m_size = int(input())
set_m = set(map(int, input().split()))
n_size = int(input())
set_n = set(map(int, input().split()))
diff = set_m.symmetric_difference(set_n)
for val in sorted(diff):
    print(val)
