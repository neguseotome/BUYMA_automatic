from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

login_addles = "hogehoge@mail.com"
login_pass = "hugahogepiyo"
# Chrome WebDriverを起動
driver = webdriver.Chrome()

def mouse_hover_id(hover_id):
    hover = driver.find_element(By.ID, hover_id)
    actions = ActionChains(driver)
    actions.move_to_element(hover).perform()


# バイマのログインページを開く
# リンクを開く
driver.get("https://www.buyma.com/login/")
texts = driver.find_element(By.ID, "txtLoginId")
texts.send_keys(login_addles)
driver.implicitly_wait(10)
texts = driver.find_element(By.ID, "txtLoginPass")
texts.send_keys(login_pass)
driver.implicitly_wait(10)
my_btn_id = driver.find_element(By.ID, "login_do")
my_btn_id.click()
driver.implicitly_wait(10)
# ログイン完了まで待機（適切な要素を待つなどの方法が必要）
time.sleep(5)