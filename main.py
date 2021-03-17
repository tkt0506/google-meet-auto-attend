from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
import schedule
from selenium.webdriver.common.action_chains import ActionChains
import tkinter as tk
import tkinter.messagebox as tmsg
import os
import csv
from win10toast import ToastNotifier
import webbrowser

def main(code):
    
    toaster.show_toast("lesson", f"the lesson code is:{code}")
    driver = webdriver.Chrome(r"C:/Program Files/Google/Chrome/Application/chromedriver")
    options = webdriver.ChromeOptions()
    options.addPreference("permissions.default.microphone", 1)
    options.addPreference("permissions.default.camera", 1)

    driver.get("https://meet.google.com/landing?authuser=1")

    element_1 = driver.find_element_by_name("identifier")
    element_1.send_keys("sms24112@stmarks.edu.hk")
    element_1.send_keys(Keys.CONTROL,'\ue007')
    time.sleep(4)

    element_2 = driver.find_element_by_name("password")
    element_2.send_keys("0721720200")
    element_2.send_keys(Keys.CONTROL,'\ue007')
    time.sleep(4)

    element_3 = driver.find_element_by_id("i3")
    element_3.send_keys(code)
    element_3.send_keys(Keys.CONTROL,'\ue007')
    time.sleep(4)

    actions = ActionChains(driver)
    actions.send_keys(Keys.LEFT_CONTROL + 'd')
    actions.send_keys(Keys.LEFT_CONTROL + 'e')
    element_4 = driver.find_elements_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
 
   

def end():
    element_5 = driver.find_elements_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]')
    while True:
      if int(element_5.text) > 10 :
           driver.close()     
      else:
          sleep(10)

if __name__ == "__main__":

    toaster = ToastNotifier()

    if os.path.exists("data.csv"):
        with open('data.csv',newline='') as file:
            rows = csv.reader(file)
            for row in rows:
                if row[2] == "1":
                     schedule.every().monday.at(row[0]).do(main , row[1])
                     schedule.every().monday.at(row[0]).do(end , row[3])
                elif row[2] == "2":
                     schedule.every().tuesday.at(row[0]).do(main , row[1])
                     schedule.every().tuesday.at(row[0]).do(end, row[3])
                elif row[2] == "3":
                     schedule.every().wednesday.at(row[0]).do(main , row[1])
                     schedule.every().wednesday.at(row[0]).do(end , row[3])
                elif row[2] == "4":
                     schedule.every().thursday.at(row[0]).do(main , row[1])
                     schedule.every().thursday.at(row[0]).do(end , row[3])
                elif row[2] == "5":
                     schedule.every().friday.at(row[0]).do(main , row[1])
                     schedule.every().friday.at(row[0]).do(end , row[3])
                elif row[2] == "6":
                     schedule.every().saturday.at(row[0]).do(main , row[1])
                     schedule.every().saturday.at(row[0]).do(end , row[3])
                elif row[2] == "7":
                     schedule.every().sunday.at(row[0]).do(main , row[1])
                     schedule.every().sunday.at(row[0]).do(end , row[3])
                else:
                    toaster.show_toast("error", "excel wrong enter!")

            while True:
                schedule.run_pending()
                time.sleep(1)        
   

    else:
        window = tk.Tk()
        window.Title = "setting"
        window.geometry("600x400")

        label1 = tk.Label(window ,text="as i am lazy to make , you just go to the excel file (data.csv)  ")
        label1.place(x=0 , y=0)

        label2 = tk.Label(window ,text="and add the schedule (time(Ex:08:00) ,code ,week(1-5) and ending time)")
        label2.place(x=0 , y=100)

        label3 = tk.Label(window ,text="after that save it and reload the code")
        label3.place(x=0 , y=200)



        with open('data.csv',"w",newline="") as file:
          writer = csv.writer(file)

        webbrowser.open('data.csv')

        window.mainloop()    
