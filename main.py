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
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "menu-week-container")))
    books = driver.find_elements(By.CSS_SELECTOR, ".menu-week-container")
    print(books)
    data = [books]
    # for book in books:
    #     title = book.find_element(By.CSS_SELECTOR, "h3 > a")
    #     price = book.find_element(By.CSS_SELECTOR, ".price_color")
    #     stock = book.find_element(By.CSS_SELECTOR, ".instock.availability")
    #     book_item = {
    #         'title': title.get_attribute("title"),
    #         'price': price.text,
    #         'stock': stock. text
    #     }
    #     data.append(book_item)

    driver.quit()
    return data


def main():
    data = get_data("https://ubc.nutrislice.com/menu/ubc-gather-place-vanier-residence/gather-place-vanier-residence-breakfast/print-menu/month/2023-10-22")
    print(f"here is my -> {data}")


if __name__ == '__main__':
    main()