import time
import requests
import json
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MsRewards():
    def __init__(self):
        self.driver = webdriver.Edge(executable_path=r'YOURPATHHERE')
        
    def _get_words(self):
        response = requests.get("https://random-word-api.herokuapp.com/word?number=450").text
        self.word_list = json.loads(response)
        
    def _teardown_method(self):
        self.driver.quit()
        
    def _rewards(self):
        self.driver.get("https://www.bing.com/?cc=de")
        self.driver.set_window_size(1517, 1060)
        counter = 0
        
        time.sleep(5)
        
        while counter < 24:
            self.driver.find_element(By.ID, "sb_form_q").click()
            self.driver.find_element(By.ID, "sb_form_q").clear()
            self.driver.find_element(By.ID, "sb_form_q").send_keys(random.choice(self.word_list), Keys.ENTER)
            counter += 1

if __name__ == '__main__':
    automat = MsRewards()
    automat.__init__()
    automat._get_words()
    automat._rewards()
    automat._teardown_method()