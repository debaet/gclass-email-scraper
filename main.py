from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import options


chrome_options = Options()
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("user-data-dir=C:\\Users\\gabri\\AppData\\Local\\Google\\Chrome\\User Data\\")
options.add_argument('--profile-directory=Profile 29') #Path to your chrome profile

driver = webdriver.Chrome(options=options, executable_path=r'C:\Program Files (x86)\Chrome\Application\chromedriver.exe')



def main():
	link = input('Enter Google Classroom Persons link. link must have sort-last-name at the end: ')
	driver.get(link)
	time.sleep(5)
	for a in driver.find_elements_by_xpath('.//a'):
	    print(a.get_attribute('href'))

while True:
	main()
	restart = input('Do you want to scrape another class?: ')
	if restart=="yes":
		main()

	elif restart=="y":
		main()

	elif restart=="Y":
		main()

	else:
		print('exit code. thank you for using.')
		driver.quit()
