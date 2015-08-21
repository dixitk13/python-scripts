__author__ = 'Dixit_Patel'

def sanitize(time_string):
    if '-' in time_string:
        (mins, secs) = time_string.split('-')
    elif ':' in time_string:
        (mins, secs) = time_string.split(':')
    else:
        return time_string
    return (mins + '.' + secs)


def get_coach_data(filename):
    try:
        with open(filename) as data_file:
            data = data_file.readline()
            return data.strip().split(',')
    except IOError as ioerr:
        print('IOError ',ioerr)
        return None


try:
    james = get_coach_data('james2.txt')
    julie = get_coach_data('julie2.txt')
    mikey = get_coach_data('mikey2.txt')
    sarah = get_coach_data('sarah2.txt')
    dixit_sarah = get_coach_data('sarah2.txt')


except IOError as err:
    print('IOError is ' + str(err))


print('james : ',james)
print('julie : ',julie)
print('mikey : ',mikey)
print('sarah : ',sarah)
print('dixit : ', dixit_sarah)

james_name, james_dob = james.pop(0), james.pop(0)
print(james_name + "'s fastest times are : " + str(sorted([sanitize(each_t) for each_t in james])[0:3]))
#james_sorted = sorted([sanitize(each_t) for each_t in james])

julie_name, julie_dob = julie.pop(0), julie.pop(0)
print(julie_name + "'s fastest times are : " + str(sorted([sanitize(each_t) for each_t in julie])[0:3]))
#julie_sorted = sorted([sanitize(each_t) for each_t in julie])#sanitize_lst(sorted(julie))

mikey_name, mikey_dob = mikey.pop(0), mikey.pop(0)
print(mikey_name + "'s fastest times are : " + str(sorted([sanitize(each_t) for each_t in mikey])[0:3]))
#mikey_sorted = sorted([sanitize(each_t) for each_t in mikey])#sanitize_lst(sorted(mikey))

sarah_name, sarah_dob = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are : " + str(sorted([sanitize(each_t) for each_t in sarah])[0:3]))
#sarah_sorted = sorted(set([sanitize(each_t) for each_t in sarah]))#sanitize_lst(sorted(sarah)))

#dixit_sarah_sorted = sorted([sanitize(each_t) for each_t in dixit_sarah])


# print("-- sorted -- ")
#
# print('james : ',james)
# print('julie : ',julie)
# print('mikey : ',mikey)
# print('sarah : ',sarah)
# print('dixit : ',dixit_sarah)
#
# print('james_sorted : ',james_sorted)
# print('julie_sorted : ',julie_sorted)
# print('mikey_sorted : ',mikey_sorted)
# print('sarah_sorted : ',sarah_sorted)
#
# print('dixit_sorted : ',dixit_sarah_sorted)
#
# print('james_sorted3 : ',james_sorted[0:3])
# print('julie_sorted3 : ',julie_sorted[0:3])
# print('mikey_sorted3 : ',mikey_sorted[0:3])
# print('sarah_sorted3 : ',sarah_sorted[0:3])
#
#
# print(sanitize('1-1'))
# print(sanitize('1:1'))
#
#
# print('test sorting', sorted(['1.1','1-1','1.2','2-2','apple','abba']))

# ref = [1,2,3]
# ref_r = ref
# print(ref)
# print(ref_r)
# ref_r.append('5')
# print(ref)
# print(ref_r)
