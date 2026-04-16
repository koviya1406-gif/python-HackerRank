import math
ab = int(input())
bc = int(input())
angle_radians = math.atan2(ab, bc)
angle_degrees = math.degrees(angle_radians)
result = round(angle_degrees)
print(str(result) + "\u00b0")
