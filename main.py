from __future__ import print_function
from diffequations import diff_equations
import matplotlib.pyplot as plt
from service import servicefunctions, functions, systemfunctions as sf
from diffequations import diffsystems as ds

eps = 0.001
num = 20
beg = 0
end = 5
y10 = 1
y20 = 2
x, y1, y2, n = ds.eulerian_fourth_grade(sf.y1, sf.y2, beg, end, y10, y20, num, eps)

y11, y12, y13, y21, y22, y23, y14, y24 = y1[0], y1[1], y1[2], y2[0], y2[1], y2[2], y1[3], y2[3]

x1, y15, y25, n = ds.adams_third_grade(sf.y11, sf.y22, beg, end, y11, y12, y13, y21, y22, y23, num, eps)
print('adams 3 for systems', n)
x2, y35, y45, n = ds.adams_fourth_grade(sf.y11, sf.y22, beg, end, y11, y12, y13, y14, y21, y22, y23, y24, num, eps)
print('adams 4 for systems', n)
