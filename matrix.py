import re

n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

decoded_string = "".join(["".join(row[i] for row in matrix) for i in range(m)])

print(re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded_string))
