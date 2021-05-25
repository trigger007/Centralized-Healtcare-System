import face_recognition
import cv2
import numpy as np
import os
import glob


def train():

    faces_encodings = []
    faces_names = []

    cur_direc = os.getcwd()

    #path = os.path.join(cur_direc,'face_recognition_copy/data/')
    #path=('/face_recognition_copy/data')
    #f=os.listdir("face_recognition copy/data") 
    f = os.listdir(cur_direc+"/data")
    print(f)
    #list_of_files = [f for f in (glob.glob(path+'*.jpg') and (glob.glob(path+'*.jpeg')))]
    #number_files = len(list_of_files)
    #names = list_of_files.copy()
    path="face_recognition copy/data/"
    path = cur_direc+"/data/"
    #print(path)
    # print(number_files)
    # print(list_of_files)
    for i in range(len(f)):
        a = face_recognition.load_image_file(path+f[i])
        b = face_recognition.face_encodings(a)[0]
        faces_encodings.append(b)
    # Create array of known names
        # names[i] = names[i].replace(cur_direc, "")  
        # print(names[i])
        # faces_names.append(names[i])
    print("2",len(faces_encodings))
    print("1",f)
    face_locations = []
    #face_encodings = []
    #face_names = []
    process_this_frame = True
    name = ""
    path1 = cur_direc+'/face_recognition copy/temp/temp.jpeg'
    print(path1,type(cur_direc))
    #video_capture = cv2.VideoCapture(0)
    
    #frame = cv2. imread(path1)
    frame1=face_recognition.load_image_file("/home/shreyanshsatvik/GIT/Centralized-Healtcare-System/face_recognition copy/temp/temp.jpeg")
    frame= face_recognition.face_encodings(frame1)[0]
    #print(frame)
    # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # rgb_small_frame = small_frame[:, :, ::-1]
    ans=[]
    if True:
        print("yoo")
        #face_names = []
        for i in range(len(faces_encodings)):
            print("hiii")
            matches = face_recognition.compare_faces (frame, [faces_encodings[i]])
            print("matches",matches,f[i])
            name = "Unknown"
            face_distances = face_recognition.face_distance( frame, [faces_encodings[i]])
            l=[]
            l.append(face_distances)
            l.append(f[i])
            ans.append(l)
            print(face_distances,f[i])
        ans=sorted(ans,key=lambda x:x[0])  
        name= ans[0][1]
    '''
            face_names.append(name)

    process_this_frame = not process_this_frame
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
    # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    # Input text label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    # Display the resulting image
    
    cv2.imshow('Video', frame)
        Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    '''
    print("name",name)
    return name


