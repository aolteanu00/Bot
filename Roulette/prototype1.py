from subprocess import call
import os
import pyautogui
from PIL import Image
import PIL.ImageOps
import time
import random

print("*")
print("*")
print("*")
print("DRIPBOT#2 IS LIVE")
print("_________________________________________________________________________")
start_balance = int(input('Enter starting amount: '))
money_make = int(input('Enter the amount you want to make: '))
stop_loss = start_balance + money_make
print(stop_loss)
list = ["z", 'x']
#num_loss = 0
time_list = [15]

#pyautogui functions
def chip():
    pyautogui.click(x=797, y=874, clicks=1, button='left')
    pyautogui.click(x=797, y=874, clicks=1, button='left')

def black():
    pyautogui.click(x=1319, y=634, clicks=1, button='left')
    pyautogui.click(x=1319, y=634, clicks=1, button='left')

def spin():
    pyautogui.click(x=1413, y=871, clicks=1, interval=2, button='left')
    pyautogui.click(x=1413, y=871, clicks=1, button='left')

def re_bet():
    pyautogui.click(x=1311, y=873, clicks=1, button='left')
    pyautogui.click(x=1311, y=873, clicks=1, interval=2, button='left')

def re_bet2x():
    pyautogui.click(x=1331, y=873, clicks=1, button='left')
    pyautogui.click(x=1331, y=873, clicks=1, button='left')

#image functions
def screengrab():
    call(["screencapture", "-R348,961,70,20", "test.jpg"])
    image = Image.open('test.jpg')
    new_image = image.resize((200, 50))
    new_image.save("test.png")


def black_and_white(input_image_path, output_image_path):
   color_image = Image.open(input_image_path)
   bw = color_image.convert('L')
   bw.save(output_image_path)

def invert_colors(image):
    image = Image.open('test1.png')
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save('test2.png')

def resize_image():
    basewidth = 500
    img = Image.open('test2.png')
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save('test3.png')

def adjust_resolution():
    image_path = "test3.png"
    image_file = Image.open(image_path)
    image_file.save("test4.png", dpi=(500,500))

#tesseract function
def tess_run():
    os.system("tesseract test4.png tess 6")
    file_in = open('tess.txt', 'r')
    y = file_in.read().split(',')
    w = ''.join(y)
    r = w.replace('\n\x0c', '')
    q = float(r)
    z = list.append(q)


#bet
def bet():
    if list[-1] > list[-2]:
        black()
        spin()
        list.pop(-3)
        #num_loss = 0
    if list[-1] < list[-2]:
        re_bet()
        re_bet2x()
        spin()
        list.pop(-3)
        #num_loss = num_loss + 1


def image_func():
    screengrab()
    x = black_and_white("test.png", "test1.png")
    invert_colors(x)
    resize_image()
    adjust_resolution()
    tess_run()

def start_game():
    image_func()
    chip()
    black()
    spin()
    list.pop(-3)
    time.sleep(13)

def body():
    image_func()
    bet()


i = 0
while i < 1:
    start_game()
    i += 1
    i2 = 0
while list[-1] < stop_loss:
    body()
    print(list)
    x = random.choice(time_list)
    time.sleep(x)



print("_________________________________________________________________________")
print("DRIPBOT#2 OUT")
print("*")
print("*")
print("*")
