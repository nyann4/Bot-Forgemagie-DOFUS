def screen(A, B, C, D, E):
    from pathlib import Path
    list_1 = []
    root_path = Path(".").resolve()
    down = B
    i=0

    tmp_dir = root_path / "screen modifier"
    try:
        tmp_dir.mkdir(parents=True)
    except:
        pass
    while i != E:   
        pprice = str(tmp_dir / "tmp-priice{}.png".format(i))
        img = takeScreen(A, down, C, D)
        img.save(r''+str(root_path)+'\screenshot'+str(i)+'.png')
        threshold(img, pprice, 85, i, list_1)
        down += 40
        i += 1
        
    # print(list_1)
    return list_1
    

def takeScreen(posX, posY, pixelX, pixelY):
    import pyautogui 
    screen = pyautogui.screenshot(region=(posX, posY, pixelX, pixelY))
    return screen

def threshold(processed, path, valueTreshold1, i, list_1):
    from PIL import Image  
    import pytesseract  
    import cv2
    processed.save(path)
    processed = cv2.imread(path)
    processed = cv2.cvtColor(processed, cv2.COLOR_RGB2GRAY)
    # processed = cv2.threshold(processed, valueTreshold1, 255, cv2.THRESH_OTSU)[1]  
    # processed = cv2.threshold(processed, valueTreshold1, 255, cv2.THRESH_BINARY_INV)[1]  
    cv2.imwrite(path, processed)
    processed = Image.open(path)
    ocr_result = pytesseract.image_to_string(processed)
    # ocr_result = re.sub("[^0-9]","", ocr_result)            

    list_1.append(ocr_result)
    return list_1

# rune = screen(290, 752, 285, 138, 1)
# print(rune)