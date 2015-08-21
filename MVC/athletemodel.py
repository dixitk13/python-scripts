__author__ = 'Dixit_Patel'


from athlelist import AthleteList
import pickle

PICKLE_FILENAME = "athletemodel.pickle"

def get_coach_data(filename):
    returnDict = {}
    try:
        with open(filename) as data_file:
            data = data_file.readline()
            data = data.strip().split(',')
            return AthleteList(data.pop(0),data.pop(0),data)
    except IOError as ioerr:
        print('IOError ',ioerr)
        return None

def get_from_store():
    all_athletes = {}
    try:
        with open(PICKLE_FILENAME,'+rb') as pickle_store:
            all_athletes = pickle.load(pickle_store)

    except IOError as err:
        print('Filename:' + str(err))
    except pickle.PickleError as peer:
        print('Picking error' + str(peer))

    return all_athletes

def put_to_store(files_list):
    all_athletes = {}
    ath = AthleteList()
    for item in files_list:
        print('item->', item)
        ath = get_coach_data(item)
        all_athletes[ath.name] = ath

    try:
        with open(PICKLE_FILENAME,'+wb') as pickle_store:
            pickle.dump(all_athletes,pickle_store)
    except IOError as err:
        print('Filename:' + str(err))
    except pickle.PickleError as peer:
        print('Picking error' + str(peer))

    #return all_athletes


# temp_lst = ['julie2.txt','mikey2.txt','james2.txt','sarah2.txt']
#
# put_to_store(temp_lst)
#
# all_athletes = get_from_store()
# for each_athlete in all_athletes:
#     print(all_athletes[each_athlete].name + ' ' + all_athletes[each_athlete].dob)
#
# print(all_athletes)
