#!/usr/bin/python3
# encoding -*- utf-8 -*-

from selenium.webdriver.support.ui import Select
from selenium import webdriver
import glob, os , sys ,time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random


try:
    All_PROXY= open("Proxy.txt", "r").read().split()
except:
    print("You have Proxy.text list !!")

driver = webdriver.Chrome()
url = input("Video url : ")
counter = 0
    

# Play Video
def playing_video():
    try:
        PROXY = random.choice(All_PROXY)
        options = Options()
        options.add_argument('--proxy-server=%s' % PROXY)
        options.add_argument('--allow-running-insecure-content')
        print(PROXY)
        driver.get(url)
        videoid = driver.find_element_by_class("video-stream html5-main-video")
        #videolike = driver.find_element_by_class_name("style-scope yt-icon-button")
        videoid.click()
        print("[ + ] Wait watch  Video N {}......".format(counter))
        try:
            driver.find_element_by_id("button").click()
            print("Liked Video √ ")
        except:
            print("error not like  video ")    
        counter =+1
    except:
        pass

def main():
    while True:
        playing_video()  
        time.sleep(60)
       

if __name__ == "__main__":
    main()     
