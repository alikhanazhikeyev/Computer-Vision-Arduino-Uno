This project combines Electronics and Computer Vision using an Arduino microcontroller and Python libraries such as MediaPipe and OpenCV for finger detection, and pyserial for Arduino–Python communication.

This project is an extension of the original “Arduino Computer Vision Finger Counter” by [@vbookshelf](https://github.com/vbookshelf).

![Project Demonstration](images/project-demo.png) 

## Enhancements in this version:
- Added LEDs that light up when a corresponding finger is raised.
- Optimized the Python script by reducing the number of FPS for smoother performance.

## Features
- Real-time finger detection using a webcam.
- Sends finger states to Arduino via Serial communication.
- Lights up corresponding LEDs for each raised finger.
- Optimized FPS for smoother and more efficient detection.

## Requirements
- Python 3.10–3.14
- opencv-python
- mediapipe==0.10.9
- pyserial
- Arduino microcontroller
- Breadboard, LEDs, resistors, jumper wires

## Arduino Setup
1.	Connect a breadboard to the Arduino microcontroller.
2.	Components needed:
- 5 LEDs
- 5 x 220 Ω resistors
- 6 jumper wires
3.	Connect GND from Arduino to the breadboard.
4.	Place 5 LEDs on the breadboard and connect them to Arduino digital pins 3–7.
5.	Connect each LED through a 220 Ω resistor to GND.
![Arduino Setup](images/arduino_setup.jpg)

## How to run the project?
1. Install project zip, Python, all libraries mentioned above, and Arduino IDE
2. Upload Arduino scetch on your board in Arduino IDE, make sure you selected your board and port (usb) in settings
3. Connect USB to your PC
4. Run Python program -> webcam window will open
5. Test the project! 

## Credits
This project is based on the original work by [@vbookshelf](https://github.com/vbookshelf).
