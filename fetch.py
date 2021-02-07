import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

user_info = {}
filename = 'settings.json'
with open(filename,'r') as f_obj:
    user_info = json.load(f_obj)

browser = webdriver.Chrome(ChromeDriverManager().install())

# login
browser.get('https://student.amizone.net')
username_field = browser.find_element_by_name('_UserName')
username_field.send_keys(user_info['id'])
password_field = browser.find_element_by_name('_Password')
password_field.send_keys(user_info['password'])
login_button = browser.find_element_by_class_name("login100-form-btn")
login_button.click()

# remove modals
# elem = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="myModal"]/div/div/div[1]/button')))
# action = ActionChains(browser)
# action.move_to_element(elem).move_by_offset(250, 0).click().perform()

# fetch time-table
elem = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="calendar"]/div[1]/div[1]/div/button[1]')))
action = ActionChains(browser)
action.move_to_element(elem).click().perform()
action.move_to_element(elem).click().perform()

time_table = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="calendar"]/div[2]/div/div/table/tbody/tr[2]/td[3]/a')))









































































# TODO
# fetch the time-table 
# store it in data.py and settings.py with corresponding code for MSTEAMS
# and display it usign GUI(https://pysimplegui.readthedocs.io/en/latest/screenshots_demos/)
# create subprocess for MSTEAMS
# absent message to be sent to respective faculty with the default text
# settings.py 
# data.py will contain today's time-table
# use opencv to detect button in MSTEAMS (https://stackoverflow.com/questions/63442967/best-way-to-detect-gui-buttons-using-a-image-file-as-reference-in-python-opencv)
