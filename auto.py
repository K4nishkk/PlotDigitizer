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

for i in range(40, 42):

    projectButton = getElement("//button[@data-testid='project-select-trigger']")
    projectButton.click()

    newProjectButton = getElement("//a[@data-testid='project-select-add-new-project']")
    newProjectButton.click()

    projectName = getElement("//input[@name='projectName']")
    projectName.send_keys("Meow" + str(i))

    time.sleep(10)
    newProjectNameButton = driver.find_element(By.XPATH, "//button[@name='next']")
    newProjectNameButton.click()

    # same button attribute to create new project
    time.sleep(10)
    newProjectNameButton = driver.find_element(By.XPATH, "//button[@name='next']")
    newProjectNameButton.click()

    createCluster = getElement("//button[@data-testid='create-cluster-button']")
    createCluster.click()

    choseM0 = getElement("//div[@data-testid='template-inner-card-m0']") # radio button for choice b/w M0, M2, M5
    choseM0.click()

    clickButton = getElement("//button[@data-testid='primary-cta']")
    clickButton.click()

    passwordInput = getElement("//input[@id='textinput-14']")
    passwordInput.send_keys("qwerQWERasdfASDF")

    createUser = getElement("//button[@name='create-user']")
    createUser.click()

    continueButton = getElement("//button[@data-testid='continueButton']")
    continueButton.click()

    networkAccess = getElement("//a[@href='#/security/network']")
    networkAccess.click()

    addIP = getElement("//a[@href='#/security/network/accessList/addToAccessList']")
    addIP.click()

    allowAccess = getElement("//button[@name='allowAccessAnywhere']")
    allowAccess.click()

    confirmButton = getElement("//button[@name='confirm']")
    confirmButton.click()

    # databaseLink = getElement("//a[@href='#/clusters']")
    # databaseLink.click()

    # connectButton = getElement("//button[@data-testid='js-connect']")
    # connectButton.click()

    # mongoDrivers = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button .button-is-descriptive .cluster-connect-modal-option-button")
    # mongoDrivers.click()
