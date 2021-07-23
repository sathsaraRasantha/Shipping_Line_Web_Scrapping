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
    import datetime
    import time
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
errorLogPath = "C:\\Users\\User\\PycharmProjects\\shippingLine\\logs\\MCS log\\errorlog.txt"
errorLog_screenshot = "C:\\Users\\User\PycharmProjects\\shippingLine\\screenshots\\error\\"
screenshotPath = "C:\\Users\\User\\PycharmProjects\\shippingLine\\screenshots\\mcs\\"
#path = "C:\selenium browser drivers\chromedriver.exe"
url = "https://www.msc.com/track-a-shipment?agencyPath=mwi"
driver = webdriver.Chrome(r"C:\Users\Vevro\Downloads\chromedriver.exe")


def web_load():
    now = datetime.now()
    formatted_date = now.strftime('%Y_%m_%d_%H_%M_%S')
    try:
        driver.get(url)
        # managing cookies
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[4]/div[2]/div/button'))).click()

        driver.implicitly_wait(60)
        time.sleep(3)
        driver.save_screenshot(screenshotPath + "MSC_SA_FP_" + formatted_date + ".png")
    except Exception as e:
        exc_type, exc_obj, exc_tb = exc_info()
        fname = path.split(exc_tb.tb_frame.f_code.co_filename)[0]
        infoList = [fname, exc_tb.tb_lineno, exc_obj]
        print("Exception (web_load) : " + str(e))
        errorLogger(errorLogPath, e, infoList)
        # alert("Exception (web_load) : "+str(e))
        screenshot(errorLog_screenshot + "web_load.png")
    else:
        autoBooking()


# ////////////////////////Automating the booking ID//////////////////////////////////////////////////////////////
def autoBooking():
    try:
        now = datetime.now()
        formatted_date = now.strftime('%Y_%m_%d_%H_%M_%S')
        try:
            bookingid = "MEDUC6885825"
            searchBox = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located(
                    (By.ID, "ctl00_ctl00_plcMain_plcMain_TrackSearch_txtBolSearch_TextField")))
            searchBox = driver.find_element_by_id("ctl00_ctl00_plcMain_plcMain_TrackSearch_txtBolSearch_TextField")
            searchBox.send_keys(bookingid)
            searchBtn = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.ID, "ctl00_ctl00_plcMain_plcMain_TrackSearch_hlkSearch")))
            searchBtn = driver.find_element_by_id("ctl00_ctl00_plcMain_plcMain_TrackSearch_hlkSearch")
            searchBtn.send_keys(Keys.ENTER)
            driver.save_screenshot(screenshotPath + "MSC_SA_FP_AUTO" + formatted_date + ".png")
        except:
            searchBox = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located(
                    (By.ID, "ctl00_ctl00_plcMain_plcMain_TrackSearch_txtBolSearch_TextField")))
            searchBox = driver.find_element_by_id("ctl00_ctl00_plcMain_plcMain_TrackSearch_txtBolSearch_TextField")
            searchBtn = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.ID, "ctl00_ctl00_plcMain_plcMain_TrackSearch_hlkSearch")))
            searchBtn = driver.find_element_by_id("ctl00_ctl00_plcMain_plcMain_TrackSearch_hlkSearch")
            driver.save_screenshot(screenshotPath + "MSC_SA_FP_AUTO" + formatted_date + ".png")

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


# /////////////////////////////////////////Data Extraction module/////////////////////////////////////////

def data_extractor():
    try:
        now = datetime.now()
        formatted_date = now.strftime('%Y_%m_%d_%H_%M_%S')
        dataList = []
        try:
            dataTable = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.CLASS_NAME, "resultTable")))
            dataTable = driver.find_elements_by_class_name('resultTable')
            trows = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.TAG_NAME, "tr")))
            trows = dataTable[2].find_elements_by_tag_name('tr')
        except:
            dataTable = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CLASS_NAME, "resultTable")))
            dataTable = driver.find_elements_by_class_name('resultTable')
            trows = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.TAG_NAME, "tr")))
            trows = dataTable[2].find_elements_by_tag_name('tr')

            for i in range(0, len(trows)):
                tdata = trows[i].find_elements_by_tag_name('td')
                headers = trows[0].get_attribute('innerText')
                b = []
                for k in range(0, len(tdata)):
                    d = tdata[k].get_attribute('innerText')
                    b.append(d)
                    dataList.append(b)
        with open(r'C:\Users\User\PycharmProjects\shippingLine\csv/MSC_SA_FP_' + formatted_date + '.csv', 'w',
          newline='\n') as file:
            writer = csv.writer(file)
            writer.writerows(dataList)
            return dataList
            writer.close()
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