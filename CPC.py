
# extracte the contour through the display_contours function from visualize.py file
c = visualize.display_contours(image, r['rois'], r['masks'], r['class_ids'], 
                            dataset.class_names, r['scores'], ax=ax,
                            title="Predictions")

## np arrary of mask coordinates

# store contour into an a x b matrix
a = 2
b = int(np.size(c)/2)

mask = r['masks']
mask = mask.astype(int)
y_coo = mask.shape[1]
print(y_coo)

# empty array to store data
mask_polygon = np.empty(shape=[0, a]) 

# store all the coordinates into a list
for j in range(b):
    mask_polygon = np.append(mask_polygon, [[c[0][0][j][1], y_coo-c[0][0][j][0]]], axis=0)
print(b)

# visulize the contour
from shapely.geometry import Polygon
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator

ax = plt.gca() 

x_major_locator = MultipleLocator(200)
y_major_locator = MultipleLocator(200)

ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
plt.xlim(0,1024)
plt.ylim(0,1024)

poly = Polygon(mask_polygon)
x,y = poly.exterior.xy

plt.plot(x,y,color='orange')
plt.show

size_of_list = int(np.size(mask_polygon)/2)
print(size_of_list)
  
# find the fariest two points
Max_L = 0
point = []
index = 0
  
for i in range(size_of_list):
    for j in range(size_of_list):
      distance = np. linalg. norm(mask_polygon[i]- mask_polygon[j])
      if distance > Max_L:
        point = [mask_polygon[i],mask_polygon[j]]
        index = i
        index_2 = j

      else:
        pass
      Max_L = max(Max_L, distance)

print(Max_L)
print(point)
print(index,index_2)
print(mask_polygon[index])

# map the endpoints with the contour 
print(np.linalg.norm(point[0]-point[1]))

plt.plot(point[0][0], point[0][1], "ro")
plt.plot(point[1][0], point[1][1],"ro")

x_major_locator = MultipleLocator(200)
y_major_locator = MultipleLocator(200)

ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
plt.xlim(0,1024)
plt.ylim(0,1024)

p1 = [point[0][0], point[0][1]]
p2 = [point[1][0], point[1][1]]

plt.plot(x,y,color='orange')
plt.show

# path planning with "greedy"
# choose p1 as start and delete it from list
print(mask_polygon[index])

# create a new list to store path coordinates
print(mask_polygon[index])
print(i)
new_size_of_list = size_of_list-1
print(new_size_of_list )
path = np.empty(shape=[0, 2])
k = index+1
l = index-1

# calculate the center points from the endpoint p1
while k!=index or l!=index:
  if k == index_2 or l == index_2:
    break
  elif k <= new_size_of_list and l>=0:  
    new_point = ((mask_polygon[k][0]+mask_polygon[l][0])/2,(mask_polygon[k][1]+mask_polygon[l][1])/2) 
    path = np.append(path, [new_point], axis = 0)
    k = k + 1
    l = l- 1
  elif k > new_size_of_list and l>=0:
    k = 0
    new_point = ((mask_polygon[k][0]+mask_polygon[l][0])/2,(mask_polygon[k][1]+mask_polygon[l][1])/2) 
    path = np.append(path, [new_point], axis = 0)
    k = k + 1
    l = l- 1
  elif k > new_size_of_list and l<0:
    k = 0
    l = new_size_of_list
    new_point = ((mask_polygon[k][0]+mask_polygon[l][0])/2,(mask_polygon[k][1]+mask_polygon[l][1])/2) 
    path = np.append(path, [new_point], axis = 0)
    k = k + 1
    l = l- 1
  elif k<=new_size_of_list and l<0:
    l = new_size_of_list
    new_point = ((mask_polygon[k][0]+mask_polygon[l][0])/2,(mask_polygon[k][1]+mask_polygon[l][1])/2) 
    path = np.append(path, [new_point], axis = 0)
    k = k + 1
    l = l - 1

print(path)
print(np.size(path))

# transfom the format of the list 
r_1 = int(np.size(path)/2)

co_x = []
co_y = []
for h in range(r_1): 
  co_x.append(path[h][0])
  co_y.append(1024-path[h][1])

x_major_locator = MultipleLocator(200)
y_major_locator = MultipleLocator(200)

plt.xlim(0,1024)
plt.ylim(0,1024)

poly = Polygon(mask_polygon)
x,y = poly.exterior.xy
plt.plot(x,y)
plt.plot(point[0][0], point[0][1], "ro")
plt.plot(point[1][0], point[1][1],"ro")
p1 = [point[0][0], point[0][1]]
p2 = [point[1][0], point[1][1]]

# map the path with the detection image
x1 = np.array(co_x)
y1 = np.array(co_y)

ax = get_ax(1)
r = results[0]
visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], 
                            dataset.class_names, r['scores'], ax=ax,
                            title="Predictions")
log("gt_class_id", gt_class_id)
log("gt_bbox", gt_bbox)
log("gt_mask", gt_mask)
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
plt.plot(x1, y1)
plt.plot(x1,y1,color='white', linewidth= 5)

plt.show
