import os
import io
from google.cloud import vision
import json
import re
import pandas as pd


def date_cleaning(date_value):
    
    date_value = date_value.rstrip()
    date_value = date_value.lstrip()
    date_value = date_value.replace('l', '/')
    date_value = date_value.replace('L', '/')
    date_value = date_value.replace('I', '/')
    date_value = date_value.replace('i', '/')
    date_value = date_value.replace('|', '/')
    date_value = date_value.replace('\"', '/1')
    date_value = date_value.replace(" ", "")
    date_value = date_value.split(':')[-1]
    return date_value


def prescriptionn(path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']= os.path.join(os.path.dirname(os.path.realpath(__file__)),"project-azyo-dd74724c37c6.json")
    #os.environ['GOOGLE_APPLICATION_CREDENTIALS']= os.path.join(os.path.dirname(os.path.realpath(__file__)),"cskaa-jsrw-7ea10f0844f3.json")
    #os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'/home/shreyanshsatvik/Documents/python_env/VisionAPI/cskaa-jsrw-7ea10f0844f3.json'
    #GOOGLE_APPLICATION_CREDENTIALS = "/home/shreyanshsatvik/Documents/python_env/VisionAPI/cskaa-jsrw-7ea10f0844f3.json"
    
    client = vision.ImageAnnotatorClient()

    #path = "/home/shreyanshsatvik/Downloads/dl_new.png"
    d= os.path.dirname(os.path.realpath(__file__))
    #path = d +'/docs/'+path


    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    str1 = ""
    texts = response.text_annotations
    for text in texts:
        #print(text.description)
        str1 += text.description
        break
    print("Raw Data",str1)
    res = [] 
    for sub in str1.split('\n'): 
        if ':' in sub: 
            res.append(map(str.strip, sub.split(':', 1))) 
    res = dict(res) 

    # printing result  
    print("The converted dictionary is : " + str(res))
 
    #########################################POST_PROCESSING_TEXT###########################################

    

    
    text1 = []
    text2 = []
    

    lines = str1.split('\n')
    #print(lines)
    for lin in lines:
        s = lin.strip()
        s = lin.replace('\n','')
        s = s.rstrip()
        s = s.lstrip()
        text1.append(s)
    text1 = list(filter(None, text1))
    print(text1)


    date = []
    Patient = None
    doctor = None

    def finddate(test_str):
        check = []
        for test in test_str:
            for l in test.split():
                if(re.search(r'\d{2}/\d{2}/\d{4}', str(l)) or re.search(r'\d{2}-\d{2}-\d{4}',str(l) )):
                    check.append(l)
                    test_str.remove(test)

        return check
    
    date = finddate(text1)
    
    for text in text1:
        text = str(text).replace("-"," ")
    
    print(text1)
    print(date)


    medicine_list = ['MEDICINE','MEDICINES','MEDICINES-','medicine','Medicine']

    index = 0
    for text in text1:
        a = text.split()
        for k in a:
            if k in medicine_list:
                index = text1.index(text)
                break
    print("Index",index)
    medicine_list = text1[index+1:]
    print(medicine_list)

    name_list = ['NAME','NAME:','name','NAME!',"NAME-","NAME -"]
    name_index = 1
    for text in text1:
        a = text.split()
        for k in a:
            if k in name_list:
                name_index = text1.index(text)
                break
    
    print(name_index)

    doctor_list = ['DOCTOR','dotor','DOCTOR!','DOCTOR:','DOCTOR-','DOCTOR -']

    doc_index = 1
    for text in text1:
        a = text.split()
        for k in a:
            if k in doctor_list:
                doc_index = text1.index(text)
                break

    Patient = ""
    for i in range(name_index+1,doc_index):
        Patient += text1[i]+" "
    print(Patient)
    doctor = ""
    for i in range(doc_index+1,index):
        doctor += text1[i]+" "
    print(doctor)

    return Patient, doctor , date, medicine_list

    
prescriptionn("/home/shreyanshsatvik/GIT/Centralized-Healtcare-System/face_recognition copy/prescriptions/pres1.jpeg")