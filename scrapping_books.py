import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Definir la URL de la página web
url = "https://www.booktegi.eus/liburuak/"

# Hacer una petición GET a la URL y obtener el contenido HTML
response = requests.get(url)
html = response.text
driver.get(url)

onartu = driver.find_element(By.XPATH, value='//*[@id="cmplz-cookiebanner-container"]/div/div[6]/button[1]')
onartu.click()
time.sleep(2)

elements = driver.find_elements(By.CSS_SELECTOR,value="a[class=ikusi]")

for lib in elements:
    lib.click()

    pdf = driver.find_element(By.XPATH, value='/html/body/div[2]/div/main/article/div[1]/div/div[2]/div[3]/div[4]/a')
    if pdf.text == 'PDF':
        #pdf.click()
        print('impreso')
        driver.back()
#print(link)
