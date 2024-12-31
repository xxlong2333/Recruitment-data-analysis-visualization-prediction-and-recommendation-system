from utils.getPublicData import *
from myApp.models import *

def getIndexData():
    averageCity = list(getaverageCity())
    averageCityX = [x[0] for x in averageCity]
    averageCityY = [round(x[1], 1) for x in averageCity]
    print(averageCityX, averageCityY)

    salarycategoryList = list(getsalaryCategory())
    salarycategoryData = []
    for i in salarycategoryList:
        salarycategoryData.append({
            'name':i[0],
            'value':i[1]
        })

    #工作经验
    expSalaryList = list(getworkExperience())
    expSalaryX = [x[0] for x in averageCity]
    expSalaryY = [round(x[1], 1) for x in expSalaryList]
    expSalaryY1 = [round(x[1], 1) for x in expSalaryList]
    expSalaryY2 = [round(x[2], 1) for x in expSalaryList]

    peopleCategoryList = list(getpeopleCategory())
    peopleCategoryData = []
    for i in peopleCategoryList:
        peopleCategoryData.append({
            'name':i[0],
            'value':i[1]
        })
    print(salarycategoryData, expSalaryX, expSalaryY, expSalaryY1, expSalaryY2, peopleCategoryData)

    adddresssumList = list(getaddresssum())
    adddresssumData = []
    for i in adddresssumList:
        adddresssumData.append({
            'name':i[0],
            'value':i[1]
        })

    print(adddresssumData)
    return averageCityX, averageCityY, salarycategoryData, expSalaryX, expSalaryY, expSalaryY1, expSalaryY2, peopleCategoryData,adddresssumData


def addHistoryData(userInfo, jobId):
    hisData = History.objects.filter(user=userInfo, jobId = jobId)
    if len(hisData):
        hisData[0].count += 1
        hisData[0].save()
    else:
        History.objects.create(
            user=userInfo,
            jobId = jobId
        )

def getUserHistory(userInfo):
    dataList = list(History.objects.filter(user=userInfo).order_by('-count'))
    jobIdList = []
    for i in dataList:
        jobIdList.append(i.jobId)
    print(jobIdList)

    jobList = []
    for i in jobIdList:
        x = list(query_hive('select * from jobData where id=%d', [int(i)], 'select')[0])
        print(x)
        jobList.append(x)
    print(jobList)
    return jobList

def changePwd(userInfo, passwordInfo):
    oldPwd = passwordInfo['oldPassword']
    newPwd = passwordInfo['newPassword']
    chkPwd = passwordInfo['ckPassword']

    user = User.objects.get(username=userInfo.username)

    if oldPwd != user.password:
        return '原密码错误'
    if newPwd != chkPwd:
        return '两次密码不一致'
    user.password = newPwd
    user.save()


