# Motion Detector Using OpenCV

This project is a basic motion detector implemented using Python and OpenCV. It captures video from a webcam and detects motion by applying background subtraction.

## Features

- Captures video from a webcam.
- Detects motion using the MOG2 background subtraction algorithm.
- Displays both the actual video feed and the motion-detected feed.

## Prerequisites

To run this script, you need to have Python installed along with OpenCV. You can install OpenCV using the following command:

```bash
pip install opencv-python

Usage
Clone or download this repository:

Save the motion detection script (e.g., motion_detector.py).
Run the script: Open a terminal or command prompt in the project directory and run:

bash
python motion_detector.py

Control the script:

The webcam will start, and two windows will appear:
actual_frame: Shows the live video feed.
motion_frame: Shows the motion detected.
To exit the program, press the Esc key.

How It Works
The script captures video using OpenCV's VideoCapture.
It uses the MOG2 background subtraction algorithm to detect moving objects in the video feed.
It displays two windows:
The live video feed.
A binary image highlighting areas where motion is detected.
License
This project is licensed under the MIT License.#   M o t i o n - D e t e c t o r  
 