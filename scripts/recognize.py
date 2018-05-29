import sys
import datetime
import os
import cv2 as cv
import numpy as np
import pickle
import logger as l
import requests
import json


#import pickle as pickle

url = "http://127.0.0.1:5000"

face_recognizer = cv.face.LBPHFaceRecognizer_create()
cascade_path = '../data/opencv-files/lbpcascade_frontalface.xml'

def detect_face(img):  
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_cascade = cv.CascadeClassifier(cascade_path)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    print ('[ INFO ] Found {0} faces!'.format(len(faces)))
    l.log('Found {0} faces!'.format(len(faces)))

    if(len(faces) == 0):
        return None, None

    (x, y, w, h) = faces[0]
    return gray[y:y+w, x:x+h], faces[0]

def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)
    faces = []
    labels = []
    
    for dir_name in dirs:
        if not dir_name.startswith("s"):
            continue
            
        label = int(dir_name.replace("s", ""))
        subject_dir_path = data_folder_path + "/" + dir_name 
        subject_images_names = os.listdir(subject_dir_path)
        print("[ DEBUG ]" + subject_dir_path)
        
        l.log(subject_dir_path, 1)

        for image_name in subject_images_names:
            print("[ DEBUG ]" + image_name)
            if image_name.startswith("."):
                continue

            image_path = subject_dir_path + "/" + image_name
            image = cv.imread(image_path)
            cv.imshow("Training on image...", cv.resize(image, (400, 500)))
            cv.waitKey(100)
            face, rect = detect_face(image)
            if face is not None:
                faces.append(face)
                labels.append(label)
            
    cv.destroyAllWindows()
    cv.waitKey(1)
    cv.destroyAllWindows()
    
    return faces, labels
 
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

def draw_text(img, text, x, y):
    cv.putText(img, text, (x, y), cv.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

def predict(test_img):
    img = test_img.copy()
    face, rect = detect_face(img)
    label, confidence = face_recognizer.predict(face)

    print ('[ DEBUG ] Confidence: {0}'.format(confidence))
    l.log('Confidence: {0}'.format(confidence), 1)

    if confidence < 43:
        label_text = subjects[label]
        post_data(subjects[label], str(datetime.datetime.now()))
        print ("[ INFO ] Matching!")
        l.log("Matching!")

    else:
        label_text = subjects[0]
        label=0
        post_data(subjects[0], str(datetime.datetime.now()))
        print ("[ INFO ] No match!")
        l.log("No match!")

    draw_rectangle(img, rect)
    draw_text(img, label_text, rect[0], rect[1]-5)
    
    return (img,label)

def read_data(img_path, cmd):
    global subjects
    subjects=[]

    with open("../data/data-files/data.txt", "r") as f:
        subjects = f.readlines()

    subjects = [str(el.strip()) for el in subjects]
    subjects.insert(0,"unknown")

    if cmd == "train":
        print("[ INFO ] Preparing data...")


        faces, labels = prepare_training_data("../data/training-data/")
    
        print ("[ INFO ] Data prepared")
        print ("[ INFO ] Saving to file...")
        with open("../data/pickle-files/objs.pkl", 'wb') as f:
            pickle.dump([faces, labels], f)
    
    print ("[ INFO ] Reading from file...")
    
    with open("../data/pickle-files/objs.pkl", 'rb') as f:  
        faces_read, labels_read = pickle.load(f)

    faces=faces_read
    labels=labels_read

    print ('[ INFO ] Total faces: {0}'.format(len(faces)))
    print ('[ INFO ] Total labels: {0}'.format(len(labels)))

    face_recognizer.train(faces_read, np.array(labels_read))

    print ("[ INFO ] Predicting images...")

    test_img1 = cv.imread(img_path)
    predicted_img1,i = predict(test_img1)
    
    print ("[ INFO ] Prediction complete!")
    

    return subjects[i]

def post_data(name, timestamp, location=0):
    t = str.split(timestamp, '.')
    urlpost = url + "/createEVNT"

    data = {'name' : name, 'timestamp' : t[0], 'location' : 0}
    d = json.dumps(data)
    print("[ DEBUG ] " + d)
    r = requests.post("http://127.0.0.1:5000/createEVNT", json=data)
    


if __name__ == '__main__':

    # detect_face("../data/s0/Calina1.jpg")
    # read_data("../data/test/test.jpg", "train")

    if len(sys.argv) == 3:
        print ("[ INFO ] Running recognizer.py...")
        read_data(sys.argv[1], sys.argv[2])

    else:
        print ("[ ERROR ] Invalid arguments.\n[ INFO ] Usage: <scriptname> <test_img_path> <train | test>")
