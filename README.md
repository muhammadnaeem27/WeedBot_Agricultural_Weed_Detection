# Weed Detection and Robotic Car Deployment

This project aims to detect and manage four common weed types in agriculture - Lamb's Quarter, Nut Grass, Parthenium hysterophorus, and Borh. We gathered a custom dataset based on farmer interviews to identify these harmful and prevalent weeds. Our approach involves dataset preprocessing, YOLOv5 model training, testing, and the development of a user-friendly GUI for weed detection. We also deployed this system on a robotic car for real-world field testing.

## Table of Contents
1. [Project Overview](#major-steps)
2. [Problem Statement](#problem-statement)
3. [How to Run the Code](#how-to-run-the-code)
4. [Links and Resources](#links-and-resources)

## Project Overview
1. **Data Set Gathering**: We collected data from interviews with farmers to identify the most common and harmful weeds.
2. **Dataset Preprocessing**: Our initial dataset of 600 images was augmented to 1400 images for model training, with annotations.
3. **YOLOv5 Model Training**: We used YOLOv5 for object detection and trained the model on Google Colab.
4. **Model Testing**: The model was tested on test images and in real-world environments.
5. **GUI Development**: We created a user-friendly GUI for easy use, enabling the following:
   - Weed image detection
   - Wireless camera input
   - Custom trained .pt model input
   - Detection graph generation
   - Weed coordinate identification
6. **Data Open Sourcing**: Our dataset is available on Roboflow and includes the 4 harmful weed types identified through farmer surveys. We've also provided links to the interview videos with farmers.

7. **Deployment on Robotic Car**: After successful software testing, we deployed the system on a robotic car equipped with motors. We used a mobile phone camera as a wireless input and tested the model in real fields where these weeds are commonly found.

[Watch Our Project Video](https://www.youtube.com/watch?v=0Td1oyGz89U)
[Read Our Project Report](https://drive.google.com/file/d/1Z5ZObSlPNUdkdIquQbBMoKtcok56EkIP/view?usp=drive_link)

## Problem Statement
Farmers face numerous challenges due to the proliferation of harmful weeds. This project aims to provide an effective solution for weed detection and management. By automating the detection process, we help farmers identify and control weed growth, ultimately increasing crop yield and reducing the need for manual labor.

## How to Run the Code
1. Create and activate a virtual environment in Windows using the following commands:
    ```
    python -m venv env  # Virtual environment creation
    .\env\Scripts\activate  # Activation of the virtual environment
    ```
2. Clone repo and install [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt) in a [**Python>=3.8.0**](https://www.python.org/) environment, including
[**PyTorch>=1.8**](https://pytorch.org/get-started/locally/).
   ```bash
   pip install ultralytics
   git clone https://github.com/muhammadnaeem27/WeedBot_Agricultural_Weed_Detection.git  # clone
   cd WeedBot_Agricultural_Weed_Detection/my_files
   pip install -r requirements.txt  # install
   ```  
6. Pre-Trained model file "best.pt" is already exist in the "my_files" directory.

7. To use the project, run the file "run_detect.py" with the following command:
    ```
    python run_detect.py
    ```

   This will open a user-friendly GUI interface for detecting and managing weeds.

<div style="display: flex; justify-content: center; align-items: center; height: 300px;">
  <div style="border-radius: 20px; overflow: hidden;">
    <img src="GUI_interface.gif" alt="GUI interface GIF" style="max-width: 80%; height: 50%;" />
  </div>
</div>



## Links and Resources

- <a href="https://universe.roboflow.com/zeeshan/weed-classification/dataset/8" target="_blank">Dataset on Roboflow</a>
- <a href="https://www.youtube.com/watch?v=o4avFYoFz5s" target="_blank">Interview Video with Farmers</a>
- <a href="https://www.youtube.com/watch?v=0Td1oyGz89U" target="_blank">Project Video</a>
- <a href="https://drive.google.com/file/d/1Z5ZObSlPNUdkdIquQbBMoKtcok56EkIP/view?usp=drive_link" target="_blank">Project Report</a>

## Reference 
This project utilizes [YOLOv5](https://github.com/ultralytics/yolov5) for object detection.
