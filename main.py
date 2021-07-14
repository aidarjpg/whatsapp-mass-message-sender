from selenium import webdriver
import time
from datetime import datetime
import random

#+-+-+-+-+-+-+-+-+-+-+-+-+- GLOBAL DECLARATIONS +-+-+-+-+-+-+-+-+-
chat_name = ['name1','name2','etc']  #names of people you want to send the message to
messages = ['@32-1-s2l', '@g1-14-v-1'] #list of messages you want to send
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-++-+-+-+-

class WhatsAppBot():
	def __init__(self):
		#initialize the driver and open chrome
		self.driver = webdriver.Chrome()
		
	def login(self):
		#open the web.whatsapp website
		self.driver.get('https://web.whatsapp.com/')
		print("Please scan QR Once")
		#wait until the user scans the QR code
		while True:
			try:
				searchBox = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')
				print('Scanning Successful')
				#if search box is available then the user has Successfully scanned the QR so break 
				break
			except Exception as e:
				pass
			#check if the search box is available, every 1 second
			time.sleep(1)

	def searchChat(self, name):
			#get the search box
			searchBox = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')
			print('Opening search box...')
			#type in the required person's name
			searchBox.send_keys(name)
			#wait for 1 second to make sure everything renders properly
			time.sleep(10)

	def sendMessage(self, name):
		#look for the required chat name
		try:
			chat = self.driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
			print('Looking for '+ name)
			#click on the particular chat
			chat.click()
		except:
			print("Couldn't find user")
			chat_name.remove(i)
		#select the typing area/ chat box				
		chatBox = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]')
		print('Opening chat with '+ name)
		time.sleep(5)
		#type in the required message
		chatBox.send_keys('Test')
		#wait for 1 second to make sure that the send button renders
		time.sleep(1)
		#search the send button
		sendButton = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]/button')
		print('Sending the message...')
		#click the send button
		sendButton.click()

	def quit(self):
		self.driver.quit()

	def clearBox(self, name):
			#get the search box
			searchBox = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')
			print('Clearing search box...')
			#type in the required person's name
			searchBox.clear()
			#wait for 1 second to make sure everything renders properly
			time.sleep(1)
#make class object
bot = WhatsAppBot()
bot.login()

while len(chat_name)>0:
	for i in chat_name[:]:
		try:
			bot.searchChat(i)
			time.sleep(1)
			bot.sendMessage(i)
			time.sleep(5)
			chat_name.remove(i)
		except Exception as e:
			print("\n------ERROR------\n")
			print(e)
			bot.clearBox(i);
print('Messages were sent Successfully')
