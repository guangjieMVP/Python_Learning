
import math
while True:
    radius = float(input("请输入圆的半径："))
    perimeter = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    print("周长： %.2f" % perimeter)
    print("面积： %.2f " % area)