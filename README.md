# Optical-Flow-And-Depth-Estimation-From-Event-Cameras-Based-On-Deep-Learning-Techniques

Data from event cameras have become readily available due to new camera products and public databases. These systems offer high temporal resolution, high dynamic range, low power consumption and high pixel bandwidth making them attractive for image-based navigation solutions. However, new computational techniques are required for this completely different data format. This research explores the use of deep learning techniques for the estimation of optical flow and depth from this data.

<p align="center">
  <img src="https://github.com/ClaireDel/Conflict-Detection---GDP2/blob/main/pictures/intro.jpg" width=400 height=auto> <br/> 
  Fig: Model Inference
</p>


## 1. Datasets
[COCO download](http://cocodataset.org/#download): COCO dataset used to train the segmentation model (HRNet)

[Dataset download](https://drive.google.com/drive/folders/1Ezkcq8TW7NJFyS-yKSb8dmNqIFabs2nr):  Original and cleaned dataset (images cropped + black backgrounds)

| ```Repartition``` | ```Original image``` | ```Image cropped``` |
|:---:|:---:|:---:|
|<img src="https://github.com/ClaireDel/Conflict-Detection---GDP2/blob/main/pictures/dataset_repartition.png" width="100%" height="30%">|<img src="https://github.com/ClaireDel/Conflict-Detection---GDP2/blob/main/pictures/image.png" width="70%" height="30%">|<img src="https://github.com/ClaireDel/Conflict-Detection---GDP2/blob/main/pictures/image_crop.png" width="100%" height="30%">|


## 2. Optical Flow Estimation
This part consists in the first part of the model using HRNet used to get the predicted key points on each human body presents on an image, a video or a video launch. 

### Utilisation <br/> 
[Models required](https://drive.google.com/drive/folders/1Ezkcq8TW7NJFyS-yKSb8dmNqIFabs2nr): Need to download the models folder and place it in the running folder according to the following architecture: 

```

### Running <br/> 
The same python code 'demo.py' is used for this part. The model can be updated but the one used by default is in 'demo/inference-config.yaml'. 

The parse can be updated according to the type of results needed:

```
python Segmentation_phase/demo/demo.py
```
- use --webcam when the input is a real-time camera.
- use --video [video-path] when the input is a video.
- use --image [image-path] when the input is an image.
- use --write to save the image, camera or video result.
- use --showFps to show the fps (this fps includes the detection part).

<p align="center">
  <img src="https://github.com/ClaireDel/Conflict-Detection---GDP2/blob/main/pictures/seg_airport.jpg" width=400 height=auto> <br/> 
  Fig: Example of segmentation
</p>



## 3. Depth Estimation
This part consists in the first part of the model using HRNet used to get the predicted key points on each human body presents on an image, a video or a video launch. 
