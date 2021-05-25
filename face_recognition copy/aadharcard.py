import os
import io
from google.cloud import vision
import json
import re
import pandas as pd
#from google.cloud.vision import types 


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

def aadhar_card_front(path,path1):
    #os.environ['GOOGLE_APPLICATION_CREDENTIALS']= os.path.join(os.path.dirname(os.path.realpath(__file__)),"project-azyo-dd74724c37c6.json")
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']= os.path.join(os.path.dirname(os.path.realpath(__file__)),"cskaa-jsrw-7ea10f0844f3.json")
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
    """
    res = dict(text.split(":") for text in texts.split("/n"))
    print(str(res))

    for text in texts:

        #print('\n"{}"'.format(text.description))
        str1.join('\n"{}"'.format(text.description))
        print(str1)

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    """


    #########################################POST_PROCESSING_TEXT###########################################

    import re

    License_no = None
    name = None
    father = None
    Address = None
    dob = None
    ed = None
    Vehicle_Class = None
    PIN = None
    doi = None
    phone_number=[]
    text0 = []
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

    # to remove any text read from the image file which lies before the line 'Transport Department'

    lineno = 0  # to start from the first line of the text file.

    for wordline in text1:
        xx = wordline.split('\n')
        if ([w for w in xx if re.search('(GOVERNMENT OF INDIA @|DEPART|GOVERNMENT|TRANSP|GOW|GOVT|INDIE|indie|GOVERNMENT|OVERNMENT|VERNMENT|DEPARTMENT|EPARTMENT|PARTMENT|ARTMENT|INDIA|NDIA|India|Indie)$', w)]):
            text1 = list(text1)
            lineno = text1.index(wordline)
            break

    # text1 = list(text1)
    text0 = text1[lineno+1:]
    text00= []
    name_list =[]
    print("Text-0",text0)  # Contains all the relevant extracted text in form of a list - uncomment to check
    def finddate(test_str):
        check = []
        for test in test_str:
            for l in test.split():
                if(re.search(r'\d{2}/\d{2}/\d{4}', str(l)) or re.search(r'\d{2}-\d{2}-\d{4}',str(l) )):
                    check.append(l)
                    test_str.remove(test)

        return check
    
    def findnumber(test_str):
        check = []
        for test in test_str:
            for l in test.split():
                if(re.search(r'\d{10}', str(l))):
                    check.append(l)
                    test_str.remove(test)
        return check
    

    date_list = finddate(text0)
    phone_number = findnumber(text0)
    print("Phone No", phone_number)
    print("Date List ", date_list)
    for text in text0:
        text = re.sub('[^a-zA-Z0-9 ]','', str(text))
        text=str(text).strip()
        if(text!=''):
            text00.append(text)

        """
        if(str(text).isalpha() or str(text).isspace()):
            name_list.append(text)
        else:
            text00.append(text)
        """
    gender_list = ['MALE','Male','male','FEMALE','female','Female']

    gender = None
    for text in text00:
        res_list = re.findall('[A-Z][^A-Z]*', str(text))
        if(res_list):
            for tex in res_list:
                if tex in gender_list:
                    gender = tex
                    text00.remove(text)
                    break
                else:
                    if text in gender_list:
                        gender = text
                        text00.remove(text)
                        break

    
    print("Gender :",gender)



    



    print(text00)
    text00 = list(set(text00))
    num_list = []
    for tes in text00:
        for test in tes.split(' '):
            print(test.isnumeric())
            if(str(test).isnumeric()):
                num_list.append(tes)
                
                
    num_list = list(set(num_list)) 
    name_list = []
    for a in text00:
        if a not in num_list:
            name_list.append(a)    
    father_list = ["Father",'father']

    father = None
    for text in name_list:
        tex = text.split()
        for k in tex:
            if k in father_list:
                father = re.sub(r'^.*?Father', '', text)
                father = re.sub(r'^.*?father', '', father)
                name_list.remove(text)
                break

    print("Father",father)
    print(text00)
    print(num_list)
    print(name_list)
    


    

    name = name_list[0]
    if(date_list==[]):
        dob = None
    else:
        dob= date_list[0]
    father = father
    gender= gender
    aadhar_number = None
    for i in num_list:
        i = str(i).replace(" ","")
        if(re.search(r'\d{12}', str(i))):
            aadhar_number = i
    if(aadhar_number==None):
        aadhar_number = num_list[0]
    phone_number = phone_number



    def aadhar_card_complete(path,path1):
        #os.environ['GOOGLE_APPLICATION_CREDENTIALS']= os.path.join(os.path.dirname(os.path.realpath(__file__)),"project-azyo-dd74724c37c6.json")
        os.environ['GOOGLE_APPLICATION_CREDENTIALS']= os.path.join(os.path.dirname(os.path.realpath(__file__)),"cskaa-jsrw-7ea10f0844f3.json")
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
        """
        res = dict(text.split(":") for text in texts.split("/n"))
        print(str(res))

        for text in texts:

            #print('\n"{}"'.format(text.description))
            str1.join('\n"{}"'.format(text.description))
            print(str1)

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                        for vertex in text.bounding_poly.vertices])

            print('bounds: {}'.format(','.join(vertices)))

        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
        """


        #########################################POST_PROCESSING_TEXT###########################################

        import re

        License_no = None
        name = None
        father = None
        Address = None
        dob = None
        ed = None
        Vehicle_Class = None
        PIN = None
        doi = None
        phone_number=[]
        text0 = []
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
        lineno = 0  # to start from the first line of the text file.

        for wordline in text1:
            xx = wordline.split('\n')
            if ([w for w in xx if re.search('(GOVERNMENT OF INDIA @|DEPART|GOVERNMENT|TRANSP|GOW|GOVT|INDIE|indie|GOVERNMENT|OVERNMENT|VERNMENT|DEPARTMENT|EPARTMENT|PARTMENT|ARTMENT|INDIA|NDIA|India|Indie)$', w)]):
                text1 = list(text1)
                lineno = text1.index(wordline)
                break

        # text1 = list(text1)
        text0 = text1[lineno+1:]
        text00= []
        name_list =[]
        print("Text-0",text0) 


        def check_long(text0):
            check_list = ['GOVERNMENT','INDIA','GOVERNMENT OF INDIA','NDIA','government','india','INDI','1NDIA','1ND1A','Government of India','Government','India','Enrolment','Enrolment No']
            check = False
            for text in text0:
                k  = str(text).strip()
                if k in check_list:
                    check= True
                    break
                
            return check

        ch_long = check_long(text0)

        print(ch_long)


        if(check_long):
            num_list = []
            for tes in text0:
                for test in tes.split(' '):
                    if(str(test).isnumeric()):
                        num_list.append(tes)
                        
                    
                        
            num_list = list(set(num_list))

            print("Num-List",num_list)


            def finddate(test_str):
                check = []
                for test in test_str:
                    for l in test.split():
                        if(re.search(r'\d{2}/\d{2}/\d{4}', str(l)) or re.search(r'\d{2}-\d{2}-\d{4}',str(l) )):
                            check.append(l)
                            test_str.remove(test)

                return check
            

            date_list = finddate(text0)

            if(date_list==[]):
                dob = None
            else:
                dob= date_list[0]
                dob=re.sub(r'^.*?:', '', dob)
            
            print("DOB",dob)

            
            aadhar_number = []
            for r in num_list:
                r = r.replace(" ","")
                if(re.search(r'\d{12}', str(r))):
                    aadhar_number.append(r)
                    break
            
            print("Aadhar Number",aadhar_number)

            text00=[]

        

            
            for text in text0:
                text = str(text).replace("-"," ")
                text = re.sub('[^a-zA-Z0-9, ]','', str(text))
                text=str(text).strip()
                if(text!=''):
                    text00.append(text)

            print("Text00",text00)

            str_to = ['To','TO','to','T0']
            
            for text in text00:
                x = text.split()
                for k in x:
                    if k in str_to:
                        index_of = text00.index(text)
                        break


            name = text00[index_of+1]
            print("Name",name)


            str_co = ['CO','Co','SO','So','S0','C0','DO','D0','Do']


            phone = None
            for r in num_list:
                k = r.replace(" ","")
                if(re.search(r'\d{10}', str(k))):
                    phone = str(r)
                    break
                
            print("Phone",phone)

            father = None
            for text in text00:
                x = text.split()
                for k in x:
                    if k in str_co:
                        father = text.replace(k,'')
                        index_father = text00.index(text)

            if father==None:
                index_father = index_of+1

            for text in text00:
                if str(text) == phone:
                    print("text found",text)
                    index_before = text00.index(text)


            address=''

            for i in range(index_father+1,index_before):
                address += text00[i]
                

            print(address)
            
            
            
            print("Father",father)
            print("index of father",index_father)
            #print("Final- index",final_index)



            gender = None
            gender_list = ['MALE','Male','male','FEMALE','female','Female']

            for text in text1:
                text = text.split()
                for tex in text:
                    te = tex.split('/')
                    for t in te:
                        if t in gender_list:
                            gender = t
                            break


            print("Gender",gender)


            region = "India"




            return name , father, address, aadhar_number, gender, dob, region
        
        
        
    
    
    
    
    
    
    def second_side(path1):
        d1= os.path.dirname(os.path.realpath(__file__))
        #path1 = d1 +'/docs/'+path


        text0 = []
        text1 = []
        text2 = []
        father = []


        with io.open(path1, 'rb') as image_file:
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



        import re


        Address = None
        

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
        ttt = text1

        # to remove any text read from the image file which lies before the line 'Transport Department'

        lineno = 0  # to start from the first line of the text file.

        for wordline in text1:
            xx = wordline.split('\n')
            if ([w for w in xx if re.search(r'\d{6}',w)]):
                text1 = list(text1)
                lineno = text1.index(wordline)
                break

        # text1 = list(text1)
        text0 = text1[lineno+1:]
        text00= []
        name_list =[]
        father =[]

        print("Text-0",text0) 


        address_list = ['C/O','C/0','D/O','S/0','S/O','D/0','C/O','C/O:']

        after_father = []
        for text in text0:
            a = text.split()
            print("A",a)
            for k in a:
                if(k in address_list):
                    index = text0.index(text)
                    text = re.sub(r'^.*?C/O:','', str(text))
                    text = re.sub(r'^.*?S/O','', str(text))
                    #print("test",text)
                    text = text.split(',')
                    after_father = text[1]
                    text = text[0]


            

                    if(text!=''):
                        text.split(',')
                        father.append(text)
                        break
                    else:
                        father.append(text)
                        break


                    
                    
                
        print("Father",father)
        print("after_Father",after_father)
        #print(index)


        for wordline in text0:
            xx = wordline.split('\n')
            if ([w for w in xx if re.search(r'\d{6}',w)]):
                final_index=text0.index(wordline)
                break

        #print("final-index",final_index)

        address=''

        for i in range(index+1,final_index+1):
            address += text0[i]
            if(after_father!=''):
                address = after_father+address

        print(address)


        return father,address



        """

        text00=[]
        for text in text1:
            text = re.sub('[^a-zA-Z0-9,]','', str(text))
            text=str(text).strip()
            if(text!=''):
                text00.append(text)

        

        text001=[]

        for text in ttt:
            for te in list(str(text)):
                if(re.findall('[\u0900-\u097F]',str(te))):
                    print("Te",te)
                    ttt.remove(text)
                    break

        print("check-again",ttt)


        








        
        for text in text1:
            k = text.split()
            for l in k:
                if(re.findall('[^a-zA-Z0-9]',str(l))):
                    text001.append(l)
                else:
                    text1.remove(text)
                    break
        
        
        def seems_like_english(word):
            for letter in word:
                if ord(letter) > 127:
                    return False
                return True
        
        total_words = str1.split()
        english_words = []
        for text in text1:
            words = text.split(" ")
            # output = []
            for wor in words:
                if (seems_like_english(wor)==False):
                    text1.remove(text)
                    break

                    # output.append(line)
                    
                    
        

        print("text 1 f",text1)

        text01=[]
        for text in text1:

            if(re.findall('[^a-zA-Z0-9,]',str(text))):
                text01.append(text)
        
        print(text01)


        text000 =[]
        for text in text00:
            if text not in text01:
                text000.append(text)

        print("Text000",text000)


        


        for text in text00:
            a = text.split()
            for k in a:
                if(k in address_list):
                    text = re.sub(r'^.*?CO','', str(text))
                    text = re.sub(r'^.*?SO','', str(text))
                    text = text.strip()
                    j = text.strip(',')
                    text = j[1:]
                    if(text!=''):
                        text.split(',')
                        father.append(text)
                        break
                    
                    
                
        print("Father",father)



        for text in text0:
            d = text.split()
            if d in address_list:
                text00 = text0[text:]
                break
                
        print(text00)

        



    
       """



        

    def detect_text(img):
        client = vision.ImageAnnotatorClient()
        with io.open(img, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = client.text_detection(image=image)

        #print(response)
        texts = response.text_annotations
        df = pd.DataFrame(columns=['locale', 'description'])
        for text in texts:
            df = df.append(
                dict(
                    locale=text.locale,
                    description=text.description
                ),
                ignore_index=True
            )
        #print(response.text)
        return df['description'][0]


    def seems_like_english(word):
        for letter in word:
            if ord(letter) > 127:
                return False
            return True

    def formatting( english_words):
        # print(english_words)
        gender = []
        name = []
        dob = []
        son_of = []
        region = []
        uid = []
        address = []

        try:
            # For Gender Extraction
            for i in range(len(english_words)):
                english_words[i] = str(english_words[i])
                m = re.search(r'Male', english_words[i]) or re.search(r'MALE', english_words[i]) or re.search(r'/ Male', english_words[i]) or re.search(r'/ MALE', english_words[i])
                f = re.search(r'Female', english_words[i]) or re.search(r'FEMALE', english_words[i]) or re.search(r'/ Female', english_words[i])
                if m:
                    gender.append(english_words[i][m.start():m.end()])
                elif f:
                    gender.append(english_words[i][f.start():f.end()])

            # print(gender)
            gender = "".join(gender)
        except:
            gender = "".join(gender)

        try:
            # For Region Extraction
            for i in range(len(english_words)):
                r1 = re.search(r'India', english_words[i]) or re.search(r'india', english_words[i]) or re.search(r'INDIA', english_words[i])
                r2 = re.search(r'USA', english_words[i]) or re.search(r'usa', english_words[i]) or re.search(r'Usa', english_words[i])
                r3 = re.search(r'Canada', english_words[i]) or re.search(r'canada', english_words[i]) or re.search(r'CANADA', english_words[i])
                if r1:
                    region.append(english_words[i][r1.start():r1.end()])
                    break
                elif r2:
                    region.append(english_words[i][r2.start():r2.end()])
                    break
                elif r3:
                    region.append(english_words[i][r3.start():r3.end()])
                    break

            if (len(region) > 0):
                english_words.remove(region[0])
            region = ''.join(region[0])
        except:
            region = "".join((region))

        try:

            # For DOB extraction

            for j in range(len(english_words)):
                res1 = re.search(r'\d{2}/\d{2}/\d{4}', english_words[j])
                res2 = re.search(r'BIRTH', english_words[j]) or re.search(r'Birth', english_words[j]) or re.search(r'YOB', english_words[j]) or re.search('yob', english_words[j])
                if res1:
                    dob.append(english_words[j][res1.start():res1.end()])
                elif res2:
                    dob.append(english_words[j+2][res2.start():res2.end()])

            if (len(dob) > 0):
                english_words.remove(dob[0])
            dob = ''.join(dob)
        except:
            dob = " ".join(dob)


        # For UID extraction

        try:
            num1 = []
            for l in range(len(english_words)):
                res2 = re .search(r'\d{4}', english_words[l])
                if res2:
                    num1.append(english_words[l])
                    break
            if (len(num1) > 0):
                english_words.remove(num1[0])

            num2 = []
            for l in range(len(english_words)):
                res3 = re.search(r'\d{4}', english_words[l])
                if res3:
                    num2.append(english_words[l])
                    break
            if (len(num2) > 0):
                english_words.remove(num2[0])

            num3 = []
            for l in range(len(english_words)):
                res4 = re.search(r'\d{4}', english_words[l])
                if res4:
                    num3.append(english_words[l])
                    break
            if (len(num3) > 0):
                english_words.remove(num3[0])
            # print(num1)
            # print(num2)
            # print(num3)
            com_num = num1 + num2 + num3
            com_num = ''.join(com_num)
        except:
            uid = " ".join(uid)

        for i in range(len(english_words)):
            english_words[i] = re.sub('[\W_]+', '', english_words[i])


        try:
            # For Name Extraction

            for i in english_words:
                res5 = re.search(r'DOB', i)
                res6 = re.search(r'Father', i) or re.search(r'FATHER', i)
                res7 = re.search(r'Year', i)
                if res5 :
                    index6 = english_words.index(i)
                    break
                elif res6:
                    index6 = english_words.index(i)
                    # index14 = english_words.index(i)
                    break
                elif res7:
                    index6 = english_words.index(i)
                    break


            for i in range(2, index6):
                name.append(english_words[i])

            #print(name)
            name = " ".join(name)
        except:
            name = " ".join(name)

        actual_add = " "
        actual_father = " "
        try:
            # Father name and Address
            for i in english_words:
                res15 = re.search(r'Father', i) or re.search(r'daughter', i) or re.search(r'Daughter', i) or re.search(r'husband', i) or re.search(r'Husband', i) or re.search(r'HUSBAND', i)
                index16 = english_words.index(i)
                if res15:
                    for m in english_words:
                        res8 = re.search(r'DOB', m)
                        res9 = re.search(r'Year', m)
                        if res8 :
                            index7 = english_words.index(m)
                            break
                        elif res9:
                            index7 = english_words.index(m)
                            break

                    for p in range(index16+2, index7):
                        son_of.append(english_words[p])

                    # print(son_of)
                    for c in range(len(son_of)):
                        if(len(son_of) == 3):
                            break
                        son_of.pop()

                    # #print(son_of[-1].capitalize())
                    # if(len(son_of) > 2):
                    #     if (son_of[-1].capitalize()) != (name[-1].capitalize()):
                    #         son_of.pop()

                    actual_father = ''
                    for h in son_of:
                        actual_father = actual_father + h + " "

                    for b in english_words:
                        res10 = re.search(r'Address', b) or re.search(r'ADDRESS', b)
                        res11 = re.search(r'\d{6}', b)
                        if res10:
                            index8 = english_words.index(b)
                        if res11:
                            index9 = english_words.index(b)

                    for q in range(index8+1, index9+1):
                        address.append(english_words[q])

                    actual_add = ''
                    for j in address:
                        actual_add = actual_add + j + " "
                    break

            if res15 == None:
                for i in english_words:
                    res12 = re.search(r'SO', i) or re.search(r'so', i) or re.search(r'So', i) or re.search(r'WO', i) or re.search(r'wo', i) or re.search(r'Wo', i) or re.search(r'DO', i) or re.search(r'do', i) or re.search(r'Do', i)
                    if res12:
                        address = []

                        for i in english_words:
                            res13 = re.search(r'Address', i) or re.search(r'ADDRESS', i)
                            if res13:
                                index11 = english_words.index(i)

                        for i in range(index11+2, index11+6):
                            son_of.append(english_words[i])
                        #
                        # for i in range(index8+3, index8+5):
                        #     son_of.append(english_words[i])

                        #print(son_of)
                        #
                        # print(son_of)
                        for z in son_of:
                            if(len(z) == 2):
                                son_of.remove(z)

                        for i in range(len(son_of)):
                            if(len(son_of) == 3 or len(son_of) == 2):
                                break
                            son_of.pop()

                        if(len(son_of) > 2):
                            if son_of[2] != name[1]:
                                son_of.pop()


                        actual_father = ''
                        for i in son_of:
                            actual_father = actual_father + i + " "

                        for i in english_words:
                            # res10 = re.search(r'Address', i) or re.search(r'ADDRESS', i)
                            res11 = re.search(r'\d{6}', i)
                            # if res10:
                            #     index8 = english_words.index(i)
                            if res11:
                                index14 = english_words.index(i)

                        for i in range((index11+5), index14+1):
                            address.append(english_words[i])

                        actual_add = ''
                        for i in address:
                            actual_add = actual_add + i + " "
                        break
        except:
            actual_add = " ".join(actual_add)
            actual_father = " ".join(actual_father)
        return actual_father,  actual_add

         

    

    
    lines1 = detect_text(path)
    list_of_words_1 = lines1.split()
    lines2 = detect_text(path1)
    list_of_words_2 = lines2.split()

    com_list = list_of_words_1 + list_of_words_2

    english_words = []

    for line in com_list:
        words = line.split(" ")
        # output = []
        if seems_like_english(line):
            # output.append(line)
            english_words.append(line)

    # print(english_words)
    #son_of, addr = formatting(english_words)

    #print("Son of",son_of)
    #print("Address---",addr)

    d11= os.path.dirname(os.path.realpath(__file__))
    #path1 = d11 +'/docs/'+path


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

    text0 = []
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
    lineno = 0  # to start from the first line of the text file.

    for wordline in text1:
        xx = wordline.split('\n')
        if ([w for w in xx if re.search('(GOVERNMENT OF INDIA @|DEPART|GOVERNMENT|TRANSP|GOW|GOVT|INDIE|indie|GOVERNMENT|OVERNMENT|VERNMENT|DEPARTMENT|EPARTMENT|PARTMENT|ARTMENT|INDIA|NDIA|India|Indie)$', w)]):
            text1 = list(text1)
            lineno = text1.index(wordline)
            break

    # text1 = list(text1)
    text0 = text1[lineno+1:]
    text00= []
    name_list =[]
    print("Text-0",text0) 


    def check_long(text0):
        check_list = ['GOVERNMENT','INDIA','GOVERNMENT OF INDIA','NDIA','government','india','INDI','1NDIA','1ND1A','Government of India','Government','India','Enrolment','Enrolment No']
        check = False
        for text in text0:
            k  = str(text).strip()
            if k in check_list:
                check= True
                break
            
        return check

    ch_long = check_long(text0)

    print(ch_long)


   



    with io.open(path1, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    str11 = ""
    texts = response.text_annotations
    for text in texts:
        #print(text.description)
        str11 += text.description
        break
    print("Raw Data",str11)
    aadhar_list = ['AADHAAR','ADHAAR','AADHAR','aadhaar','adhar','ADHAR']
    aadhar_back = False
    sttr = str11.split()
    for st in sttr:
        if(st in aadhar_list):
            aadhar_back = True


    if(ch_long):
        name , father, addr, aadhar_number, gender, dob, region = aadhar_card_complete(path,path1)

    else:        
        if(aadhar_back==True):
            son_of, addr = second_side(path1)
        elif(phone_number!=[]):
            son_of, addr = second_side(path1)
        
        else:
            son_of, addr = formatting(english_words)
            print("Son of",son_of)
            print("Address---",addr)


        if(father==None):
            father = son_of

        region = "India"


        print("Text-0",text0)


    return name , father, addr, aadhar_number, gender, dob, region




def json_convert1(path,path1):


    name , father, addr, aadhar_number, gender, dob, region = aadhar_card_front(path,path1)
        # print(ln)
        # print(doi)
        # print(cls)
        # print(doe)
        # print(dob)
        # print(name)
        # print(addr)
        #
    attr = ['Name', 'C/O', 'Address', 'UID', 'gender', 'DOB', 'Region']

    final = []
    final.append(name)
    final.append(father)
    final.append(addr)
    final.append(aadhar_number)
    final.append(gender)
    final.append(dob)
    final.append(region)
    #final.append(doe)

    # print(final)
    obj = {
        'fields_detected': [],
        'field_values': []
    }

    for a in attr:
        obj['fields_detected'].append({'value': a})

    for f in final:
        # print(f)
        obj['field_values'].append({'value': f})

    return obj






        

    #second_side(path1)

#aadhar_card_front('/home/shreyanshsatvik/Downloads/Shreyansh_addhar_front.jpeg','/home/shreyanshsatvik/Downloads/Shreyansh_aadhar_back.jpeg')WhatsApp Image 2021-02-16 at 03.08.59.jpeg
#aadhar_card_front('/home/shreyanshsatvik/Downloads/aadhar/radhika_aadhar_fronts.jpeg')
#aadhar_card_front('/home/shreyanshsatvik/Downloads/aadhar/tanuj_aadhar_front.jpeg','/home/shreyanshsatvik/Downloads/aadhar/tanuj_aadhar_back.jpeg')
#aadhar_card_front('/home/shreyanshsatvik/Downloads/WhatsApp Image 2021-02-13 at 22.10.48.jpeg','/home/shreyanshsatvik/Downloads/Shreyansh_aadhar_back.jpeg')