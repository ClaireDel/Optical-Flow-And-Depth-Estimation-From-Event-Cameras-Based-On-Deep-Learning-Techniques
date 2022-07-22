# Optical-Flow-And-Depth-Estimation-From-Event-Cameras-Based-On-Deep-Learning-Techniques

Data from event cameras have become readily available due to new camera products and public databases. These systems offer high temporal resolution, high dynamic range, low power consumption and high pixel bandwidth making them attractive for image-based navigation solutions. However, new computational techniques are required for this completely different data format. This research explores the use of deep learning techniques for the estimation of optical flow and depth from this data.

<p align="center">
  <img src="https://github.com/ClaireDel/Optical-Flow-And-Depth-Estimation-From-Event-Cameras-Based-On-Deep-Learning-Techniques/blob/main/pictures/of.PNG" width=400 height=auto> <br/> 
  Fig: Optical Flow Example
</p>

<p align="center">
  <img src="https://github.com/ClaireDel/Optical-Flow-And-Depth-Estimation-From-Event-Cameras-Based-On-Deep-Learning-Techniques/blob/main/pictures/depth.PNG" width=400 height=auto> <br/> 
  Fig: Depth Estimation Example
</p>


## 1. Datasets

### DSEC
The DSEC dataset can be downloaded [here](https://dsec.ifi.uzh.ch/dsec-datasets/download/).
The script [download_dsec_test.py](download_dsec_test.py) can be used to extract the data.
It downloads the dataset directly into the `OUTPUT_DIRECTORY` with the expected directory structure.
```python
download_dsec_test.py OUTPUT_DIRECTORY
```

### MVSEC
The MVSEC dataset can be downloaded here:

[MVSEC Outdoor Day 1 for 20 Hz evaluation](https://download.ifi.uzh.ch/rpg/ERAFT/datasets/mvsec_outdoor_day_1_20Hz.tar)

[MVSEC Outdoor Day 1 for 45 Hz evaluation](https://download.ifi.uzh.ch/rpg/ERAFT/datasets/mvsec_outdoor_day_1_45Hz.tar)

### DENSE
The Depth Estimation oN Synthetic Events (DENSE) Dataset can be downloaded here:

- [DENSE](http://rpg.ifi.uzh.ch/E2DEPTH.html)


| ```MVSEC``` | ```DSEC``` | 
|:---:|:---:|
|<img src="https://github.com/ClaireDel/Optical-Flow-And-Depth-Estimation-From-Event-Cameras-Based-On-Deep-Learning-Techniques/blob/main/pictures/msvec.jpeg" width="70%" height="30%">|<img src="https://github.com/ClaireDel/Optical-Flow-And-Depth-Estimation-From-Event-Cameras-Based-On-Deep-Learning-Techniques/blob/main/pictures/dsec.jpeg" width="70%" height="30%">|


## 2. Optical Flow Estimation
This part consists in

### Download

Download the network checkpoints and place them in the folder ```checkpoints/```:


[Checkpoint trained on DSEC](https://download.ifi.uzh.ch/rpg/ERAFT/checkpoints/dsec.tar)

[Checkpoint trained on MVSEC 20 Hz](https://download.ifi.uzh.ch/rpg/ERAFT/checkpoints/mvsec_20.tar)

[Checkpoint trained on MVSEC 45 Hz](https://download.ifi.uzh.ch/rpg/ERAFT/checkpoints/mvsec_45.tar)


### Running 
The same python code '....py' is used for this part.

The parse can be updated according to the type of results needed:

<p align="center">
  <img src="https://github.com/ClaireDel/Conflict-Detection---GDP2/blob/main/pictures/seg_airport.jpg" width=400 height=auto> <br/> 
  Fig: Example of segmentation
</p>



## 3. Depth Estimation
This part consists in

### Running

- Download the pretrained model:

```bash
wget "http://rpg.ifi.uzh.ch/data/E2DEPTH/models/E2DEPTH_si_grad_loss_mixed.pth.tar" -O pretrained/E2DEPTH_si_grad_loss_mixed.pth.tar
```

- Download the test sequence in the DENSE dataset:

```bash
wget "http://rpg.ifi.uzh.ch/data/E2DEPTH/dataset/test_sequence_00_town10.zip" -O data/test_sequence_00_town10.zip
```
- Extract the data sequence:

```bash
unzip -q data/test_sequence_00_town10.zip -d data/test
```

Before running the depth prediction, make sure the conda environment is sourced:

```bash
conda activate E2DEPTH
```

- Run reconstruction:

```bash
python run_depth.py -c pretrained/E2DEPTH_si_grad_loss_mixed.pth.tar \
  -i data/test/events/voxels \
  --output_folder /tmp \
  --save_numpy \
  --show_event \
  --display \
  --save_inv_log \
  --save_color_map
```
