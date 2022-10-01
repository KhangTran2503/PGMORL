from utils import generate_weights_batch_dfs
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


weights_batch = []
min_weight =  0.0
max_weight = 1.0
delta_weight = 0.1
obj_num = 3
#args.obj_num, args.min_weight, args.max_weight, args.delta_weight
generate_weights_batch_dfs(0, obj_num, min_weight, max_weight, delta_weight, [], weights_batch)

print(weights_batch)
print(len(weights_batch))

x = [w[0] for w in weights_batch]
y = [w[1] for w in weights_batch]
z = [w[2] for w in weights_batch]

ax = plt.axes(projection='3d')
ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5);

plt.show()