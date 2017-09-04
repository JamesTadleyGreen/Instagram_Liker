#Program to load up instagram, login using details, navigate to specific tags
# and like a specified number of photos. Then record data in text file.

#imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import webbrowser
import time
import datetime
import random
from random import randint
import os

#main function
def main():

    USERNAME = ""
    PASSWORD = ""
    
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "chrome/chromedriver"
    abs_file_path = os.path.join(script_dir, rel_path)


    #Tags to like
    insta = ['https://www.instagram.com/explore/tags/computerscience/',
             'https://www.instagram.com/explore/tags/study/',
             'https://www.instagram.com/explore/tags/learning/',
             'https://www.instagram.com/explore/tags/maths/',
             'https://www.instagram.com/explore/tags/math/',
             'https://www.instagram.com/explore/tags/science/',
    		 'https://www.instagram.com/explore/tags/exploring/']

    #location of the chrome browser
    driver = webdriver.Chrome(executable_path=abs_file_path)

    #login information
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(1)
    inputElementUsername = driver.find_element_by_name("username")
    inputElementUsername.send_keys(USERNAME)
    inputElementPassword = driver.find_element_by_name("password")
    inputElementPassword.send_keys(PASSWORD)
    time.sleep(1)
    inputElementUsername.send_keys(Keys.ENTER)

    #opening a random webpage
    #sleeping to allow time for page to load
    time.sleep(3)
    driver.get(random.choice(insta))
    time.sleep(3)
    
    #running liker 
    driver.find_element_by_css_selector('._e3il2').click() #find and click on first image (starts "slideshow")
    time.sleep(1)
    i = 1
    
    #like photos
    while i < random.randint(10, 50): #random number of photos chosen
        time.sleep(1.5)
        try:
            driver.execute_script("document.querySelector('.coreSpriteHeartOpen').click();") #like the photo
        except:
            pass #if 404 error or page does not load on time, move on
        try:
            driver.find_element_by_css_selector('._3a693').click() #move on to next photo
        except:
            driver.get(random.choice(insta)) #if 404 error, restart with new tag selection
            time.sleep(3)
            driver.find_element_by_css_selector('._e3il2').click()
            time.sleep(1)
        i += 1

    #collect data about run
    time.sleep(10)
    #write out the last URL to check for errors
    with open('last_url.txt', 'a') as the_file:
        the_file.write(driver.current_url + ' at ' + ('%s' % datetime.datetime.now()))
    #go to account and check followers    
    driver.get("https://www.instagram.com/" + USERNAME + "/")
    with open('last_url.txt', 'a') as the_file:
        the_file.write(' with ' + driver.find_elements_by_class_name("_t98z6")[1].text + '\n')
    #quit the browser
    driver.quit();
    print('Done')
    print(datetime.datetime.now())


#run main program
main()
