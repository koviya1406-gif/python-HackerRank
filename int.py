import re
t = int(raw_input())
for _ in range(t):
    try:
        s = raw_input()
        re.compile(s)
        print True
    except re.error:
        print False

