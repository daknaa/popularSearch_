from tkinter import *
from selenium import webdriver

url=""

chrome_option = webdriver.ChromeOptions()
search_option = webdriver.ChromeOptions()
#SecretMode, HideWindow
chrome_option.add_argument("--incognito")
chrome_option.add_argument("headless")
search_option.add_argument("--incognito")
driver = webdriver.Chrome("chromedriver.exe", options=chrome_option)


def getWord(event):
	global url
	url = Entry.get(entry)
	driver.get(url)

	#popular10 = []
	elements = driver.find_elements_by_css_selector("div.popularSearches > a")
	count = len(elements)
	for i in range(0, count):
		popular10 = elements[i].get_attribute('innerText')
		listbox.insert(END, popular10)

	driver.close()

def inSearch(event):
	value_idx = listbox.curselection()
	#예외 처리
	if (len(value_idx) == 0):
		return
	value = listbox.get(value_idx[0])
	temp = value.replace(" ", "+")
	webdriver.Chrome("chromedriver.exe", options=search_option).get(url + "/video/search?search=" + temp)

root = Tk()
root.title("trending")
root.geometry("300x300")
root.resizable(False, False)

entry = Entry(root)
entry.insert(END, "https://pornhub.com")
listbox = Listbox(root, selectmode='single')

entry.pack()
listbox.pack()

root.bind('<Return>', getWord)
root.bind('<Button>', inSearch)


root.mainloop()