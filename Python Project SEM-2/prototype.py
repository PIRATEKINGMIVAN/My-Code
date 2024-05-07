from flask import Flask, request, send_from_directory
from twilio.twiml.messaging_response import MessagingResponse
import csv
import re

app = Flask(__name__)
msgs={}
curnum=''
currenthandle = []

class PersonalAssistant:
    def __init__(self):
        pass

    @staticmethod
    def handle_message(msgs,currenthandle,curnum): #HANDLES MESSAGES RECIEVED
        try:
            if currenthandle[-1].lower() == 'hi' or currenthandle[-1].lower() == 'hello':
                return PersonalAssistant.welcome_message()
            
            if currenthandle[-2].lower() == 'hi' or currenthandle[-1].lower() == 'hello':
                msgs[curnum].append(curnum)
                return email()
            
            
            if currenthandle[-4].lower() == 'hi' or currenthandle[-4].lower() == 'hello':
                if validate_email(currenthandle[-1]):
                    return datarepeat()
                else:
                    msgs[curnum].pop()
                    return 'Please enter a valid email address'
                
            elif currenthandle[-1].lower() == 'help':
                return 'Choose an option: \n>1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n'
            
            elif currenthandle[-1].lower() == 'brochure':
                return send_pdf()
        
            elif currenthandle[-1].lower() == 'admission' or currenthandle[-1]=='1':
                return admission()
        
            elif (currenthandle[-1].lower() == 'btech' and currenthandle[-2].lower() == 'admission') or currenthandle[-1]=='6':
                return btechFees()

        
            elif (currenthandle[-1].lower() == 'diploma' and currenthandle[-2].lower() == 'admission') or currenthandle[-1]=='7':
                return diplomaFees()

            elif (currenthandle[-1].lower() == 'bca' and currenthandle[-2].lower() == 'admission') or currenthandle[-1]=='8':
                return bcaFees()

            elif currenthandle[-1].lower() == 'academics' or currenthandle[-1]=='2':
                return academics()
            elif (currenthandle[-1].lower() == 'btech' and currenthandle[-2].lower() == 'academics') or currenthandle[-1]=='9':
                return btechsub()
            elif (currenthandle[-1].lower() == 'diploma' and currenthandle[-2].lower() == 'academics') or currenthandle[-1]=='10':
                return diplomasub()
            elif (currenthandle[-1].lower() == 'bca' and currenthandle[-2].lower() == 'academics') or currenthandle[-1]=='11':
                return bcasub()

            elif currenthandle[-1].lower() == 'exam' or currenthandle[-1].lower() == 'exams' or currenthandle[-1]=='3':
                return exams()

            elif currenthandle[-1].lower() == 'transport' or currenthandle[-1]=='4':
                return transport()
            elif currenthandle[-1].lower() == 'vadodara' or currenthandle[-1]=='12':
                return vad()
            elif currenthandle[-1].lower() == 'halol' or currenthandle[-1]=='13':
                return hal()
            elif currenthandle[-1].lower() == 'godhra' or currenthandle[-1]=='14':
                return god()
        
            elif currenthandle[-1].lower() == 'exit' or currenthandle[-1]=='5':
                del msgs[curnum]
                return exits()
            elif currenthandle[-1].lower() == 'home' or currenthandle[-1]=='0':
                return home()
            
            else:
                return "I'm sorry, I can't help you with that! Please type 'help' to see all commands!"
        except Exception as e:
            print(e)
            return "Please Start the message with a Hi or Hello!"

    @staticmethod
    def welcome_message():
        return "*Welcome to Mivan and Harshili's API.\nPlease Enter your name:*" 

def email():
    return "Please enter your email:"
    
    
def admission():
    response = "You chose Admission.\nChoose an option:\n6.Btech\n7.Diploma\n8.BCA\n0.Home"
    return response

#BTECH
def btechsub():
    return """You Chose Btech :
    Btech is a 4-year course containing subjects:\n
    -Data structures and Algorithms\n
    -Database management (DBMS)\n
    -Operating system (OS)\n
    -Networking\n
    -Basic programming\n
    -Object-Oriented Programming (OOP)\n
    -Cryptography\n
    -Web development\n
    -Machine learning\n
    -Security, vulnerabilities, and cryptography")\n
    \n
    How else can we assist you with.\nChoose an option: \n->1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n
    """
def btechFees():
    return "You chose Fees.\nAnnual fee for Btech is 98000 excluding exam fees and transportation\n\nChoose an option: \n->1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n"

#DIPLOMA

def diplomaFees():
    return "You chose Fees.\nAnnual fee for Diploma is 87000 excluding exam fees and transportation\n\nChoose an option: \n>1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n"

def diplomasub():
    return """You chose Diploma:
    Diploma is a 3-year course containing subjects:\n
    - Mathematics\n
    - Physics\n
    - Chemistry\n
    - English\n
    - Computer Applications\n
    - Electronics\n
    - Communication Skills\n
    - Digital Electronics\n
    - Programming in C\n
    - Microcontrollers and Microprocessors\n\n
    How else can we assist you with.\nChoose an option: \n>1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n"""

#BCA
def bcaFees():
    return "You chose Fees.\nAnnual fee for BCA is 95000 excluding exam fees and transportation\n\nChoose an option: \n>1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n"

def academics():
    response = "You chose Academics.\nChoose an option:\n9.Btech\n10.Diploma\n11.BCA\n5.Exit"
    return response

def bcasub():
    return """You chose BCA:
    BCA is a 3-year undergraduate degree program in computer applications. The subjects typically include:\n
    - Mathematics\n
    - Computer Fundamentals and Programming\n
    - Data Structures and Algorithms\n
    - Database Management Systems\n
    - Object-Oriented Programming using Java/C++\n
    - Web Development\n
    - Operating Systems\n
    - Software Engineering\n
    - Computer Networks\n
    - Project Work\n\n
    How else can we assist you with.\nChoose an option: \n>1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n"""

def exams():
    return "External Exams for all Majors takes twice a year.\nThat is in December and in May. \n\nChoose an option: \n>1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n"

def transport():
    return "We have transport service available via bus. Please choose the city you belong:\n12.Vadodara\n13.Halol\n14.Godhra"
def vad():
    return "Annual fees of transportation from Vadodara will be Rs.21,000/- \n\nChoose an option: \n>1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n"
def hal():
    return "Annual fees of transportation from Halol will be Rs.18,000/- \n\nChoose an option: \n>1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n"
def god():
    return "Annual fees of transportation from Godhra will be Rs.26,000/- \n\nChoose an option: \n>1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n"


#COMMON SAMPLE PDF (ALL SUBJECTS)
def send_pdf():
    GOOD_BOY_URL = (
        "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1"
        "&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
    )
    return send_media(GOOD_BOY_URL)

def send_media(file_url):
    resp = MessagingResponse()
    msg=resp.message("Here's Your file!")
    msg.media(file_url)
    return str(resp)
        
def exits():
    return "We hope to see you again! Thank you for using our services!!"

def home():
    return "How can we assist you with.\nChoose an option: \n>1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n"

def data():
    global msgs
    global currenthandle
    add=[currenthandle[-3],currenthandle[-2],currenthandle[-1]]
    try:
        with open("data.csv","a",newline='') as f:
            wr=csv.writer(f)
            wr.writerow(add)
            print("Data added!!")
    except Exception as e:
        print(e)

def datarepeat():
    global msgs
    global currenthandle
    searchn = currenthandle[-3]
    searchc = currenthandle[-2]
    found = False
    try:
        with open("data.csv","a+") as f:
            f.seek(0)
            rd=csv.reader(f)
            for i in rd:
                if i[1] == searchc and i[0] == searchn:
                    found = True
                    break
                else:
                    continue
            if found==False:
                data()
                return f"Thank you for providing your info {currenthandle[-3]}! How can we assist you with.\nChoose an option: \n>1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n"
            else:
                return f"Welcome Back {currenthandle[-3]}.\n How can we assist you with.\nChoose an option: \n>1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n"
    except:
        return "How can we assist you with.\nChoose an option: \n>1.Admission\n>2.Academics\n>3.Exam\n>4.Transport\n>5.Exit\n"
    
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False
    

@app.route("/")
def hello():
    return "This is the home page of our Server!"


@app.route("/whatsapp", methods=['POST','GET'])
def msg_reply():
    msg = request.form.get('Body')
    global msgs
    global curnum
    global currenthandle
    num = request.values.get( 'From' )
    curnum = num[9:]
    if curnum not in msgs:
        msgs[curnum] = []
    msgs[curnum].append(msg)
    currenthandle = msgs[curnum]
    print(currenthandle)
    response = PersonalAssistant.handle_message(msgs,currenthandle,curnum)
    resp = MessagingResponse()
    resp.message(response)
    print(msgs)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)