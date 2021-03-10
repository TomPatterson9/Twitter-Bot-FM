import pyautogui
import cv2
import pytesseract
import tweepy
import time
import os
from dotenv import load_dotenv

load_dotenv()
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# Create API object
api = tweepy.API(auth)

lastTweet = ''
currentScore = ''
leedsUnited = 'leeds' 
while True:
    myScreenshot = pyautogui.screenshot(region=(700, 253, 240, 190))
    myScreenshot.save(r'C:\Users\Tom\Documents\Twitterbot-python\area1.png')

    myScreenshot = pyautogui.screenshot(region=(955, 253, 235, 190))
    myScreenshot.save(r'C:\Users\Tom\Documents\Twitterbot-python\area2.png')

    img = cv2.imread('area1.png')
    tempScore = pytesseract.image_to_string(img)


    img = cv2.imread('area2.png')
    tempScore += "\n"

    tempScore += pytesseract.image_to_string(img)
 
    if leedsUnited in tempScore.lower():
        print("yes")
        if currentScore != tempScore:
            currentScore = tempScore
            time.sleep(5)
            # Create a tweet
            if lastTweet != currentScore:
                print(currentScore.strip())
                api.update_status(currentScore.strip())
                lastTweet = currentScore
    print("end of loop")
