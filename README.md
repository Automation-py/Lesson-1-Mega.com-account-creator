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

To run this project secuessfully, install these pakages 

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

    driver.get("https://mega.nz/start")
```

## All the code above is a template I use to start a project. I usually copy and paste it to save time.
- After this is done, we can begin automating the creation of Mega.nz accounts.

#### If you run the code you should get this

![1](https://user-images.githubusercontent.com/121656708/210117754-191fe745-5b8c-4c33-9bd6-0ff805674b3b.png)


## In the next step, we will use the NAMES package to complete our random email and password functions. 





