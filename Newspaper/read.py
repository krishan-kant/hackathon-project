
from PIL import Image
import pytesseract
import cv2
import os
import webbrowser
import urllib
import numpy as np
import re
from bs4 import BeautifulSoup
import pyautogui
from time import sleep
#key = cv2.waitKey(1)
webcam = cv2.VideoCapture(1)
while True:
	try:
		check, frame1 = webcam.read()
		frame1 = cv2.rectangle(frame1,(100,100),(500,300),(255,0,0),6)
		frame = frame1[100:300, 100:500]     
		cv2.imshow("capturing",frame1)     
		cv2.imshow("capture_actual",frame)
		key = cv2.waitKey(1)
		if key == ord('s'):
			try:
				f=open('saved_img.jpg','r')
				os.remove('saved_img.jpg')
			except:
				print('done')
			cv2.imwrite(filename='saved_img.jpg',img=frame)
			webcam.release()
			cv2.destroyAllWindows()
			break
		elif key == ord('q'):
			webcam.release()
			cv2.destroyAllWindows()
			break
	except(KeyboardInterrupt):
		webcam.release()
		cv2.destroyAllWindows()
		break
image = cv2.imread('saved_img.jpg', 1)
# grayscale
#image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", gray)

# apply thresholding to preprocess 

gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# median blurring
gray = cv2.medianBlur(gray, 3)


# temp imge & apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(' '.join(text.split()))


url = "https://www.youtube.com/results?search_query=" + urllib.quote(' '.join(text.split()))
#url2 = "https://www.google.com/search?client=ubuntu&channel=fs&q="+ urllib.quote(text) 

url = "https://www.youtube.com/results?search_query=" + urllib.quote(' '.join(text.split()))
response = urllib.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
first = 'https://www.youtube.com' + soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]['href']
webbrowser.open(first,new=2,autoraise=True)

#pyautogui.hotkey('alt','tab')
sleep(5)
pyautogui.click(button='left')
#pyautogui.press('f')
text=''

