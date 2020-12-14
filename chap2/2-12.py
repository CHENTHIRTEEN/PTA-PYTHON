import math

a, b, c = map(int, input().split())
s = (a + b + c) / 2
if a + b > c and a + c > b and b + c > a:
    print(f"area = {math.sqrt(s * (s - a) * (s - b) * (s - c)):.2f}; perimeter = {a + b + c:.2f}")
else:
    print("These sides do not correspond to a valid triangle")