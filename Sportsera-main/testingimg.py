import os
import sys
import face_recognition as fc
import cv2 
import sqlite3

# initialize the camera
   # frame captured without any error
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#MEDIA_ROOT =os.path.join(BASE_DIR,'pages')

def dbprocess():
    conn = sqlite3.connect('lite.db')
    cursor = conn.execute("SELECT *  FROM USER WHERE username=?",(sys.argv[1],))
    records = cursor.fetchall()
    if conn:
        conn.close()
    return len(records)
def main():
    cam = cv2.VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    #loc = "C:/Users/anujjain/Pictures/Camera Roll/Niket.jpg" # signup image
    loc = os.path.join(os.path.dirname(os.path.realpath(__file__)),"filename.jpg")
    #loc = "C:/node-course/sports-arena-booking-system/image.png"
    if s:
        cv2.namedWindow("cam-test")
        cv2.imshow("cam-test",img)
        #cv2.waitKey(0)
        cv2.destroyWindow("cam-test")
        cv2.imwrite("filename.jpg",img)
     #   print(img)
        face_1_image = fc.load_image_file(loc)
        face_1_face_encoding = fc.face_encodings(face_1_image)[0]

        small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = fc.face_locations(rgb_small_frame)
        face_encodings = fc.face_encodings(rgb_small_frame, face_locations)

        check=fc.compare_faces(face_1_face_encoding, face_encodings)
        dbb = dbprocess()
        #print(check)
        if check[0] and dbb!=0:
            print(1)
            #sys.stdout.flush()
        else:
            print(0)
            #sys.stdout.flush()
#start process
if __name__ == '__main__':
    main()
