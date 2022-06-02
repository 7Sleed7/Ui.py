from selenium import webdriver
import time


url = "http://suninjuly.github.io/simple_form_find_task.html"
driver = webdriver.Chrome(executable_path = "chromedriver.exe")

first_name = "Dmitrii"
last_name = "Bessarab"
city = "Lugano"
country = "Shwitzerland"


try:
	driver.get(url=url)

	driver.execute_script(f"document.querySelector('.form-group:nth-child(1) input').value = '{first_name}';")
	driver.execute_script(f"document.querySelector('.form-group:nth-child(2) input').value = '{last_name}';")
	driver.execute_script(f"document.querySelector('.form-group:nth-child(3) input').value = '{city}';" )
	driver.execute_script(f"document.querySelector('.form-group:nth-child(4) input').value = '{country}';")

	driver.execute_script(f"document.querySelector('#submit_button').click() ;" )

except Exception as ex:
	print(ex)

finally:
	driver.close()
	driver.quit()