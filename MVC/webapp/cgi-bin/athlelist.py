__author__ = 'Dixit_Patel'

NAME = "NAME"
DOB = "DOB"
LSTTIME = "LSTTIME"

class AthleteList(list):

    def __init__(self, a_name = "", a_dob = "", a_times = []):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
        self.extend(a_times)

    @property
    def returnTop3(self):
        return (sorted(sanitize(each_t) for each_t in self))[0:3]


def sanitize(time_string):
    if '-' in time_string:
        (mins, secs) = time_string.split('-')
    elif ':' in time_string:
        (mins, secs) = time_string.split(':')
    else:
        return time_string
    return (mins + '.' + secs)


def get_coach_data(filename):
    returnDict = {}
    try:
        with open(filename) as data_file:
            data = data_file.readline()
            # datalst = []
            # datalst = data
            # print(datalst)
            data = data.strip().split(',')
            returnDict[NAME] = data.pop(0)
            returnDict[DOB] = data.pop(0)
            returnDict[LSTTIME] = sorted(sanitize(each_t) for each_t in data)#data
            #return data.strip().split(',')
            return returnDict
    except IOError as ioerr:
        print('IOError ',ioerr)
        return None

def get_coach_data_make_dict(filename):
    returnDict = {}
    try:
        with open(filename) as data_file:
            data = data_file.readline()
            data = data.strip().split(',')
            # returnDict[NAME] = data.pop(0)
            # returnDict[DOB] = data.pop(0)
            # returnDict[LSTTIME] = sorted(sanitize(each_t) for each_t in data)
            #return ({'NAME':data.pop(0),'DOB':data.pop(0),"LSTTIME":sorted(sanitize(each_t) for each_t in data)})
            return AthleteList(data.pop(0),data.pop(0),data)
            #return data.strip().split(',')
            #return returnDict
    except IOError as ioerr:
        print('IOError ',ioerr)
        return None

# try:
#     james = get_coach_data('james2.txt')
#     julie = get_coach_data('julie2.txt')
#     mikey = get_coach_data('mikey2.txt')
#     sarah = get_coach_data('sarah2.txt')
#     dixit_sarah = get_coach_data_make_dict('sarah2.txt')
#     #dixit_sarah.addTimes(['2.1','1.12'])
#     # dixit_sarah.addTime('1.12')
#     # dixit_sarah.addTimes(['1-1','1-12'])
#     #dixit_sarah.extend('1.12')
#     dixit_sarah.extend(['1-1','1-12'])
#
# except IOError as err:
#     print('IOError is ' + str(err))
#
#
# print('james : ',james)
# print('julie : ',julie)
# print('mikey : ',mikey)
# print('sarah : ',sarah)
# print('dixit : ', dixit_sarah)
#
# print(type(dixit_sarah))

# james_dict = {}
# julie_dict = {}
# mikey_dict = {}
# sarah_dict = {}




# james_name, james_dob = james.pop(0), james.pop(0)
#print(james[NAME] + "'s fastest times are : " + str((james[LSTTIME])[0:3]))


# print(dixit_sarah.name)
# print(dixit_sarah)


# #james_sorted = sorted([sanitize(each_t) for each_t in james])
#
# julie_name, julie_dob = julie.pop(0), julie.pop(0)
# print(julie_name + "'s fastest times are : " + str(sorted([sanitize(each_t) for each_t in julie])[0:3]))
# #julie_sorted = sorted([sanitize(each_t) for each_t in julie])#sanitize_lst(sorted(julie))
#
# mikey_name, mikey_dob = mikey.pop(0), mikey.pop(0)
# print(mikey_name + "'s fastest times are : " + str(sorted([sanitize(each_t) for each_t in mikey])[0:3]))
# #mikey_sorted = sorted([sanitize(each_t) for each_t in mikey])#sanitize_lst(sorted(mikey))
#
# sarah_name, sarah_dob = sarah.pop(0), sarah.pop(0)
# print(sarah_name + "'s fastest times are : " + str(sorted([sanitize(each_t) for each_t in sarah])[0:3]))
