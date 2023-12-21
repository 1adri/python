from selenium import webdriver
import requests
from io import BytesIO
from PIL import Image
from selenium.webdriver.common.by import By
import time
import os
import pyautogui
from selenium.webdriver.common.keys import Keys
import pyperclip

# URL of the OCR website
ocr_website_url = "https://bengali.indiatyping.com/index.php/apps/ocr"

# Path to your webdriver executable (e.g., chromedriver.exe for Chrome)
webdriver_path = r"C:\Users\Adri\Desktop\python\preranaaudiolibrary\chromedriver-win64\chromedriver-win64\chromedriver.exe"
# Create a webdriver instance
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the OCR website
    driver.get(ocr_website_url)

    # Add code here to interact with the website if necessary (e.g., filling out forms)

    # Locate the image element (replace 'xpath' with the actual XPath of the image)
    image_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div/div/div/main/div/div[3]/div[2]/div[1]/div/div/main/div/div/div/div[2]/div[1]/div[1]/label')
    image_element.click()
    time.sleep(5)
    pyautogui.write('C:\\Users\\Adri\\Desktop\\python\\preranaaudiolibrary\\image7.png') 
    pyautogui.press('enter')
    time.sleep(5)
    convert_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div/div/div/main/div/div[3]/div[2]/div[1]/div/div/main/div/div/div/div[2]/div[2]/div[2]/button')
    driver.execute_script("arguments[0].scrollIntoView();", convert_element)
    time.sleep(5)

    convert_element.click()
    time.sleep(10)
    text_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div/div/div/main/div/div[3]/div[2]/div[1]/div/div/main/div/div/div/div[2]/div[4]/textarea')
    text_element.send_keys(Keys.CONTROL + 'a')  # Select all text
    text_element.send_keys(Keys.CONTROL + 'c')  # Copy selected text
    time.sleep(5)
    copied_text = pyperclip.paste()
    print(copied_text)
    # Get the source attribute of the image
    #image_src = image_element.get_attribute("src")

    # Download the image using requests
    #response = requests.get(image_src)
    
    # Open the image using PIL
    #image = Image.open(BytesIO(response.content))

    # Save or process the image as needed
    #image.save("output_image.png")

finally:
    # Close the webdriver
    driver.quit()
