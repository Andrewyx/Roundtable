from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import pickle
import pywhatkit
import os
import ast

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
    ListOfRecipients = ast.literal_eval(SOME_SECRET)
except KeyError:
    SOME_SECRET = "Token N/A"
    #add name number pairs below
    ListOfRecipients = {
    }

def send_to(ListOfNumber, info):
    for number in ListOfNumber:
        pywhatkit.sendwhatmsg_instantly(f"+1{ListOfRecipients[number]}", f'Menu Today: \n {str(info)}', 10, tab_close=True)

def get_data(url) -> list:
    browser_options = ChromeOptions()
    browser_options.add_argument("--headless=new")
    
    driver = Chrome(options=browser_options)
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "menu-day-contents.font-normal.height11")))
    listofdays = driver.find_elements(By.CSS_SELECTOR, ".menu-day-contents.font-normal.height11")
    

    data = {}
    for count, day in enumerate(listofdays):
        dishes = day.find_elements(By.CSS_SELECTOR, ".food-name")
        menu = []
        for dish in dishes:
            
            food_item = dish.get_attribute("textContent").replace("\\n", "").strip()
            menu.append(food_item)
        if len(menu) > 0:
            data[f'Day {count + 1}'] = menu

    driver.quit()
    return data


def main():
    try:
        file = open("menus.txt", "rb")
        cache = pickle.load(file)
        print(f'{date.today()}:\n {cache[f"Day {date.today().day}"]}')
        send_to(ListOfRecipients, cache[f"Day {date.today().day}"])
        file.close()

    except Exception as error:
        print(error)
        data = get_data(f"https://ubc.nutrislice.com/menu/ubc-gather-place-vanier-residence/gather-place-vanier-residence-lunch/print-menu/month/{date.today()}")
        print(f'{date.today()}:\n {data[f"Day {date.today().day}"]}')
        send_to(ListOfRecipients, data[f"Day {date.today().day}"])
        file = open("menus.txt", "wb")
        pickle.dump(data, file)
        file.close()


if __name__ == '__main__':
    main()