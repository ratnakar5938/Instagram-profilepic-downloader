from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request
import time

driver = webdriver.Chrome()
driver.get(r"https://www.instagram.com/accounts/login/")

user = input("Enter your username: ")
textInput = driver.find_element_by_xpath(r"/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
textInput.send_keys(f'{user}')
password = input("Enter your password: ")
textInput = driver.find_element_by_xpath(r"/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")
textInput.send_keys(f"{password}")
loginBtn = driver.find_element_by_xpath(r"/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]")
loginBtn.click()
print("Logging in...")
time.sleep(10)

i = 0
while True:
    get_user = input("Enter username whose profile picture you want: ")
    # driver.get(r"https://www.instagram.com/aliaabhatt/")
    driver.get(fr"https://www.instagram.com/{get_user}/")
    body = driver.find_element_by_tag_name('body')
    page = body.get_attribute("innerHTML")

    soup = BeautifulSoup(page, "html.parser")
    userImageTag = soup.select(f'img[alt="{get_user}\'s profile picture"]')
    if not userImageTag:
        userImageTag = soup.select('.be6sR')
    print(userImageTag[0]["src"])
    request.urlretrieve(userImageTag[0]["src"], f"userprofile{i}.jpg")
    i += 1
    end = input("Enter exit to exit the program else just press any other key: ")
    if end == 'exit':
        driver.close()
        break