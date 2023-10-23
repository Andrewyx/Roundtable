from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_data(url) -> list:
    browser_options = ChromeOptions()
    browser_options.headless = True
    
    driver = Chrome(options=browser_options)
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "menu-day-contents.font-normal.height11")))
    listofdays = driver.find_elements(By.CSS_SELECTOR, ".menu-day-contents.font-normal.height11")
    
    #ListOfPage -> ListOfDay
    #produces 7 days for each page    


    data = []  

    for day in listofdays:
        dishes = day.find_elements(By.CSS_SELECTOR, ".food-name")
        for count, dish in enumerate(dishes):
            food_item = {
                f"dish{count}" : dish.get_attribute("textContent").replace("\\n", "").strip()
            }
            data.append(food_item)

    


    driver.quit()
    return data


def main():
    data = get_data("https://ubc.nutrislice.com/menu/ubc-gather-place-vanier-residence/gather-place-vanier-residence-lunch/print-menu/month/2023-10-22")
    print(f"here is my -> {data}")


if __name__ == '__main__':
    main()