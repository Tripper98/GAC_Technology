
import datetime as dt 


DAYS = {'1': 'Lundi', '2':'Mardi', '3': 'Mercredi', '4': 'Jeudi', '5': 'Vendredi'}


def get_date(date_str):
    ''' 

    Input : '2 08:39-09:48'
    Output:  (2, 08:39, 09:48)
    
    '''
    aux_split = date_str.split()
    day = aux_split[0]
    slot = aux_split[1]
    aux_indispo = aux_split[1].split('-')
    slotStart = aux_indispo[0]
    slotEnd = aux_indispo[1]
    return day, slotStart, slotEnd


def get_days(N, len_N):
    '''

    Input: ['6', '2 08:39-09:48', '2 08:12-11:08', '1 13:09-16:27', '4 15:18-15:23', '3 14:05-17:51', '2 13:19-17:18'], 6
    Output: ['1', '2', '3', '4']

    '''
    N_days = []
    for i in range(1, len_N):
        day = N[i].split()[0]
        if day not in N_days:
            N_days.append(day)
    return sorted(N_days)


def get_slot_day(N, len_N, day):
    '''

    Input: N, la taille de N, day >> (N, 6, '1')
    Output: ['08:00', '13:09', '16:27', '17:59'] 

    '''
    slot_day = []
    # slot_day.append('08:00')
    for i in range(1, len_N+1):
        day_aux , slotStart, slotEnd = get_date(N[i])
        # print(get_date(N[i]))
        if day_aux == day :
            slot_day.append([slotStart, slotEnd])
    # slot_day.append('17:59')
    slot_day = sorted(slot_day)

    # print(slot_day)
    flat_list = [item for sublist in slot_day for item in sublist]

    for i in range(1, len(flat_list)-1, 2):
        if(flat_list[i]>flat_list[i+2]):
            flat_list[i], flat_list[i+2] = flat_list[i+2], flat_list[i]
    flat_list.insert(0, '08:00')
    flat_list.append('17:59')
    return flat_list


def calculate_difference_time(startTime, endTime):
    '''

    Input: 08:00, 08:13
    Output:  14 minutes de différance

    '''
    result =  (dt.datetime.strptime(endTime, "%H:%M") - dt.datetime.strptime(startTime, "%H:%M")).total_seconds()/60+1
    # print(result)
    return result


def check_duration(slot_day):
    '''
    
    Input: les créneaux impossibles >> ['08:00', '13:09', '16:27', '17:59']
    Output: Horaire de réunion (08:00,08:59)

    '''
    # slot_day = get_slot_day(N, day)
    len_slot = len(slot_day)
    # print(slot_day)
    for i in range(0, len_slot, 2) :
        diff = calculate_difference_time(slot_day[i], slot_day[i+1])
        # print(slot_day[i], diff)
        if diff >= 60:
            return slot_founded(slot_day[i])
            # print("Starting", slot_day[i])
            # break
    # return False

def slot_founded(startTime):
    endTime = dt.datetime.strptime(startTime, "%H:%M") + dt.timedelta(minutes= 59)
    endTime = format(endTime, '%H:%M')
    # print(endTime)
    return startTime, endTime


def main():
    N = ['6', '2 08:39-09:48', '2 08:12-11:08', '1 13:09-16:27', '4 15:18-15:23', '3 14:05-17:51', '2 13:19-17:18']
    len_N = int(N[0])
    N_days = get_days(N, len_N)


    # print(calculate_difference_time('08:00', '08:13'))
    # print(N)
    for day in N_days:
        # print(day)
        # print(get_slot_day(N, len_N, day))
        # print(f'Daaaaaaaaaaaaaaaay >> {day}')
        slot_duration = get_slot_day(N, len_N, day)
        founded_slot = check_duration(slot_duration)
        if(founded_slot):
            print(f'{day} {founded_slot[0]}-{founded_slot[1]}')
            # print(f'Your slot is: {DAYS[day]} : {founded_slot[0]} >> {founded_slot[1]}')
            return 0
    print('Slot not founded /!\\')
    # slot_founded('09:20')

    

if __name__ == '__main__':
    main()