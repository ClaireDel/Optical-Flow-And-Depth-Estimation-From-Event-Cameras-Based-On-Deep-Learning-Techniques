# Optical-Flow-And-Depth-Estimation-From-Event-Cameras-Based-On-Deep-Learning-Techniques

Data from event cameras have become readily available due to new camera products and public databases. These systems offer high temporal resolution, high dynamic range, low power consumption and high pixel bandwidth making them attractive for image-based navigation solutions. However, new computational techniques are required for this completely different data format. This research explores the use of deep learning techniques for the estimation of optical flow and depth from this data.

<p align="center">
  <img src="https://github.com/ClaireDel/Conflict-Detection---GDP2/blob/main/pictures/intro.jpg" width=400 height=auto> <br/> 
  Fig: Model Inference
</p>


## 1. Datasets

### DSEC
The DSEC dataset for optical flow can be downloaded [here](https://dsec.ifi.uzh.ch/dsec-datasets/download/).
We prepared a script [download_dsec_test.py](download_dsec_test.py) for your convenience.
It downloads the dataset directly into the `OUTPUT_DIRECTORY` with the expected directory structure.
```python
download_dsec_test.py OUTPUT_DIRECTORY
```

### MVSEC
To use the MVSEC dataset for our approach, it needs to be pre-processed into the right format. For your convenience, we provide the pre-processed dataset here:

[MVSEC Outdoor Day 1 for 20 Hz evaluation](https://download.ifi.uzh.ch/rpg/ERAFT/datasets/mvsec_outdoor_day_1_20Hz.tar)

[MVSEC Outdoor Day 1 for 45 Hz evaluation](https://download.ifi.uzh.ch/rpg/ERAFT/datasets/mvsec_outdoor_day_1_45Hz.tar)

| ```Repartition``` | ```MVSEC``` | ```DSEC``` |
|:---:|:---:|:---:|
|<img src="https://github.com/ClaireDel/Conflict-Detection---GDP2/blob/main/pictures/dataset_repartition.png" width="100%" height="30%">|<img src="https://github.com/ClaireDel/Conflict-Detection---GDP2/blob/main/pictures/image.png" width="70%" height="30%">|<img src="https://github.com/ClaireDel/Conflict-Detection---GDP2/blob/main/pictures/image_crop.png" width="100%" height="30%">|


## 2. Optical Flow Estimation
This part consists in

### Download

Download the network checkpoints and place them in the folder ```checkpoints/```:


[Checkpoint trained on DSEC](https://download.ifi.uzh.ch/rpg/ERAFT/checkpoints/dsec.tar)

[Checkpoint trained on MVSEC 20 Hz](https://download.ifi.uzh.ch/rpg/ERAFT/checkpoints/mvsec_20.tar)

[Checkpoint trained on MVSEC 45 Hz](https://download.ifi.uzh.ch/rpg/ERAFT/checkpoints/mvsec_45.tar)


### Running <br/> 
The same python code '....py' is used for this part.

The parse can be updated according to the type of results needed:

```

<p align="center">
  <img src="https://github.com/ClaireDel/Conflict-Detection---GDP2/blob/main/pictures/seg_airport.jpg" width=400 height=auto> <br/> 
  Fig: Example of segmentation
</p>



## 3. Depth Estimation
This part consists in 
