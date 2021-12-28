# Cleaning-path-calculation

Created based on the `inspect_model.ipynb` originated from [here](https://github.com/matterport/Mask_RCNN)


#### Step 1: 
Extract the detected mask result from Mask R-CNN-based weld seam detection model.

<img width="200" src='https://github.com/Tzu-Jan/Cleaning-path-calculation/blob/main/images/mask.png'/> <img width="200" src='https://github.com/Tzu-Jan/Cleaning-path-calculation/blob/main/images/mask2.png'/> <img width="200" src='https://github.com/Tzu-Jan/Cleaning-path-calculation/blob/main/images/mask3.png'/>

<img width="200" height="200" src='https://github.com/Tzu-Jan/Cleaning-path-calculation/blob/main/images/conturs.png'/><img width="200" height="200" src='https://github.com/Tzu-Jan/Cleaning-path-calculation/blob/main/images/conturs2.png'/><img width="200" height="200" src='https://github.com/Tzu-Jan/Cleaning-path-calculation/blob/main/images/conturs3.png'/>

#### Step 2:
Calculate the two points with longest distance

<img width="200" height="200" src="https://github.com/Tzu-Jan/Cleaning-path-calculation/blob/main/images/endpoints.png"/><img width="200" height="200" src="https://github.com/Tzu-Jan/Cleaning-path-calculation/blob/main/images/endpoints2.png"/><img width="200" height="200" src="https://github.com/Tzu-Jan/Cleaning-path-calculation/blob/main/images/endpoints3.png"/>

#### Step 3:

Calculate the final path using Greedy Algorithm

<img width="200" height="200" src="https://github.com/Tzu-Jan/Cleaning-path-calculation/blob/main/images/path.png"/><img width="200" height="200" src="https://github.com/Tzu-Jan/Cleaning-path-calculation/blob/main/images/path2.png"/><img width="200" height="200" src="https://github.com/Tzu-Jan/Cleaning-path-calculation/blob/main/images/path3.png"/>
