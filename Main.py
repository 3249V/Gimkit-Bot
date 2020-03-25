from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time
import random

#gamecode = "51993"
questions = {}
upgrade_num = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 3, 2, 1, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
upgrade_cost = [10, 15, 50, 100, 150, 300, 1000, 1500, 2000, 10000, 12000, 15000, 75000, 85000, 115000, 300000, 450000,
                700000, 1000000, 1500000, 6500000, 10000000, 15000000, 65000000, 100000000, 200000000, 1000000000,
                10000000000000000000000000000000000000000]
upgrade_code = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]
wait = 0.15


class GimkitBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.step = -1
        #self.driver.set_window_position(0,-10000)
        # self.driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def join(self, gamecode):
        self.driver.get("https://www.gimkit.com/play")
        GC_in = self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div/div/div/form/input')
        GC_in.send_keys(gamecode)
        join_button = self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div/div/div/div')
        join_button.click()
        time.sleep(2)
        GC_in.send_keys("Your Name " + str(random.randint(1, 100)))
        join_button.click()

    def next(self):
        nexta = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div[1]/div[2]/div/div/div/div[2]/span[2]/div/div/div')
        nexta.click()
        time.sleep(wait)

    def main_act(self):
        self.step = 0
        question = self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div/div/div')
        self.question_text = question.text


        b1a = self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div')
        b2a = self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div')
        b3a = self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div/div[2]/div[3]/div/div/div')
        b4a = self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div/div[2]/div[4]/div/div/div')
        b1a_text = b1a.text
        b2a_text = b2a.text
        b3a_text = b3a.text
        b4a_text = b4a.text
        time.sleep(0.1)
        if not self.question_text in questions:
            questions[self.question_text] = ""
            b1a = self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div')
            b1a.click()
            self.clicked = b1a_text
        else:
            correct = questions[self.question_text]
            print(questions[self.question_text])
            if b1a_text == correct:
                clicked = b1a_text
                b1a = self.driver.find_element_by_xpath(
                    '//*[@id="root"]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div')
                b1a.click()
            elif b2a_text == correct:
                clicked = b2a_text
                b2a = self.driver.find_element_by_xpath(
                    '//*[@id="root"]/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div')
                b2a.click()
            elif b3a_text == correct:
                clicked = b3a_text
                b3a = self.driver.find_element_by_xpath(
                    '//*[@id="root"]/div[1]/div[2]/div/div/div[2]/div[3]/div/div/div')
                b3a.click()
            elif b4a_text == correct:
                clicked = b4a_text
                b4a = self.driver.find_element_by_xpath(
                    '//*[@id="root"]/div[1]/div[2]/div/div/div[2]/div[4]/div/div/div')
                b4a.click()
        self.Response()

    def Response(self):
        self.step = 1
        time.sleep(wait)
        r_o_w = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div[1]/div[2]/div/div/div/div[2]/span[1]/div/div/div')
        if r_o_w.text == "View Correct Answer":
            print("Wrong")
            r_o_w.click()
            time.sleep(wait)
            right_answer = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div')
            questions[self.question_text] = right_answer.text
            ahhh = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div[1]/div[2]/div/div/div/div[2]/span/div/div/div')
            ahhh.click()
        else:
            print("right")
            questions[self.question_text] = self.clicked
            self.upgrade()

    def upgrade(self):
        self.step = 2
        money = self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div[2]/div[2]/div')
        money_text = money.text.replace('$', '')
        if int(money_text.replace(',', '')) >= upgrade_cost[0]:
            shop = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div[1]/div[2]/div/div/div/div[2]/span[1]/div/div/div')
            shop.click()
            self.step = 3
            time.sleep(wait)
            upgrade = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[' + str(upgrade_num[0]) + ']')
            upgrade.click()
            time.sleep(wait + 0.5)
            spend = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div[1]/div[2]/div/div/div[2]/div[' + str(upgrade_code[0]) + ']/div/div')
            spend.click()
            purchase = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div/div[3]/div/div')
            purchase.click()
            time.sleep(0.1)
            exit = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[4]')
            exit.click()
            time.sleep(0.1)
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
                time.sleep(15)

                menu = self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/button[1]')
                menu.click()
                back = self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/nav/span[1]/div')
                back.click()
                self.start()




#bot = GimkitBot()
#bot.join()
#time.sleep(2)
#bot.start()
