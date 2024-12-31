from utils.qureyhive import query_hive

def getjobData():
    sql = '''
    select * from jobData
    '''
    data = query_hive(sql, [], 'select')
    return data

def getaverageCity():
    sql = '''
    select * from averageCity
    '''
    data = query_hive(sql, [],'select')
    return data

def getsalaryCategory():
    sql = '''
    select * from salaryCategory
    '''
    data = query_hive(sql, [],'select')
    return data

def getworkExperience():
    sql = '''
    select * from workExperience
    '''
    data = query_hive(sql, [],'select')
    return data

def getaddresssum():
    sql = '''
    select * from addresssum
    '''
    data = query_hive(sql, [],'select')
    return data

def getpeopleCategory():
    sql = '''
    select * from peopleCategory
    '''
    data = query_hive(sql, [],'select')
    return data

def getsalaryTop():
    sql = '''
    select * from salaryTop
    '''
    data = query_hive(sql, [],'select')
    return data

def gettypeSalary():
    sql = '''
    select * from typeSalary
    '''
    data = query_hive(sql, [],'select')
    return data

def getaverageType():
    averageType = query_hive('select * from averageType', [], 'select')
    return averageType

def getaverageExperience():
    sql = '''
    select * from averageExperience
    '''
    data = query_hive(sql, [],'select')
    return data

def geteducationCount():
    sql = '''
    select * from educationCount
    '''
    data = query_hive(sql, [],'select')
    return data

def gettypeCount():
    sql = '''
    select * from typeCount
    '''
    data = query_hive(sql, [],'select')
    return data

def gettypeMax():
    sql = '''
    select * from typeMax
    '''
    data = query_hive(sql, [],'select')
    return data

def getcitySalary():
    sql = '''
    select * from citySalary
    '''
    data = query_hive(sql, [],'select')
    return data

def getcityPeople():
    sql = '''
    select * from cityPeople
    '''
    data = query_hive(sql, [],'select')
    return data
