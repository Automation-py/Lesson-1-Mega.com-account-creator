# Lesson 1 Mega.nz Account Creator

**In this lesson, we will create a Mega.nz account creator using Selenium and the Request package. We will go more in depth with the Request package in later lessons. The first lesson is designed to give you some understanding of how automation works and functions.**


## Acknowledgement Before We start Make Sure You Know The Basics Before Continuing

 - [Learn The Basics Of Python Here](https://www.youtube.com/watch?v=kqtD5dpn9C8&ab_channel=ProgrammingwithMosh)
 - [Learn The Basics Of Selenium Here](https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ)
 - [Learn The Basics Of Request Here](https://www.youtube.com/watch?v=qriL9Qe8pJc&ab_channel=DanielLeeman)
 
 
 #
 
 - We will begin by using a template that I use when i have a Selenium project.
 
 #### We start by importing the package that we will use.
 
 ```
import random
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


