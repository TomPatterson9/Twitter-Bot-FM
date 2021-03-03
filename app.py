import pyautogui
import cv2
import pytesseract
import tweepy
import time

keyFile = open('twitterKeys.txt', 'r')
consumer_key = keyFile.readline().rstrip()
consumer_secret = keyFile.readline().rstrip()
access_token = keyFile.readline().rstrip()
access_token_secret = keyFile.readline().rstrip()
keyFile.close()

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# Create API object
api = tweepy.API(auth)

lastTweet = ''
currentScore = ''
leedsUnited = 'leeds'
while True:
    myScreenshot = pyautogui.screenshot(region=(700, 250, 540, 210))
    myScreenshot.save(r'C:\Users\Tom\Documents\Twitterbot-python\test.png')

    img = cv2.imread('test.png')
    tempScore = pytesseract.image_to_string(img)
 
    
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
