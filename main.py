
try:
    import base64
    import datetime
    from termcolor import colored
    import os
    import time
    from time import sleep
    from colorama import Fore
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as EC, expected_conditions
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
    import os
    import re
    import sys
    import time
    import json
    import shutil
    import ctypes
    import random
    import colorama
    import threading
    import subprocess
    from time import sleep
    import sys
    from uuid import uuid4
    import multiprocessing
    from subprocess import Popen, PIPE
    import json
    import json as jsond
    import webbrowser
    import requests
    import psutil
    import random
    import string
    import ctypes
    import selenium
    import names
    from selenium.webdriver.chrome.service import Service
except Exception as e:
    print(e)
    input()

Account_made = 0

ctypes.windll.kernel32.SetConsoleTitleW("Mega Account Generator | {} Created Accounts".format(Account_made))  #Set console title

cwd = os.getcwd() #gets current folder that the program is running in


#--------- opens file to grab settings

try:
    with open('config.json', 'r') as f:
        data = json.load(f)

    Use_proxy = re.findall("'Use_Proxies': '(.*?)'", str(data))[0]
    Threads = re.findall("'Threads': '(.*?)'", str(data))[0]
except:
    print(Fore.RED + " ● " + Fore.LIGHTCYAN_EX + "Application: " + Fore.RED + "Something is Wrong With The Config.json, Make sure you fill out the config Correctly.")
    input("")
    try:
        exit()
    except:
        sys.exit()

#--------- opens file to grab settings


def random_email():
    loademail = ''.join(
        random.choice("1234567890") for x in range(4))
    return "_" + loademail


def random_pass():
    loademail = ''.join(
        random.choice("1234567890") for x in range(3))
    return loademail


#--------- email service function

def FetchEmail(xitroo_email=None, subject=None, timeout=30):
    if xitroo_email == None:
        print(f"""
        {Fore.RED}
Traceback (an error has occurred):
   File "{cwd}"
     Error = get_email(xitroo_email=?)
TypeError: get_email(xitroo_email=?), Missing positional argument, xitroo_email= should have the value of the generated email. """)
        input()
    else:
        pass

    if subject == None:
            print(f"""
            {Fore.RED}
Traceback (an error has occurred):
   File "{cwd}"
     Error = get_email(subject=?)
TypeError: get_email(subject=?), Missing positional argument, subject= should have the value of the email subject received. """)
            input()
    else:
        pass

    xitroo_session = requests.session()

    counter = 0

    while True:
        counter += 1
        now = datetime.datetime.now()
        b = now + datetime.timedelta(0, 600)
        timestamp = datetime.datetime.timestamp(b)

        xitroo_response = xitroo_session.get(
            "https://api.xitroo.com/v1/mails?locale=en&mailAddress=" + xitroo_email + "&mailsPerPage=25&minTimestamp=0&maxTimestamp=" + str(
                timestamp))

        if str(subject) in xitroo_response.text:
            break

        time.sleep(1)

        if counter == timeout:
            return print(Fore.RED + "Email timeout limit has reached")
        else:
            pass

    email_id = re.findall('_id":"(.*?)"', xitroo_response.text)[0]


    data = {
        'id': email_id
    }

    email_body = xitroo_session.get("https://api.xitroo.com/v1/mail?locale=en&id={}".format(email_id), data=data)
    bodytext = re.findall('"bodyText":"(.*?)"', email_body.text)[0]
    code = base64.b64decode(bodytext)
    conv_email_base64 = base64.b64encode(code)
    body = base64.b64decode(conv_email_base64).decode()
    return body

#--------- email service function


print(Fore.LIGHTGREEN_EX + " ● Creating Mega Accounts, Please Wait...\n")

def main():
    global Account_made, driver
    try:
        while True:

            first_name = names.get_first_name(gender='male')  #Random first name, example john

            last_name = names.get_last_name() #Random last name, example doe

            email = first_name + last_name + random_email() + "@xitroo.com"  #combines first and last names together plus adds email domain @xitroo.com, johndoe@xitroo.com

            password = first_name + last_name + random_pass() #combines first and last names together plus adds random numbers to generate password

            # --------- selenium stuff

            chrome_options = webdriver.ChromeOptions() # random stuff
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) # random stuff
            prefs = {"profile.default_content_setting_values.notifications": 2} # random stuff
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument("--log-level=3") # random stuff
            os.environ['WDM_LOG_LEVEL'] = '0' # random stuff
            chrome_options.add_argument(
                'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36') # random stuff
            chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) # random stuff
            chrome_options.add_argument('--profile-directory=Default') # random stuff
            chrome_options.add_argument('--disable-blink-features=AutomationControlled') # random stuff
            chrome_options.add_argument("window-size=500,500") # sets window size

            # --------- selenium stuff


            driver = webdriver.Chrome(options=chrome_options)

            driver.get("https://mega.nz/register") #opens chrome tab of the link you added

            while __name__ == '__main__': #checks if the button is clickable on chrome tab
                try:
                    r = driver.find_element(By.XPATH,
                                            "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[2]/input").is_displayed()
                    if r == True:
                        break
                    else:
                        pass
                except:
                    pass

            driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[2]/input").send_keys(first_name) #sends first name in text box in chrome

            driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[3]/input").send_keys(last_name) #sends last name in text box in chrome

            driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[5]/input").send_keys(email) #sends email in text box in chrome

            driver.find_element(By.ID, "register-password-registerpage2").click() #clicks on the password box 1

            driver.find_element(By.ID, "register-password-registerpage2").send_keys(password) #sends password in text box in chrome

            driver.find_element(By.ID, "register-password-registerpage3").click() #clicks on the password box 2

            driver.find_element(By.ID, "register-password-registerpage3").send_keys(password) #sends password-2 in text box in chrome

            driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[8]/div[1]/input").click() #random clicks

            driver.find_element(By.XPATH,
                                "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[9]/div[1]/input").click() #random clicks

            driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/button").click() #random clicks

            email_content = FetchEmail(xitroo_email=email, subject="MEGA") # function gets auth url from email

            url = re.findall('https://(.*?)\n', email_content)[0] #grabs url from email to seperate it

            confirmation_url = "https://" + url #adds https:// to url to auth

            driver.get(confirmation_url) #opens the auth link

            while __name__ == '__main__': #checks if button is clickable
                try:
                    r = driver.find_element(By.XPATH,
                                            "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[3]/input").is_displayed()
                    if r == True:
                        break
                    else:
                        pass
                except:
                    pass

            driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[3]/input").send_keys(password)

            driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/button").click()

            time.sleep(3)
            try:
                driver.find_element(By.XPATH,
                                    "/html/body/div[6]/div[2]/div/div[2]/div[5]/div/div[2]/div[2]/div").click()
            except:
                try:
                    time.sleep(2)
                    driver.find_element(By.XPATH,
                                        "/html/body/div[6]/div[2]/div/div[2]/div[5]/div/div[2]/div[2]").click()
                except:
                    pass

            while True:
                if "Account Recovery" in driver.page_source: #checks if Account Recovery is on the webpage

                    #--------- opens file to save the account

                    saveaccount = open("accounts.txt", "a")
                    saveaccount.writelines("{}:{}\n".format(email, password))
                    saveaccount.close()

                    # --------- opens file to save the account


                    print(Fore.LIGHTGREEN_EX + f" ● Acoount Created | {email}:{password}") #prints account on console
                    Account_made += 1
                    ctypes.windll.kernel32.SetConsoleTitleW("Mega Account Generator | {} Created Accounts".format(Account_made))
                    driver.quit() #closes chrome tab
                    break
    except Exception as e:
        print(e)
        driver.quit() #if an error happens it closes chrome tab and re-runs the script
        main()


for i in range(int(Threads)):
    m = threading.Thread(target=main)
    m.start()