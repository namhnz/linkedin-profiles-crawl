from selenium import webdriver;
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By
from time import sleep;

s=Service(ChromeDriverManager().install())
op = webdriver.ChromeOptions();
op.add_argument(r"start-maximized");
driver = webdriver.Chrome(service=s)
driver.maximize_window()

# Dang nhap vao LinkedIn
driver.get(r"https://www.linkedin.com/login");
sleep(3);

emailValue = "";
passwordValue = "";

with open("credential.txt", "r") as cre:
    emailValue = cre.readline().strip();
    passwordValue = cre.readline().strip();

emailInput = driver.find_element(By.ID, "username");
emailInput.send_keys(emailValue);
print("Da nhap xong email");
sleep(1);

passwordInput = driver.find_element(By.ID, "password");
passwordInput.send_keys(passwordValue);
print("Da nhap xong password");
sleep(1);

signInButton = driver.find_element(By.XPATH, r'//*[@id="organic-div"]/form/div[3]/button');
signInButton.click();
print("Da nhan nut sign in");
sleep(5);

# Thuc hien chuc nang tim kiem
searchBoxInput = driver.find_element(By.XPATH, r'//*[@id="global-nav-typeahead"]/input');
searchBoxInput.send_keys("tech engineer person");
searchBoxInput.send_keys(Keys.ENTER);
sleep(10)

