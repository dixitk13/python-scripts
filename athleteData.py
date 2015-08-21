__author__ = 'Dixit_Patel'

def sanitize(time_string):
    if '-' in time_string:
        (mins, secs) = time_string.split('-')
    elif ':' in time_string:
        (mins, secs) = time_string.split(':')
    else:
        return time_string
    return (mins + '.' + secs)

def sanitize_lst(time_lst):
    clean_lst = []
    for each_t in time_lst:
        clean_lst.append(sanitize(each_t))
    return clean_lst

def get_coach_data(filename):
    try:
        with open(filename) as data_file:
            data = data_file.readline()
            return data.strip().split(',')
    except IOError as ioerr:
        print('IOError ',ioerr)
        return None


try:
    # with open('james.txt') as james_data:
    #     line = james_data.readline();
    # james = line.strip().split(',')
    james = get_coach_data('james.txt')
    # with open('julie.txt') as julie_data:
    #     line = julie_data.readline();
    # julie = line.strip().split(',')
    julie = get_coach_data('julie.txt')
    # with open('mikey.txt') as mikey_data:
    #     line = mikey_data.readline();
    # mikey = line.strip().split(',')
    mikey = get_coach_data('mikey.txt')
    # with open('sarah.txt') as sarah_data:
    #     line = sarah_data.readline();
    # sarah = line.strip().split(',')
    sarah = get_coach_data('sarah.txt')
    dixit_sarah = get_coach_data('sarah.txt')


except IOError as err:
    print('IOError is ' + str(err))


print('james : ',james)
print('julie : ',julie)
print('mikey : ',mikey)
print('sarah : ',sarah)
print('dixit : ', dixit_sarah)


# james_sorted = sanitize_lst(sorted(james))
# julie_sorted = sanitize_lst(sorted(julie))
# mikey_sorted = sanitize_lst(sorted(mikey))
# sarah_sorted = sanitize_lst(sorted(sarah))
james_sorted = sorted([sanitize(each_t) for each_t in james])
julie_sorted = sorted([sanitize(each_t) for each_t in julie])#sanitize_lst(sorted(julie))
mikey_sorted = sorted([sanitize(each_t) for each_t in mikey])#sanitize_lst(sorted(mikey))
sarah_sorted = sorted(set([sanitize(each_t) for each_t in sarah]))#sanitize_lst(sorted(sarah)))
dixit_sarah_sorted = sorted([sanitize(each_t) for each_t in dixit_sarah])


print("-- sorted -- ")

print('james : ',james)
print('julie : ',julie)
print('mikey : ',mikey)
print('sarah : ',sarah)
print('dixit : ',dixit_sarah)

print('james_sorted : ',james_sorted)
print('julie_sorted : ',julie_sorted)
print('mikey_sorted : ',mikey_sorted)
print('sarah_sorted : ',sarah_sorted)

print('dixit_sorted : ',dixit_sarah_sorted)

print('james_sorted3 : ',james_sorted[0:3])
print('julie_sorted3 : ',julie_sorted[0:3])
print('mikey_sorted3 : ',mikey_sorted[0:3])
print('sarah_sorted3 : ',sarah_sorted[0:3])


print(sanitize('1-1'))
print(sanitize('1:1'))


print('test sorting', sorted(['1.1','1-1','1.2','2-2','apple','abba']))

# ref = [1,2,3]
# ref_r = ref
# print(ref)
# print(ref_r)
# ref_r.append('5')
# print(ref)
# print(ref_r)