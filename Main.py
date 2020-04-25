from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time
import random

questions = {}
upgrade_num = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 3, 2, 1, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
upgrade_cost = [10, 15, 50, 100, 150, 300, 1000, 1500, 2000, 10000, 12000, 15000, 75000, 85000, 115000, 300000, 450000,
                700000, 1000000, 1500000, 6500000, 10000000, 15000000, 65000000, 100000000, 200000000, 1000000000,
                10000000000000000000000000000000000000000]
upgrade_code = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]
wait = 0.3


class GimkitBot():
    def __init__(self, gc, name):
        self.driver = webdriver.Chrome()

        self.join(gc, name)
        time.sleep(2)
        self.start()

    def join(self, gamecode, name):
        self.driver.get("https://www.gimkit.com/play")
        time.sleep(3)
        GC_in = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div[2]/div/div/div/div/form/input')
        GC_in.send_keys(gamecode)
        join_button = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div[2]/div/div/div/div/div')
        join_button.click()
        time.sleep(5)
        GC_in.send_keys(name)
        join_button.click()

    def next(self):
        nexta = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div[1]/div[2]/div/div/div/div[2]/span[2]/div/div/div')
        nexta.click()
        time.sleep(wait)

    def gopt(self, o):
        # get answer for o as option key.
        return self.driver.find_element_by_xpath(f'//*[@id="root"]/div/div/div/div[1]/div[2]/div/div/div[2]/div[{o}]/div/div/div/div')

    def main_act(self):
        question = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div/div/div')
        self.question_text = question.text

        b1a_text = self.gopt(1).text
        b2a_text = self.gopt(2).text
        b3a_text = self.gopt(3).text
        b4a_text = self.gopt(4).text
        time.sleep(0.1)
        if not self.question_text in questions:
            questions[self.question_text] = ""
            self.gopt(1).click()
            self.clicked = b1a_text
        else:
            correct = questions[self.question_text]
            if b1a_text == correct:
                self.clicked = b1a_text
                self.gopt(1).click()
            elif b2a_text == correct:
                self.clicked = b2a_text
                self.gopt(2).click()
            elif b3a_text == correct:
                self.clicked = b3a_text
                self.gopt(3).click()
            elif b4a_text == correct:
                self.clicked = b4a_text
                self.gopt(4).click()
        self.Response()

    def Response(self):
        time.sleep(wait)
        r_o_w = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div[1]/div[2]/div/div/div/div[2]/span[1]/div/div/div')
        if r_o_w.text == "View Correct Answer":
            r_o_w.click()
            time.sleep(wait)
            right_answer = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div')
            questions[self.question_text] = right_answer.text
            ahhh = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div/div[1]/div[2]/div/div/div/div[2]/span/div/div/div')
            ahhh.click()
        else:
            questions[self.question_text] = self.clicked
            self.upgrade()

    def upgrade(self):
        money = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div')
        money_text = money.text.replace('$', '')
        money_text = money_text.replace(',', '')
        if int(money_text) >= upgrade_cost[0]:
            shop = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div/div[1]/div[2]/div/div/div/div[2]/span[1]/div/div/div')
            shop.click()
            time.sleep(wait)
            upgrade = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div/div[1]/div[2]/div/div/div[1]/div[' + str(upgrade_num[0]) + ']')
            upgrade.click()
            time.sleep(wait + 0.5)
            spend = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div/div[1]/div[2]/div/div/div[2]/div[' + str(upgrade_code[0]) + ']/div/div')
            spend.click()
            '//*[@id="root"]/div/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div'
            '//*[@id="root"]/div/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div/div'
            purchase = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[3]/div/div')
            purchase.click()
            time.sleep(0.5)
            exit = self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[4]')
            exit.click()
            time.sleep(0.2)
            del upgrade_code[0]
            del upgrade_num[0]
            del upgrade_cost[0]
        else:
            self.next()

    def start(self):
        while 1:

            try:
                time.sleep(wait)
                self.main_act()
            except (ElementClickInterceptedException, NoSuchElementException):
                time.sleep(0.5)
                try:
                    attacker = self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div/div/div[2]')
                    print(attacker.text[2])
                except:
                    pass
                time.sleep(3)
                try:
                    menu = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div[1]/div/div/button[1]')
                    menu.click()
                    back = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/nav/span[1]/div')
                    back.click()
                except:
                    print("Something is blocking the game. Are you iced? In the waiting room?")
                self.start()
