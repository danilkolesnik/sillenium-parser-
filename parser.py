from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

url = ("https://visualobjects.com/pl/web-design")

links = []

# collecting links from page


def data_collection(url):
    driver.get(url=url)
    time.sleep(3)
    for link in driver.find_elements_by_class_name("details-title"):
        links.append(link.get_attribute('href'))


btnurl = '#__layout > div > div > div.company-list-section.content > div.base-pagination > a'
btnurl2 = '#__layout > div > div > div.company-list-section.content > div.base-pagination > a:nth-child(3)'


def button_click():
    button = driver.find_element_by_css_selector(
        btnurl)
    # __layout > div > div > div.company-list-section.content > div.base-pagination > a:nth-child(3)
    button.click()
    time.sleep(1)


# IWebDriver driver = new FirefoxDriver();
# String currentURL = driver.Url
i = 0
try:
    for i in range(5):
        if i >= 1:
            btnurl = btnurl2
        data_collection(url)
        time.sleep(1)
        button_click()
        url = driver.current_url
    # print('\n'.join(links))
    with open("Results.txt", "w") as file:
        for link in links:
            print(link, file=file, sep="\n \n")

except Exception as Ex:
    print(Ex)
finally:
    driver.close()
    driver.quit()
