from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless') 
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.linkedin.com/jobs/view/software-developer-junior-at-caci-international-inc-3814637236?refId=%2FR9%2FHwh%2BpN6aZp57NtghBg%3D%3D&trackingId=G0Hc%2BdTOKvokxvDSxfUpDA%3D%3D&trk=public_jobs_people-also-viewed")

header = driver.find_element(By.XPATH,"/html/body/main/section[1]/div/section[2]/div/div[1]/div/h1")
print(header.text)

HeadingName = driver.find_element(By.XPATH,"/html/body/main/section[1]/div/div/section[2]/div/div")
ShowMore = driver.find_element(By.XPATH,"/html/body/main/section[1]/div/div/section[2]/div/div/section/button[1]").click()
ListItems = HeadingName.find_elements(By.CSS_SELECTOR,'ul li')

for Item in ListItems:
    print(Item.text)
    
time.sleep(2)

driver.quit()
