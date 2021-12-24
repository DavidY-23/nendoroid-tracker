from selenium import webdriver
from selenium.webdriver.common.by import By
totalNendo = []

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
def addingToArray(pageNum):
    global totalNendo
    className = pageNum.find_element(By.CLASS_NAME, 'hitList')
    x = className.text.split("\n")
    lengthOfX = len(x)
    mergeX = [x[i] + ' - ' + x[i+1] for i in range(0, lengthOfX-1, 2)]
    if lengthOfX % 2 == 1:
        mergeX.append(x[lengthOfX-1])
    totalNendo = totalNendo + mergeX

#grabs the first 1300 nendoroids
driver.get("https://www.goodsmile.info/en/nendoroid000-100")
addingToArray(driver)
driver.get("https://www.goodsmile.info/en/nendoroid101-200")
addingToArray(driver)
driver.get("https://www.goodsmile.info/en/nendoroid201-300")
addingToArray(driver)
driver.get("https://www.goodsmile.info/en/nendoroid301-400")
addingToArray(driver)
driver.get("https://www.goodsmile.info/en/nendoroid401-500")
addingToArray(driver)
driver.get("https://www.goodsmile.info/en/nendoroid501-600")
addingToArray(driver)
driver.get("https://www.goodsmile.info/en/nendoroid601-700")
addingToArray(driver)
driver.get("https://www.goodsmile.info/en/nendoroid701-800")
addingToArray(driver)
driver.get("https://www.goodsmile.info/en/nendoroid801-900")
addingToArray(driver)
driver.get("https://www.goodsmile.info/en/nendoroid801-900")
addingToArray(driver)
driver.get("https://www.goodsmile.info/en/nendoroid901-1000")
addingToArray(driver)
driver.get("https://www.goodsmile.info/en/nendoroid1001-1100")
addingToArray(driver)
driver.get("https://www.goodsmile.info/en/nendoroid1101-1200")
addingToArray(driver)
driver.get("https://www.goodsmile.info/en/nendoroid1201-1300")
addingToArray(driver)

print(totalNendo)

#print(driver.title)