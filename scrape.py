from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

desc=[]

chrome_options = Options()
chrome_options.add_argument('--headless') 
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/view/software-engineer-machine-learning-at-resonate-3804393239?refId=J9XR3L1ljY2zcdkehxRmIQ%3D%3D&trackingId=8QdNIl4rGqOe9nbstuzmyQ%3D%3D&trk=public_jobs_people-also-viewed")

HeaderName = driver.find_element(By.XPATH,"/html/body/main/section[1]/div/section[2]/div/div[1]/div/h1")
desc.append(HeaderName.text)

SearchElement = driver.find_element(By.XPATH,'/html/body/main/section[1]/div/div')
ClickButton  = SearchElement.find_element(By.TAG_NAME, 'button').click()
driver.implicitly_wait(2)
ListItems = SearchElement.find_elements(By.CSS_SELECTOR,'ul li')


for Item in ListItems:
    desc.append(Item.text)

driver.quit()

print("\n")
print("JOB ALERT!!!!!")
print("\n")
for x in desc:
    print(x)
print("\n")