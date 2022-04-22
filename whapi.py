from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import os
import time



class whaDriver:
    qrPath="/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div/canvas"
    SearchBarPath='/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]'
    TextBoxPath = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]"
    MenuPath = "/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[3]/div/span"
    CloseSessionPath = "/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[3]/span/div/ul/li[4]/div[1]"
    MsgPath = "/html/body/div[1]/div/div/div[4]/div/div[3]/div/div[2]/div[3]/"
    
    loggedIn = False
    
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.get("https://web.whatsapp.com")
    
    def getQr(self):
        try:
            self.qrcode = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, self.qrPath)))
            print("QR code found")
            self.qrcode.screenshot(".qr.png")
            tmp = os.system("killall feh")
            tmp = os.system("feh .qr.png")
            
        except TimeoutException or NoSuchElementException:
            self.loggedIn = True
        
    def SendMsg(self, chatName, msg):
        try:
            self.SearchBar = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, self.SearchBarPath)))
            self.SearchBar.send_keys(chatName)
            time.sleep(0.5)
            self.Chat = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, "//span[@title ='{}']".format(chatName))))
            self.Chat.click()
            time.sleep(0.5)
            self.TextBox = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, self.TextBoxPath)))
            time.sleep(0.5)
            
            self.TextBox.send_keys(msg)
            self.TextBox.send_keys(Keys.RETURN)
        except TimeoutException or NoSuchElementException:
            print("Chat not found")
            time.sleep(1)
            
    def GetChatMsg(self, chatName):
        
        try:
            self.SearchBar = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, self.SearchBarPath)))
            self.SearchBar.send_keys(chatName)
            time.sleep(0.5)
            self.Chat = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, "//span[@title ='{}']".format(chatName))))
            self.Chat.click()
            time.sleep(0.5)
            i=1
            while True:
                try:
                    self.MessageList = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, self.MsgPath+"div[{}]".format(i))))
                    print(self.MessageList.text)        
                except TimeoutException or NoSuchElementException:
                    self.SearchBar.click()
                    self.SearchBar.send_keys(Keys.CONTROL + "a");
                    self.SearchBar.send_keys(Keys.DELETE);
                    break
                i+=1

        except TimeoutException or NoSuchElementException:
            
            print("Couldn't read chat")
            time.sleep(1)
        
        
        
        
    def CloseSession(self):
        self.Menu = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, self.MenuPath)))
        self.Menu.click()
        time.sleep(0.5)
        self.CloseButton = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, self.CloseSessionPath)))
        self.CloseButton.click()
        time.sleep(0.5)
        
        
    def close(self):
        self.driver.quit()

            
            
