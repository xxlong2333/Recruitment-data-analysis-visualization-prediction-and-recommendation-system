from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import csv
import pandas as pd
import re


class spider(object):
    def __init__(self,type,city,page):
        self.type = type
        self.city = city
        self.page = page
        self.spiderUrl = 'https://www.lagou.com/wn/jobs?fromSearch=true&kd=%s&city=%s&pn=%s'

    def startBrowser(self):
        service = Service('./chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.debugger_address='localhost:9222'
        browser = webdriver.Chrome(service=service, options=options)
        return browser


    def main(self,page):
        if self.page > page: return
        print(self.page)
        browser = self.startBrowser()
        print("正在爬取页码路径："+self.spiderUrl%(self.type,self.city,self.page))
        browser.get(self.spiderUrl%(self.type,self.city,self.page))
        time.sleep(1)
        job_list = browser.find_elements(by=By.XPATH, value='//div[@id="jobList"]/div[@class="list__YibNq"]/div[@class="item__10RTO"]')
        print(job_list)
        print(len(job_list))

        for index, job in enumerate(job_list):
            try:
                # title
                title = job.find_element(by=By.XPATH, value='.//div[@class="p-top__1F7CL"]/a').text
                # companyTitle
                companyTitle = job.find_element(by=By.XPATH, value='.//div[@class="company-name__2-SjF"]/a').text
                # salary
                salary = job.find_element(by=By.XPATH, value='.//div[@class="p-bom__JlNur"]/span').text
                salary = re.findall('\d+', salary)
                minSalary = int(salary[0]) * 1000
                maxSalary = int(salary[1]) * 1000
                # workExperience
                # education
                double = job.find_element(by=By.XPATH, value='.//div[@class="p-bom__JlNur"]').get_attribute(
                    'textContent').split('/')
                workExperience = double[0].split('k')[2].strip()
                education = double[1].strip()

                try:
                    # totalTag
                    totalTag = job.find_element(by=By.XPATH,
                                                value='.//div[@class="company__2EsC8"]/div[@class="industry__1HBkr"]').text

                    companyPeople = re.findall('\d+', totalTag)
                except:
                    totalTag = '无'
                    companyPeople = [10]

                try:
                    # companyPeople[1]
                    companyPeople = '-'.join(companyPeople)
                except:
                    companyPeople = [0]
                # tagList
                tagList = job.find_elements(by=By.XPATH, value='.//div[@class="ir___QwEG"]/span')
                tagData = []
                for tag in tagList:
                    tagData.append(tag.text)
                workTag = '/'.join(tagData)
                # welfare
                try:
                    welfare = job.find_element(by=By.XPATH, value='.//div[@class="il__3lk85"]').text.replace('“', "")
                    welfare = welfare.replace('”', "")
                except:
                    welfare = '无'
                imgSrc = job.find_element(by=By.XPATH, value='.//div[@class="com-logo__1QOwC"]/img').get_attribute(
                    'src')
                print(imgSrc)
                print(title, companyTitle, minSalary, maxSalary, workExperience, education, totalTag, companyPeople,
                      workTag, welfare)
                self.saveData(
                    [self.type, title, companyTitle, minSalary, maxSalary, workExperience, education, totalTag,
                     companyPeople,
                     workTag, welfare, imgSrc, self.city])
            except:
                print("error")
                continue
        self.page += 1
        time.sleep(1)
        self.main(page)

    def saveData(self,data):
        with open('../spark/jobData.csv', 'a', newline='', encoding='utf-8') as wf:
            writer = csv.writer(wf)
            writer.writerow(data)

    def init(self):
        if not os.path.exists('../spark/jobData.csv'):
            with open('../spark/jobData.csv', 'w', encoding='utf-8', newline='') as wf:
                writer = csv.writer(wf)
                writer.writerow(
                    ['type','title', 'companyTitle', 'minSalary', 'maxSalary', 'workExperience', 'education',
                     'totalTag',
                     'companyPeople','workTag', 'welfare','imgSrc','city'])


if __name__ == '__main__':
    spiderobj = spider('java','北京',1)
    spiderobj.init()
    #spiderobj.main(1)
   #  cityList = ['北京','上海','广州','深圳','杭州','苏州', '成都','南京','武汉','长沙']
   #  typeList = ['java','web前端','C语言','php开发','数据分析师','软件测试','IT运维','微信小程序','.NET']
   #  for city in cityList:
   #      for type in typeList:
   #          spiderobj = spider(type,city,1)
   #          spiderobj.main(10)
