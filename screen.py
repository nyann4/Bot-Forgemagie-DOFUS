def screenValues(A, B, C, D, E):
   from pathlib import Path
   import time 
   #Selectionne le chemin 
   list_value = []
   for i in  range(E) :
      list_value.append(0)
   root_path = Path(".").resolve()

   down = B
   i=0

   tmp_dir = root_path / "screen modifier"
   try:
      tmp_dir.mkdir(parents=True)
   except:
      pass
   
   while i != E:
      pprice = str(tmp_dir / "screen_{}.png".format(i))
      img = takeScreen(A, down, C, D)
      threshold(img, pprice, 85, i, list_value)
      down += 40
      i += 1
   return list_value


def takeScreen(posX, posY, pixelX, pixelY):
   import pyautogui 
   screen = pyautogui.screenshot(region=(posX, posY, pixelX, pixelY))
   return screen

def threshold(processed, path, valueTreshold1, i, list_value):
   import time
   from PIL import Image  
   import pytesseract  
   import cv2
   processed.save(path)
   processed = cv2.imread(path)
   # processed = cv2.threshold(processed, 0, 255, cv2.THRESH_BINARY_INV)[1]
   # processed = cv2.cvtColor(processed, cv2.COLOR_RGB2HLS)
   # processed = cv2.cvtColor(processed, cv2.COLOR_RGB2GRAY)
   # processed = cv2.threshold(processed, valueTreshold1, 100, cv2.THRESH_OTSU)[1] 
   # processed = cv2.threshold(processed ,55, 255, cv2.THRESH_BINARY)[1]
   # processed = cv2.adaptiveThreshold(processed, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 37, 1)[1]
   # processed = cv2.threshold(processed, valueTreshold1, 255, cv2.THRESH_BINARY_INV)[1]  
   cv2.imwrite(path, processed)
   processed = Image.open(path)
   ocr_result = pytesseract.image_to_string(processed)
   # ocr_result = pytesseract.image_to_string(processed, lang='eng',
   # config="--psm 10 --oem 3 -c tessedit_char_blacklist=''")
   list_value[i] = ocr_result
   # print(list_value)
   return list_value

# nombre_ligne_item = 10
# list_value = screenValues(768, 344, 200, 40*nombre_ligne_item, 1)
# print(list_value)
# time.sleep(1.5)
# nombre_ligne_item = 8
# list_value = screenValues(768, 341, 200, 40*nombre_ligne_item, 1)
# print(list_value)