import cv2
import pytesseract as pyt

img = cv2.imread('smile.png')
img2 = cv2.imread('quote.jpg')
img3 = cv2.imread('image_quote.jpg')
pyt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
text = pyt.image_to_string(img)
text2 = pyt.image_to_string(img2)
text3 = pyt.image_to_string(img3)
print(f'First picture: {text}')
print(f'Second picture: {text2}')
print(f'Third picture: {text3}')
