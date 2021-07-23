errorLog_screenshot ="C:\\Users\\User\\PycharmProjects\\mcs\\screenshots\\error\\"
def errorLogger(errorLogPath, error, infoList):
    try:
        # import sys, os
        from datetime import datetime
        clock = datetime.now()

        f = open(errorLogPath, 'a')
        f.write(">>>Time : " + str(clock) + "\n")
        f.write(">>>Passed Error : " + str(error) + "\n")
        f.write(">>>File : " + str(infoList[0]) + "\n")
        f.write(">>>Line Number : " + str(infoList[1]) + "\n")
        f.write(">>>Reason : " + str(infoList[2]) + "\n")
        f.write(("#" * 75) + "\n")
        f.close()
    except Exception as e:
        print("Exception (errorLogger) : " + str(e))