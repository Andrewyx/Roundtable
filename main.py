from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date

def get_data(url) -> list:
    browser_options = ChromeOptions()
    browser_options.headless = True
    
    driver = Chrome(options=browser_options)
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "menu-day-contents.font-normal.height11")))
    listofdays = driver.find_elements(By.CSS_SELECTOR, ".menu-day-contents.font-normal.height11")
    

    data = []

    for count, day in enumerate(listofdays):
        dishes = day.find_elements(By.CSS_SELECTOR, ".food-name")
        menu = []
        for dish in dishes:
            food_item = dish.get_attribute("textContent").replace("\\n", "").strip()
            menu.append(food_item)
        if len(menu) > 0:
            day_menu = {
                f"Day {count + 1}" : menu
            }
            data.append(day_menu)

    driver.quit()
    return data


def main():
    data = get_data(f"https://ubc.nutrislice.com/menu/ubc-gather-place-vanier-residence/gather-place-vanier-residence-lunch/print-menu/month/{date.today()}")
    print(data[date.today().day])


if __name__ == '__main__':
    main()