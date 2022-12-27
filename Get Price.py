import requests
from bs4 import BeautifulSoup
import time
import lxml
import webbrowser
import pyautogui
import os
from urllib.request import urlopen

print("\n**************WELCOME TO PRICE RETRIEVER***************")
print('              ------------------------               \n')

def main():
    print('Options:')
    print('1.Asus Zenbook 15 4K')
    print('2.Razer Blade 15 Base RTX 2060')
    print('3.MSI GS66 Stealth RTX 2060')
    print('\n4.Exit\n')

def Price(URL):
    print('\nChecking Price\n')
    while True:
        try:
            #global page,soup
            myuseragent={'User-Agent':'Mozilla/5.0'}# (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
            #page = requests.get(URL , headers=myuseragent)
            page = urlopen(URL)
            #print(page)
            Soup = BeautifulSoup(page,'lxml')
            Title = Soup.find(id='title').get_text().strip()
            Price = Soup.find(id='priceblock_ourprice').get_text()

            
            print('\nTitle:',Title)
            print('\n'+'Price:',Price)
            
            #specs = soup.find(id='productDetails_feature_div')
            specs = Soup.find('div',class_='a-expander-content a-expander-extend-content')

            try:
                File=open('test.html','w')
                File.write(Soup.prettify())
                File.close()
            except:
                File=open('test.html','w')
                File.write('')
                File.close()

            try:
                a=specs.prettify()
                File=open('specs.html','w')
                File.write(a)
                File.close()
            except:
                File=open('specs.html','w')
                File.write('')
                File.close()
            

            while True:
                print('\nOptions:\n')
                print('1.Display Specifications')
                print('2.Open Website')
                print('3.Open Website Locally')
                print('4.Main Menu')

                option=input('\nEnter Your Option:')
                if option=='1': 
                    os.startfile('specs.html')

                elif option=='2':
                    webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s").open(URL)
                    
                elif option=='3':
                    os.startfile('test.html')

                elif option == '4':
                    print()
                    break

                else:
                    print('\n\nInvalid Option !!!\n\n')
                    pass
            break
        except Exception as e:
            #print(e , end='   ')
            pass

def thanks():
    print('\n     ----------------------------------------------------------------')
    print('                             !!! Thank You !!!')
    print('     ----------------------------------------------------------------\n')


while True:
    main()
    Option = input('Enter the Option:')
    if Option=='1':
        URL='https://www.amazon.com/ASUS-UX534FTC-AS77-i7-10510U-ScreenPad-Compatible/dp/B0869JVMLY/ref=sr_1_3?dchild=1&keywords=asus+zenbook+15&qid=1606566145&sr=8-3'
        #URL='https://www.amazon.in/ASUS-i7-10510U-ScreenPad-Compatible-UX534FTC-AS77/dp/B0869JVMLY/ref=sr_1_20?dchild=1&keywords=asus+zenbook+15&qid=1606731690&sr=8-20'
        Price(URL)
        
    elif Option == '2':
        URL='https://www.amazon.com/Razer-Blade-Base-Gaming-Laptop/dp/B086MGYM49/ref=sr_1_3?crid=3T1TZRNQ7GO92&dchild=1&keywords=razer+blade+15+base+gaming+laptop+2020&qid=1606728311&sprefix=razer+blade+15%2Caps%2C346&sr=8-3'
        Price(URL)

    elif Option == '3':
        URL='https://www.amazon.com/MSI-GS66-Stealth-10SE-442-i7-10875H/dp/B0895Q3HW5/ref=sr_1_3?dchild=1&keywords=msi+gs66&qid=1606729242&sr=8-3'
        Price(URL)

    elif Option=='4':
        thanks()
        break
        #exit()
    else:
        print('\nINVALID OPTION TRY AGAIN !!\n')
        pass
