import praw
import wget
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

#take relevant input
subname = input("Enter subreddit name: ")
contact = input("Enter contact/group to send to: ")
numofposts = int(input("Enter number of posts to send (number is not limited by the number of posts showing on the webpage!): "))


#make sure previously running chrome window of this script is closed before running it


#create reddit object
reddit = praw.Reddit(client_id='Ctced0SwuNBIRw',
                     client_secret='8alKy-b7jvTnLMcIEyTypfFvTnQ',
                     redirect_uri='http://localhost:8080',
                     user_agent='plagscript by /u/divy')


#setup options in chrome to open a Chrome Profile so that previously logged in whatsapp remains saved
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
driver.get('https://web.whatsapp.com/');


#open the relevant group/contact in whatsapp
element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR , '._2zCfw.copyable-text.selectable-text'))
)

name=driver.find_element_by_css_selector('._2zCfw.copyable-text.selectable-text')
name.send_keys(contact)
name.send_keys(Keys.ENTER)




#get posts in a loop from the subreddit
for p in reddit.subreddit(subname).hot( limit=numofposts):

    #if it is a text post, ignore and continue
    if p.is_self == True:
        continue

    #proced to fetch the caption (first comment in the post) and download the linked file in the post
    post = p
    
    url = post.url
    print("\nDownloading image at ", url)
    #print("url is ",url)

    imagebool = False
    for ext in ['png','jpg','jpeg','gif','bmp']:
        if ext in url:
            imagebool = True
            break
    
    if imagebool == False:
        print("downloaded post is not an image")
        continue
    
    top_level_comments = list(post.comments)
    caption= " "
    for i in top_level_comments:
        if len(i.body) < 50:
            caption = i.body
            break



    try:
        img = wget.download(url)
    except:
        continue


    #type in the caption in whatsapp
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR , '._3u328.copyable-text.selectable-text'))
    )
    msg=driver.find_element_by_css_selector('._3u328.copyable-text.selectable-text')
    try:
        msg.send_keys(caption)
    except:
        print("caption has characters that cannot be typed")

    #press the attach button on whatsapp to load the element that sends files
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Attach']")))
    attach =  driver.find_element_by_xpath("//div[@title='Attach']")
    attach.click()

    #send files 
    #WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")))
    time.sleep(.5)
    upload = driver.find_element_by_xpath("//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")

    path = os.getcwd() + '\\' + str(img)
    upload.send_keys(path)
    
    
    #press enter to send
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_1g8sv NOJWi']")))                             
    send = driver.find_element_by_xpath("//div[@class='_1g8sv NOJWi']")
    send.click()

    #delete the image
    os.remove(img)
    time.sleep(.5)





    
