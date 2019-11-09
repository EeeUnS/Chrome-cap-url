##### -*- coding: utf-8 -*-
from selenium import webdriver
import os
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
# os.environ["LANG"] = "en_US.UTF-8"
# Create a new cromedriver

# chromedriver_path = os.environ.get('CHROMEDRIVER_PATH')
# chromedriver_path = DRIVER_DIR
# print(chromedriver_path)
# (DRIVER_DIR

DRIVER_DIR = r'.\chromedriver.exe'

print(DRIVER_DIR)

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

strr = "pictures"

ln = ".\\" + strr
print(ln)

try:
    if not (os.path.isdir(ln)):
        os.makedirs(os.path.join(ln))
except OSError as e:
    if e.errno != e.errno.EEXIST:
        print(r"Failed to create directory!!!!!")
        raise
try:
    rf = open("address.txt", 'r')
except FileNotFoundError:
    print('파일이 없습니다.')
    os.system("Pause")
    exit(1)
# wf = open(fol, 'w')
i = 1
try:
    driver = webdriver.Chrome(DRIVER_DIR, chrome_options=options)
except:
    print('드라이버가 없거나 버전이 맞지 않습니다.')
    os.system("Pause")
    exit(1)
while True:
    line = rf.readline()
    print(line)
    if not line: break

    # wf.write(line)
    try:
        driver.implicitly_wait(3)
        driver.get(line)
        screenshot_name = strr + '\\' + str(i) + ".png"
        driver.save_screenshot(screenshot_name)
        print("end" + str(i))
        i = i + 1
    except Exception as e:
        print("error")

driver.quit()
os.system("Pause")

# Saves a .png file with name my_screenshot_name to the directory that
# you are running the program from.
