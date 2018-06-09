from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json


f = open("../creds.json", "r", encoding="utf-8")
creds = json.load(f)
login = creds["login"]
password = creds["password"]

chrome = webdriver.Chrome()
chrome.get("https://ap-emias.mos.ru")

elements = {}


def is_loading():
	return WebDriverWait(chrome, 40).until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[3]')))
	

def wait_for_element(xpath):
	return WebDriverWait(chrome, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))


try:
	is_loading()
	elements["Логин"] = wait_for_element('//input[@id="login"]')
	elements["Пароль"] = wait_for_element('//input[@id="password"]')
	elements["Логин"].send_keys(login)
	elements["Пароль"].send_keys(password)
	elements["Войти"] = wait_for_element('/html/body/div[2]/div/div[2]/div/form/div[3]/div[2]/button')
	elements["Войти"].click()
	is_loading()
finally:
	is_loading()
	elements["Левое меню"] = wait_for_element('/html/body/div[2]/div[1]/div[1]/div')
	elements["Левое меню"].click()
	is_loading()

#try:
	#elements["АРМ Главного врача"] = wait_for_element('/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/ul/li[1]/div/a')
	#elements["АРМ Главного врача"].click()
	#elements["Качество расписания врача"] = wait_for_element('/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/ul/li[1]/ul/li[2]/div/a')
	#elements["Качество расписания врача"].click()
	#elements["Количество записей и направлений, созданных врачом"] = wait_for_element('/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/ul/li[1]/ul/li[2]/ul/li[4]/div/a')
	#elements["Количество записей и направлений, созданных врачом"].click()
#finally:
	#elements["Фильтр"] = wait_for_element('/html/body/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div/div[1]/div/div[5]/a')
	#elements["Фильтр"].click()