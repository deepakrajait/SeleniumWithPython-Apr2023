from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://www.saucedemo.com")

# Verify Swag Labs Text on Login Windows
we_swag_labs=driver.find_element(By.CLASS_NAME,"login_logo").text
assert we_swag_labs == 'Swag Labs'

we_username=driver.find_element(By.ID,"user-name")
we_username.send_keys("standard_user")

we_pwd=driver.find_element(By.ID,"password")
we_pwd.send_keys("secret_sauce")

we_login_bt=driver.find_element(By.ID,"login-button")
we_login_bt.click()

we_add_to_cart_bt=driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
we_add_to_cart_bt.click()

we_cart_icon=driver.find_element(By.CLASS_NAME,"shopping_cart_link")
we_cart_icon.click()

driver.implicitly_wait(3)

# Verify one item is added in cart
we_cart_quantity_text=driver.find_element(By.CLASS_NAME,"cart_quantity").text
assert we_cart_quantity_text == '1'

we_menu_icon=driver.find_element(By.ID,"react-burger-menu-btn")
we_menu_icon.click()

driver.implicitly_wait(2)
we_logout_bt=driver.find_element(By.ID,"logout_sidebar_link")
we_logout_bt.click()
