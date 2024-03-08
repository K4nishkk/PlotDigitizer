from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def getElement(xpath):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.maximize_window()
driver.get("https://www.mongodb.com/docs/atlas/getting-started/")

signInLink = driver.find_element(By.XPATH, "//a[@href='https://account.mongodb.com/account/login']")
signInLink.click()

usernameInput = driver.find_element(By.XPATH, "//input[@name='username']")
usernameInput.send_keys("nishtha462@gmail.com")

time.sleep(2)
usernameButton = driver.find_element(By.XPATH, "//button[@name='login']")
usernameButton.click()

input()

url = driver.current_url

projectButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='project-select-trigger']")))
projectButton.click()

newProjectButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='project-select-add-new-project']")))
newProjectButton.click()

projectName = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='projectName']")))
projectName.send_keys("Meow21")

time.sleep(5)
newProjectNameButton = driver.find_element(By.XPATH, "//button[@name='next']")
newProjectNameButton.click()

# same button attribute to create new project
time.sleep(5)
newProjectNameButton = driver.find_element(By.XPATH, "//button[@name='next']")
newProjectNameButton.click()

createCluster = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='create-cluster-button']")))
createCluster.click()

choseM0 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='radio-box-47']"))) # radio button for choice b/w M0, M2, M5
choseM0.click()

clickButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='primary-cta']")))
clickButton.click()

passwordInput = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='textinput-14']")))
passwordInput.send_keys("qwerQWERasdfASDF")

createUser = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@name='create-user']")))
createUser.click()

continueButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='continueButton']")))
continueButton.click()

networkAccess = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#/security/network']")))
networkAccess.click()

addIP = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#/security/network/accessList/addToAccessList']")))
addIP.click()

allowAccess = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@name='allowAccessAnywhere']")))
allowAccess.click()

confirmButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@name='confirm']")))
confirmButton.click()

databaseLink = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#/clusters']")))
databaseLink.click()

connectButton = getElement("//button[@data-testid='js-connect']")
connectButton.click()

mongoDrivers = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button .button-is-descriptive .cluster-connect-modal-option-button")))
mongoDrivers.click()