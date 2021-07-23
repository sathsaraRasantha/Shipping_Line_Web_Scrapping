try:
    from selenium import webdriver
    import csv
    import time
    from os import path
    from sys import exc_info
    import pyodbc
    import pandas as pd
    from sys import exc_info
    from pyautogui import screenshot
    import datetime as dt
    from datetime import datetime
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys



except ImportError as e:
    print("Exception (Error Log Import" + str(e))
try:
    from eErorHandle.errorlogger import errorLogger
except ModuleNotFoundError as e:
    print("Exception (ErrorLog Import) : " + str(e))

# confogurations
errorLogPath = "C:\\Users\\User\\PycharmProjects\\shippingLine\\logs\\Mersk\\errorlog.txt"
errorLog_screenshot = "C:\\Users\\User\PycharmProjects\\shippingLine\\screenshots\\error\\"
screenshotPath = "C:\\Users\\User\\PycharmProjects\\shippingLine\\screenshots\\Mersk\\"
path = "C:\selenium browser drivers\chromedriver.exe"
url = "https://www.maersk.com/tracking/?gclid=EAIaIQobChMI79Sigun68AIVykNgCh3l4AV2EAAYASAAEgLQs_D_BwE&gclsrc"
driver = webdriver.Chrome(r"C:\Users\Vevro\Downloads\chromedriver.exe")

def web_load():
    now = dt.now()
    formatted_date = now.strftime('%Y_%m_%d_%H_%M_%S')
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="coiPage-1"]/div[2]/button[3]'))).click()

        driver.implicitly_wait(60)
        time.sleep(3)
        driver.save_screenshot(screenshotPath + "MERSK_SA_FP_" + formatted_date + ".png")
    except Exception as e:
        exc_type, exc_obj, exc_tb = exc_info()
        fname = path.split(exc_tb.tb_frame.f_code.co_filename)[0]
        infoList = [fname, exc_tb.tb_lineno, exc_obj]
        print("Exception (web_load) : " + str(e))
        errorLogger(errorLogPath, e, infoList)
        # alert("Exception (web_load) : "+str(e))
    else:
        autoBooking()
def autoBooking():
    try:
        now = dt.now()
        formatted_date = now.strftime('%Y_%m_%d_%H_%M_%S')
        try:
            bookingid = 210262670
            searchBox = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located(
                    (By.ID, "trackShipmentSearch")))
            searchBox = driver.find_element_by_id("trackShipmentSearch")
            searchBox.send_keys(bookingid)
            searchBtn = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.ID, "trackShipmentSearch")))
            searchBtn = driver.find_element_by_id("trackShipmentSearch")
            searchBtn.send_keys(Keys.ENTER)
            driver.save_screenshot(screenshotPath + "MERSK_SA_FP_AUTO" + formatted_date + ".png")
        except:
            searchBox = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located(
                    (By.ID, "trackShipmentSearch")))
            searchBox = driver.find_element_by_id("trackShipmentSearch")
            searchBox.send_keys(bookingid)
            searchBtn = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.ID, "trackShipmentSearch")))
            searchBtn = driver.find_element_by_id("trackShipmentSearch")
            driver.save_screenshot(screenshotPath + "MERSK_SA_FP_AUTO" + formatted_date + ".png")

    except Exception as e:
        exc_type, exc_obj, exc_tb = exc_info()
        fname = path.split(exc_tb.tb_frame.f_code.co_filename)[0]
        infoList = [fname, exc_tb.tb_lineno, exc_obj]
        print("Exception (web_load) : " + str(e))
        errorLogger(errorLogPath, e, infoList)
        # alert("Exception (web_load) : "+str(e))
        screenshot(errorLog_screenshot + "automation.png")
        return False
    else:
        data_extractor()


def data_extractor():
    try:
        dataList = []

        try:
            now = dt.now()
            formatted_date = now.strftime('%Y_%m_%d_%H_%M_%S')
            dataList = []
            dataTable = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CLASS_NAME, "table_id")))
            dataTable = driver.find_elements_by_class_name('table_id')
            trows = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
            trows=dataTable[0].find_elements_by_tag_name("table")
            driver.save_screenshot(screenshotPath + "MERSK_SA_FP_DATA" + formatted_date + ".png")
        except:
            dataList = []
            dataTable = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.ID, "table_id")))
            dataTable = driver.find_elements_by_id('table_id')
            trows = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.TAG_NAME, "tr")))
            trows = dataTable[0].find_elements_by_tag_name("tr")
            '''
        for i in range(0, len(trows)):
            tdata = trows[i].find_element_by_tag_name("td")
            temp = tdata.text
            dataList.append(temp)
            print(dataList)
            '''
        ele = driver.find_element_by_xpath('//*[@id="table_id"]/tbody/tr/td[5]')
        total_height = ele.size["height"] + 1000
        driver.set_window_size(1366, total_height)  # the trick
        time.sleep(1)
        driver.save_screenshot(screenshotPath + "MEARSK_SA_FP_" + formatted_date + ".png")
        for i in range(0,len(trows)):
            tdata=trows[i].find_elements_by_tag_name("td")
            j = trows[1].get_attribute("innerText")
            dataList.append(j)


            print(dataList)
        with open(r'C:\Users\User\PycharmProjects\shippingLine\csv/MERSK_SA_FP_' + formatted_date + '.csv', 'w',
                  newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow(dataList)

    except Exception as e:

        exc_type, exc_obj, exc_tb = exc_info()
        fname = path.split(exc_tb.tb_frame.f_code.co_filename)[0]
        infoList = [fname, exc_tb.tb_lineno, exc_obj]
        print("Exception (web_load) : " + str(e))
        errorLogger(errorLogPath, e, infoList)
        # alert("Exception (web_load) : "+str(e))
        screenshot(errorLog_screenshot + "automation.png")
        return False
web_load()