from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration import Data

def test_add_to_cart_button_presence(driver):

    driver.get(Data.LINK + "/catalogue/coders-at-work_207/")

    try:
        element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"))
        )

        print("Текст элемента кнопки:", element.text)

    except Exception as e:
        raise AssertionError("Элемент не найден:", e)
