import math
from time import time
from matplotlib import pyplot as plt
import scipy
import scipy.linalg
from TrussPy import prepare_input, Point, Line, Load, Input_Data, Bidirectional_Map, Frontend_Line, Frontend_Input_Data, Visualization_Data
from rich import print
import TrussPy as tp
import numpy as np
from TrussPy import draw


# truss: Frontend_Input_Data = {
#     'points': [
#         Point(0, 0, 2),
#         Point(1, 0, 2),
#         Point(0.5, math.sqrt(3)/6),
#         Point(0.5, math.sqrt(3)/2)
#     ],
#     'lines': [
#         Frontend_Line([0, 3], 0),
#         Frontend_Line([2, 3], 0),
#         Frontend_Line([1, 3], 0),
#         Frontend_Line([0, 2], 0),
#         Frontend_Line([2, 1], 0),
#         Frontend_Line([0, 1], 0)
#     ],
#     'loads': [
#         Load(3, 90.710, -70.710),
#     ],
#     'makings': [
#         {'E': 48e5, 'A': 1, 'rho': 0}
#     ]
# }
truss = tp.txt_load('./必做题.inp')

time_start = time()
input_data = tp.prepare_frontend_input(truss)
# for line in input_data['line']:
#     print(np.rad2deg(line['theta']))
# point_map = Bidirectional_Map()
# gem, gl = tp.get_global_stiffness_matrix_and_gravity_load(input_data, point_map)
# load = tp.get_load_matrix(input_data, gl, point_map)
# result = scipy.linalg.solve(gem, load)
result = tp.main(input_data)

print(result)
print((time() - time_start)*1000)

draw.plot_truss(input_data, 200)
draw.plot_truss_structure(result, 1000, 200)
plt.show()
# draw.pdf(result, input_data, './test.pdf', 2000, 200)
