# Privaseer
#### Home surveillance system with face recognition. 

### About

Privaseer is a home surveillance system that detects and recognizes the face of a subject and alerts the user on a mobile application. The purpose of the system is to prevent crimes.

### System overview

The system runs on a RaspberryPi board (running Raspbian operating system) that is connected to a camera. Through the camera, the module collects the information and on motion detection it triggers the face recognition script. The server gets the processed data and saves it in the database. The SQLite database keeps the inserted data records. The application provides a visual interpretation of the data and keeps the user up to date with the events that occurred in realtime.


Hardware requirements:
* raspberry Pi board
* raspberry Pi camera connected with SODIMM

System requirements:
* OpenCV library
* Ionic 3 Framework for the mobile application
* Python Flask to send data to the mobile application



### Usage

The python module has two components: *capture.py* and *recognizer.py*.

*capture.py* component captures the video and sends data to recognizer when it detects motion. The script takes no arguments.

```
python ./capture.py
```

*recognizer.py* component takes data as input. It can either learn a face from the data or test if the input image has a face and if the face matches with any of the the known subjects faces.

```
python ./recognizer.py <path_to_file> <test/train>
```
To configure the server, export the path to the app:

```
export FLASK_APP=<path_to_server>
```

Then init the database:

```
flask init
```

Run the server:

```
flask run
```
For more information check [Flask documentation](http://flask.palletsprojects.com/en/1.1.x/).


<p align="center">
  <img width="400" height="400" src="https://i.imgur.com/1U4Hikx.png" alt="Privaseer Logo"/>
</p>
