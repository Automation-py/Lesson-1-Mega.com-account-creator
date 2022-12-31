# Lesson 1 Mega.nz Account Creator

**In this lesson, we will create a Mega.nz account creator using Selenium and the Request package. We will go more in depth with the Request package in later lessons. The first lesson is designed to give you some understanding of how automation works and functions.**


## Acknowledgement Before We start Make Sure You Know The Basics Before Continuing

 - [Learn The Basics Of Python Here](https://www.youtube.com/watch?v=kqtD5dpn9C8&ab_channel=ProgrammingwithMosh)
 - [Learn The Basics Of Selenium Here](https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ)
 - [Learn The Basics Of Request Here](https://www.youtube.com/watch?v=qriL9Qe8pJc&ab_channel=DanielLeeman)
 
 
 #
 
 - We will begin by using a template that I use when i have a Selenium project.
 
 #### We start by importing the packages that we will use.
 
 ```py
import random
import names
import selenium 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
 ```
 
 ## Installing pakages

To run this project successfully, you need to install these packages.
- Go to start>Search>Type CMD>Open As Admin> copy paste the following separately 

```bash
  pip install Selenium
  pip install names
```
 
 #### Then, we create two functions for generating random email and passwords using the package random.
 
 ```py
 def random_email():
    loademail = ''.join(
        random.choice("1234567890") for x in range(8)) #range(8)) sets the length to 8 random characters
    return loademail


def random_pass():
    loadpassword = ''.join(
        random.choice("1234567890") for x in range(8)) #range(8)) sets the length to 8 random characters
    return loadpassword
 ```
#### Third, we create a main function and place the Selenium code within it.
#### this part of the code will open chromedriver to Mega.nz, make sure [Chromedriver](https://chromedriver.chromium.org/downloads) is placed in the same path

```py
Headless = False

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--log-level=3")
    os.environ['WDM_LOG_LEVEL'] = '0'
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("window-size=500,500") #sets the chrome window size 

    if Headless == True:
        chrome_options.add_argument('headless')
    else:
        pass

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://mega.nz/register")
```

## All the code above is a template I use to start a project. I usually copy and paste it to save time.
- After this is done, we can begin automating the creation of Mega.nz accounts.

#### If you run the code you should get this

![1](https://user-images.githubusercontent.com/121656708/210117754-191fe745-5b8c-4c33-9bd6-0ff805674b3b.png)


## In the next step, we will use the NAMES package to complete our random email and password functions. 
- The following code should be placed in the main function above:


```py
first_name = names.get_first_name(gender='male')  #Random first name, example john

last_name = names.get_last_name() #Random last name, example doe

email = first_name + last_name + random_email() + "@xitroo.com"  #combines first and last names together plus adds email domain @xitroo.com, johndoe@xitroo.com

password = first_name + last_name + random_pass() #combines first and last names together plus adds random numbers to generate password

```


## Example

```py
Headless = False

def main():

    first_name = names.get_first_name(gender='male')  #Random first name, example john

    last_name = names.get_last_name() #Random last name, example doe

    email = first_name + last_name + random_email() + "@xitroo.com"  #combines first and last names together plus adds email domain @xitroo.com, johndoe@xitroo.com

    password = first_name + last_name + random_pass() #combines first and last names together plus adds random numbers to generate password


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--log-level=3")
    os.environ['WDM_LOG_LEVEL'] = '0'
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("window-size=500,500") #sets the chrome window size 

    if Headless == True:
        chrome_options.add_argument('headless')
    else:
        pass

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://mega.nz/register")
```

## Since Mega.nz requires you to email verify your email address, we will use a temporary email service called Xitroo.
- This email service does not have an API, so I created my own using the Request package I have used it on many websites. It allows you to verify the email address and it helps a lot, as they have multiple sub domains so if one of them is blocked you can use the others. Examples are xitroo.com, xitroo.org, xitroo.me, xitroo.fr etc...

#### Here is The API I Made
- It is not a complicated piece of code, but it does look confusing. You only need to copy and paste the following function:

```py

def FetchEmail(xitroo_email=None, subject=None, timeout=30):
    cwd = os.getcwd()
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

```

#### API Usage 
- All it takes is one line 

```py

# xitroo_email=email, Means the email you used to sign up to MEGA you feed it to the value of xitroo_email= which we generated the email up top and named it EMAIL 
# subject=MEGA, Each email has a subject all you need to do is manually go check the email thet Mega.nz sent and grab part of the subject.
# Here are some examples, Please verfiy your email MEGA, thats the subject of the email so we only need to grab a part of it which idealy would be MEGA and feed it to # # the value of subject=

email_content = FetchEmail(xitroo_email=email, subject="MEGA")

```

## If you are interested in this API, I have made it into a Python library you can install it by following these steps:
- Go to start>Search>Type CMD>Open As Admin> copy paste the following.

```
pip install xitroo-api
```
- Documentacion can be found [Here](https://pypi.org/project/xitroo-api/)


## Alright lets get back to coding Copy and Paste the following code Above/On-Top the main function

```py

def FetchEmail(xitroo_email=None, subject=None, timeout=30):
    cwd = os.getcwd()
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

```

## Your Project Should be looking like this:

```py
import random
import names
import selenium 
import os
import base64
from termcolor import colored
import colorama
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service



def random_email():
    loademail = ''.join(
        random.choice("1234567890") for x in range(8)) #range(8)) sets the length to 8 random characters
    return loademail


def random_pass():
    loadpassword = ''.join(
        random.choice("1234567890") for x in range(8)) #range(8)) sets the length to 8 random characters
    return loadpassword
    
    
def FetchEmail(xitroo_email=None, subject=None, timeout=30):
    cwd = os.getcwd()
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
    
    
    
    

def main():

    first_name = names.get_first_name(gender='male')  #Random first name, example john

    last_name = names.get_last_name() #Random last name, example doe

    email = first_name + last_name + random_email() + "@xitroo.com"  #combines first and last names together plus adds email domain @xitroo.com, johndoe@xitroo.com

    password = first_name + last_name + random_pass() #combines first and last names together plus adds random numbers to generate password


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--log-level=3")
    os.environ['WDM_LOG_LEVEL'] = '0'
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("window-size=500,500") #sets the chrome window size 

    if Headless == True:
        chrome_options.add_argument('headless')
    else:
        pass

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://mega.nz/register")
    
```

## The next section will be grabbing the Xpath of elements in Chrome and clicking or sending text to them.
- I will skip this step and paste the code, since you may already know how to do this step. If not, I suggest you watch this YT playlist. 
[Learn The Basics Of Selenium Here](https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ) 


```py
while __name__ == '__main__': #checks if the button is clickable on chrome tab
    try:
        r = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[2]/input").is_displayed()
        if r == True:
                 break
        else:
            pass
        

driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[2]/input").send_keys(first_name) #sends first name in text box in chrome

driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[3]/input").send_keys(last_name) #sends last name in text box in chrome

driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[5]/input").send_keys(email) #sends email in text box in chrome

driver.find_element(By.ID, "register-password-registerpage2").click() #clicks on the password box 1

driver.find_element(By.ID, "register-password-registerpage2").send_keys(password) #sends password in text box in chrome

driver.find_element(By.ID, "register-password-registerpage3").click() #clicks on the password box 2

driver.find_element(By.ID, "register-password-registerpage3").send_keys(password) #sends password-2 in text box in chrome

driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[8]/div[1]/input").click() #element clicks

driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[9]/div[1]/input").click() #element clicks

driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/button").click() #element clicks

```

## Your Project Should look Like This:

```py
import random
import names
import selenium 
import os
import base64
from termcolor import colored
import colorama
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service



def random_email():
    loademail = ''.join(
        random.choice("1234567890") for x in range(8)) #range(8)) sets the length to 8 random characters
    return loademail


def random_pass():
    loadpassword = ''.join(
        random.choice("1234567890") for x in range(8)) #range(8)) sets the length to 8 random characters
    return loadpassword
    
    
def FetchEmail(xitroo_email=None, subject=None, timeout=30):
    cwd = os.getcwd()
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
    
    
    
    

def main():

    first_name = names.get_first_name(gender='male')  #Random first name, example john

    last_name = names.get_last_name() #Random last name, example doe

    email = first_name + last_name + random_email() + "@xitroo.com"  #combines first and last names together plus adds email domain @xitroo.com, johndoe@xitroo.com

    password = first_name + last_name + random_pass() #combines first and last names together plus adds random numbers to generate password


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--log-level=3")
    os.environ['WDM_LOG_LEVEL'] = '0'
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("window-size=500,500") #sets the chrome window size 

    if Headless == True:
        chrome_options.add_argument('headless')
    else:
        pass

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://mega.nz/register")
    
    while __name__ == '__main__': #checks if the button is clickable on chrome tab
    try:
        r = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[2]/input").is_displayed()
        if r == True:
                 break
        else:
            pass
        

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[2]/input").send_keys(first_name) #sends first name in text box in chrome

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[3]/input").send_keys(last_name) #sends last name in text box in chrome

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[5]/input").send_keys(email) #sends email in text box in chrome

    driver.find_element(By.ID, "register-password-registerpage2").click() #clicks on the password box 1

    driver.find_element(By.ID, "register-password-registerpage2").send_keys(password) #sends password in text box in chrome

    driver.find_element(By.ID, "register-password-registerpage3").click() #clicks on the password box 2

    driver.find_element(By.ID, "register-password-registerpage3").send_keys(password) #sends password-2 in text box in chrome

    driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[8]/div[1]/input").click() #element clicks

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[9]/div[1]/input").click() #element clicks

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/button").click() #element clicks
    
```

#### If you run the code you should get this

https://user-images.githubusercontent.com/121656708/210121874-40f4bedf-c37d-4758-973b-c69247b3bf38.mp4


## Alright here comes the cool part, Email Verification
For the purpose of this lesson i tweaked some stuff, in my original source i had the email verification fully request based.
The changes i made are miner but i wanted to make this lesson toward Selenium fully we are still gonna use the XITROO API i made to grab 
the Verification link but we will verfiy it using webdriver rather than request just to simplify things.

## Okay a quick re-cap 
- We will be using this follwing code to get the verification link from the email.

1 - The Random Email We Created With a Xitroo.com Domain
```py
email = first_name + last_name + random_email() + "@xitroo.com"
```

2 - The Xitroo API function
```py
def FetchEmail(xitroo_email=None, subject=None, timeout=30):
```

## Let's Get Started:
- We will call the function as the code shows below
- The xitroo_email= will take the value email
- The subject= will take part of the email subject you recived, example below

![Email ](https://user-images.githubusercontent.com/121656708/210122307-25c01b63-5e6f-4f44-b901-a9a9158f49b5.png)


```py
email_content = FetchEmail(xitroo_email=email, subject="MEGA")
```

## Your Project Should look Like This:

```py
import random
import names
import selenium 
import os
import base64
from termcolor import colored
import colorama
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service



def random_email():
    loademail = ''.join(
        random.choice("1234567890") for x in range(8)) #range(8)) sets the length to 8 random characters
    return loademail


def random_pass():
    loadpassword = ''.join(
        random.choice("1234567890") for x in range(8)) #range(8)) sets the length to 8 random characters
    return loadpassword
    
    
def FetchEmail(xitroo_email=None, subject=None, timeout=30):
    cwd = os.getcwd()
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
    
    
    
    

def main():

    first_name = names.get_first_name(gender='male')  #Random first name, example john

    last_name = names.get_last_name() #Random last name, example doe

    email = first_name + last_name + random_email() + "@xitroo.com"  #combines first and last names together plus adds email domain @xitroo.com, johndoe@xitroo.com

    password = first_name + last_name + random_pass() #combines first and last names together plus adds random numbers to generate password


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--log-level=3")
    os.environ['WDM_LOG_LEVEL'] = '0'
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("window-size=500,500") #sets the chrome window size 

    if Headless == True:
        chrome_options.add_argument('headless')
    else:
        pass

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://mega.nz/register")
    
    while __name__ == '__main__': #checks if the button is clickable on chrome tab
    try:
        r = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[2]/input").is_displayed()
        if r == True:
                 break
        else:
            pass
        

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[2]/input").send_keys(first_name) #sends first name in text box in chrome

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[3]/input").send_keys(last_name) #sends last name in text box in chrome

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[5]/input").send_keys(email) #sends email in text box in chrome

    driver.find_element(By.ID, "register-password-registerpage2").click() #clicks on the password box 1

    driver.find_element(By.ID, "register-password-registerpage2").send_keys(password) #sends password in text box in chrome

    driver.find_element(By.ID, "register-password-registerpage3").click() #clicks on the password box 2

    driver.find_element(By.ID, "register-password-registerpage3").send_keys(password) #sends password-2 in text box in chrome

    driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[8]/div[1]/input").click() #element clicks

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[9]/div[1]/input").click() #element clicks

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/button").click() #element clicks
    
    email_content = FetchEmail(xitroo_email=email, subject="MEGA")
    
```

## FetchEmail Function explanation:

#### How does it grab the verification link?

it sends requests to the Xitroo.com servers and checks if the random email we created recived any emails, and if it has then it checks each email for a subject containing MEGA as we told the function to look for MEGA.

#### After it finds the email what does it do?

It sends another request to grab the message body of that email , where we can then see the content of the email and get the verification link.

#### How does the email body look like?

will when the function finds the email and sends the 2end request to grab the content it has to decode it from HEX to UFT-8 so we can read it, here is an example 
of how it looks decoded 

```
johndoe@xitroo.com

You have one more step remaining to activate your MEGA account.


Click on the link below to verify your email address:

https://mega.nz/#confirmQ29uZmlybUNvZGVWMt4Sgs26BgAGUOn6yHsHwUxhd3JlbmNlS2luZ18wMjM0QHhpdHJvby5jb20JTGF3cmVuY2UgS2luZ1lq3S3CeDT3

Best regards,

— Team MEGA
```

## seperating the verification link from the rest of the body content 
- we have to use a package called re which is a short name for regex here is how we do that.

Make sure to (import) re at the very top of the code

```py
url = re.findall('https://(.*?)\n', email_content)[0] #grabs url from email to seperate it

confirmation_url = "https://" + url #adds https:// to url to auth
```

#### Then we call driver.get() to open the verification link to verify the account 

```py
email_content = FetchEmail(xitroo_email=email, subject="MEGA") # function gets auth url from email

url = re.findall('https://(.*?)\n', email_content)[0] #grabs url from email to seperate it

confirmation_url = "https://" + url #adds https:// to url to auth

driver.get(confirmation_url) #opens the auth link
```

#### Once the chromedriver opens the confirmation_url we have a few more steps and we are done
- We have to chosse a plan since MEGA is a cloud storage service, here how to do that.

```py
while __name__ == '__main__': #checks if button is clickable
    try:
      r = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[3]/input").is_displayed()
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
  driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[5]/div/div[2]/div[2]/div").click()
except:
    try:
     time.sleep(2)
     driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[5]/div/div[2]/div[2]").click()
    except:
       pass
```

## Your Project Should look Like This:

```py
import random
import names
import selenium 
import os
import base64
from termcolor import colored
import colorama
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service



def random_email():
    loademail = ''.join(
        random.choice("1234567890") for x in range(8)) #range(8)) sets the length to 8 random characters
    return loademail


def random_pass():
    loadpassword = ''.join(
        random.choice("1234567890") for x in range(8)) #range(8)) sets the length to 8 random characters
    return loadpassword
    
    
def FetchEmail(xitroo_email=None, subject=None, timeout=30):
    cwd = os.getcwd()
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
    
    
    
    

def main():

    first_name = names.get_first_name(gender='male')  #Random first name, example john

    last_name = names.get_last_name() #Random last name, example doe

    email = first_name + last_name + random_email() + "@xitroo.com"  #combines first and last names together plus adds email domain @xitroo.com, johndoe@xitroo.com

    password = first_name + last_name + random_pass() #combines first and last names together plus adds random numbers to generate password


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--log-level=3")
    os.environ['WDM_LOG_LEVEL'] = '0'
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("window-size=500,500") #sets the chrome window size 

    if Headless == True:
        chrome_options.add_argument('headless')
    else:
        pass

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://mega.nz/register")
    
    while __name__ == '__main__': #checks if the button is clickable on chrome tab
    try:
        r = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[2]/input").is_displayed()
        if r == True:
                 break
        else:
            pass
        

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[2]/input").send_keys(first_name) #sends first name in text box in chrome

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[3]/input").send_keys(last_name) #sends last name in text box in chrome

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[5]/input").send_keys(email) #sends email in text box in chrome

    driver.find_element(By.ID, "register-password-registerpage2").click() #clicks on the password box 1

    driver.find_element(By.ID, "register-password-registerpage2").send_keys(password) #sends password in text box in chrome

    driver.find_element(By.ID, "register-password-registerpage3").click() #clicks on the password box 2

    driver.find_element(By.ID, "register-password-registerpage3").send_keys(password) #sends password-2 in text box in chrome

    driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[8]/div[1]/input").click() #element clicks

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[9]/div[1]/input").click() #element clicks

    driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/button").click() #element clicks
    
    email_content = FetchEmail(xitroo_email=email, subject="MEGA")
    
    url = re.findall('https://(.*?)\n', email_content)[0] #grabs url from email to seperate it

    confirmation_url = "https://" + url #adds https:// to url to auth

    driver.get(confirmation_url) #opens the auth link
    
    while __name__ == '__main__': #checks if button is clickable
       try:
         r = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/form/div[3]/input").is_displayed()
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
     driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[5]/div/div[2]/div[2]/div").click()
   except:
     try:
       time.sleep(2)
       driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div[5]/div/div[2]/div[2]").click()
     except:
       pass
```

#### And We Are Done, You've just made a Mega.nz Account creator 🎉
- We still have some stuff to do but the Main program is Done.

#### I like to add a checker to check if the account is really done and the way i do that is to check if the web-page says the account generation is successful here is how i do that 

```py
 while True:
        if "Account Recovery" in driver.page_source: #checks if The Account Was successfully Done
                      saveaccount = open("accounts.txt", "a")
                      saveaccount.writelines("{}:{}\n".format(email, password))
                      saveaccount.close()
        else:
          pass
```

#### If the account wass successfully made it will save it in a txt document in the same path as the program 


## Final Thoughts
I hope you learned something new with this lesson, In the next lesson we will go more in depth about selenium and automation, the projects will get more interesting 
I might be using a battle.net gen or a discord gen next lesson, that would be instresting since thesse tools sell for money.

Im so exited to see your guys feedback on this lesson and what i can improve on, to give you guys the best automation information out there 

## This is not a must but, If you appreciate my hard work please Donate 💰
BTC: 32qQwjQ18FF2GntAP8iPhkQ4UoMkgbTN4F


