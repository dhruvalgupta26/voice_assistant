from selenium import webdriver

driver = None

def get_driver():
    global driver
    if not driver:
        driver = webdriver.Chrome()
    return driver

def login_to_website(username, password):
    driver = get_driver()
    driver.get('https://yourwebsite.com/login')
    
    user_field = driver.find_element_by_id('username')
    pass_field = driver.find_element_by_id('password')
    
    user_field.send_keys(username)
    pass_field.send_keys(password)
    
    login_button = driver.find_element_by_name('login')
    login_button.click()

def open_tab(tab_name):
    driver = get_driver()
    driver.find_element_by_link_text(tab_name).click()
