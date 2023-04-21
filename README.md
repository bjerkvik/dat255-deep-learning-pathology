# DAT255 Course Project
==============================

A deep learning project for pathology as part of the DAT255 course.

## Table of Contents

- [Background and Objectives](#background-and-objectives)
- [Methods and Data](#methods-and-data)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Results and Achievements](#results-and-achievements)

## Background and Objectives

Cancer is one of the leading causes of death worldwide, and early detection plays a crucial role in improving patient outcomes. Histopathology images are commonly used in the diagnosis of cancer, as they provide detailed information about the cellular structure of tissues. In this project, I aimed to develop a model capable of detecting cancer tumors in histopathology images.

## Methods and Data

To create the model, I used the [Histopathologic Cancer Detection](https://www.kaggle.com/competitions/histopathologic-cancer-detection/data) dataset, which consists of histopathology images of tumor tissue and non-tumor tissue. I used the fastai library for creating the deep learning model and the timm library to access additional model architectures. We chose the 'resnet26d' architecture for our model.

## Project Structure

The project repository contains the following files and folders:

- `notebooks/`: Folder containing the Jupyter Notebook for training and exporting the model.
- `app.py`: A Gradio app that uses the trained model to predict cancer tumors in histopathology images.
- `model.pkl`: The exported model file.
- `requirements.txt`: A list of Python packages required to run the app.
- `LICENSE`: The license for this project.
- `README.md`: The documentation for this project.

## Setup and Installation

The dataset used in this project consists of pathology images and accompanying metadata. Due to the size of the dataset, it is not included in the repository. To obtain the dataset, download the images and CSV file from the following link:

- [Kaggle - Histopathologic Cancer Detection](https://www.kaggle.com/competitions/histopathologic-cancer-detection)

Once you have downloaded the dataset, follow these steps:

1. Place the `train` folder inside the `data/raw` directory.
2. Place the four CSV file inside the `data/raw` directory alongside the `train` folder.

## Usage

The Gradio app is hosted on [Hugging Face](https://huggingface.co/spaces/trymbjerkvik/histopath-cancer-detector)

To use the Gradio app, follow these steps:

1. Click on the Hugging Face link.
2. Upload a histopathology image (96x96 pixels) using the file picker.
3. The app will display the prediction for the presence of tumor tissue in the image.

## Results and Achievements

Our deep learning model achieved an accuracy of [0.97]

<img width="239" alt="image" src="https://user-images.githubusercontent.com/54101071/233719132-5cb80c0d-711a-4f70-a798-f51dfaaf695a.png">
