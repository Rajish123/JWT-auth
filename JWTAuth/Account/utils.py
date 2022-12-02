from selenium.webdriver.common.by import By 
from selenium import webdriver

class Util:
    @staticmethod
    def scrapper():
        my_title = []
        my_price = []
        website = "https://www.daraz.com.np/flash-sale"
        driver = webdriver.Firefox(executable_path = '/home/rajish/Documents/GeckoDriver')
        driver.get(website)
        title = driver.find_elements(by = By.XPATH,value = '//div[@class="sale-title"]')
        for i in title:
            my_title.append(i.text)
        price = driver.find_elements(by = By.XPATH, value = '//div[@class="sale-price"]')
        for i in price:
            my_price.append(i.text)
        my_biglist = [{my_title[i]: my_price[i]} for i in range(len(my_title))]
        driver.quit()
        return my_biglist