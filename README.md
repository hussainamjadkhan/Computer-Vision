# Computer Vision

A basic computer vision project demonstrating how to load and display images using the OpenCV Python library.

## Overview

This repository contains the work for **Computer Vision Lab Task 01**. The project demonstrates the basic use of OpenCV for reading an image from a local folder and displaying it on the screen.

The repository also contains sample images used by the Python script.

## Project Structure

```text
Computer Vision/
│
├── Files/
│   └── images.py
│
├── Images/
│   ├── image1.jpg
│   └── image2.jpg
│
└── README.md
```

## Requirements

* Python 3.x
* OpenCV

Install OpenCV using:

```bash
pip install opencv-python
```

## Usage

The `images.py` script loads an image from the `Images` folder using OpenCV and displays it in a separate window.

Run the script from the root directory of the repository:

```bash
python Files/images.py
```

The image will remain open until a key is pressed.

## Images

The `Images` folder contains two sample images selected for this lab task. These images are used to demonstrate the image-loading functionality of OpenCV.

## Code

The main Python script is located at:

```text
Files/images.py
```

It uses OpenCV's `imread()` function to load an image and `imshow()` to display it.


Computer Science / Artificial Intelligence
Bahria University Islamabad
