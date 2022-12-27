import requests
from bs4 import BeautifulSoup
import time
import lxml
import webbrowser
import pyautogui
import os

print('IMPORTED')
#URL='https://www.amazon.in/ASUS-i9-10980HK-Touchscreen-Celestial-UX581LV-H2035T/dp/B08CHDLVT1/ref=sr_1_2_sspa?dchild=1&keywords=asus+zenbook%5C&qid=1606565869&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUUgwS1pRUlFTSEFCJmVuY3J5cHRlZElkPUEwNDgzNDMxOFdWT05JR0xFS1hUJmVuY3J5cHRlZEFkSWQ9QTA2NTQwMDUxSVlJNkEwNzdYWjJQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
#URL= 'https://www.amazon.com/ASUS-UX534FTC-AS77-i7-10510U-ScreenPad-Compatible/dp/B0869JVMLY/ref=sr_1_3?dchild=1&keywords=asus+zenbook+15&qid=1606566145&sr=8-3'
URL='https://www.amazon.com/Razer-Blade-Base-Gaming-Laptop/dp/B086MGYM49/ref=sr_1_3?crid=3T1TZRNQ7GO92&dchild=1&keywords=razer+blade+15+base+gaming+laptop+2020&qid=1606728311&sprefix=razer+blade+15%2Caps%2C346&sr=8-3'

def screenshot(website):
    #os.system(f'python -m webbrowser -t {website}')
    time.sleep(1)
    pyautogui.hotkey('win','up')
    print('Step1')
    webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s").open(website)
    time.sleep(2)
    print('Opened')
    iml=pyautogui.screenshot()
    print('Taken')
    iml.save("tempval.jpeg")
    #iml.show()
    #iml.close()
    print('Taken Screenshot')
    time.sleep(1)
    os.system('taskkill /im msedge.exe /f"')

    
def email1(website):
    try:
        import smtplib
        from email.message import EmailMessage
        sender_email = os.environ.get('PYTHON_MAIL')
        rec_email = os.environ.get('REC_MAIL')
        password = os.environ.get('PYTHON_MAIL_PASS')

        msg=EmailMessage()
        msg['Subject']='Laptop Price Drop'
        msg['From']=sender_email
        msg['To']=rec_email
        msg.set_content('Price Dropped to '+Price+'at'+str(time.ctime()[11:16]))
        current_time=str(time.ctime()[11:16])
        msg.add_alternative(f'''
            <!DOCTYPE html>
            <html>
                <body>
                <body>
                    <h1 style="color:SlateGray;"> Price Dropped to {Price} at {current_time} </h1>
                    <h1 style="color:SlateGray;"> Title:{Title} </h1>
                    <h1 style="color:SlateGray;"> Website:{website} </h1>
                </body>
            </html>
        ''', subtype='html')
        screenshot(website)
    
        f=open("tempval.jpeg",'rb')
        msg.add_attachment(f.read(),maintype='image',subtype='jpeg',filename='Screenshot')
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        print("\nLogin Success")
        #server.send_message(msg)
        print("Email has been sent to ", rec_email,'\n')
        print('Email Content:\n'+'FROM    :',msg['From'],'\nTo      :',msg['To'],'\nSubject :',msg['Subject'])
        server.quit()
        f.close()
        
        os.remove('tempval.jpeg')
        
    except:
        print('Emailing Error !!')
        time.sleep(60)
print('Running')
while True:
    try:
        HEADERS={'User-Agent':'Mozilla/5.0'}# (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
        page = requests.get(URL , headers=HEADERS)
        #print(page)
        soup = BeautifulSoup(page.text,'html.parser')
        Title = soup.find(id='title').get_text().strip()
        Price = soup.find(id='priceblock_ourprice').get_text()
        if float(Price.replace('$','').replace(',',''))>1100:
            print('Title',Title)
            print('\n'+'Price:',Price)
            print('Started\n')
            print('Over')
            screenshot(URL)
            email1(URL)
            break
    except Exception as e:
        pass
