# question 2
def Question_2(input_list):
    for i in range(len(input_list)-1):
        if input_list[i]>=input_list[i+1]:  #here it simply checks whether adjucent ele is greater or not
            return [i,i+1]
    return []

# input_list = [1,2,3,0,4,5,6]
input_list = [1,2,3,4,5,6]
ans = Question_2(input_list)
print(ans)

# question1

def Question_1(input_list):
    ans_list =[]
    events_list = None #list of events
    for i in input_list:
        # if events is not there or current event is not same for example 'S' and 'A' then  append
        if events_list is None or events_list['SA'] != i['SA']:
            if events_list is not None:
                ans_list.append(events_list)
            events_list = {'SA': i['SA'],
                    'start_time':i['start_time'],
                    'end_time':i['end_time']}
        else:
            events_list['end_time']= i['end_time']
    if events_list is not None:
        ans_list.append(events_list)
    return ans_list

input_list =[{'SA': 'S', 'start_time': 1.0, 'end_time': 2.0},
 {'SA': 'S', 'start_time': 2.0, 'end_time': 3.0},
 {'SA': 'S', 'start_time': 3.2, 'end_time': 4.2},
 {'SA': 'S', 'start_time': 4.6, 'end_time': 5.6},
 {'SA': 'A', 'start_time': 5.9, 'end_time': 6.9},
 {'SA': 'A', 'start_time': 7.25, 'end_time': 8.25},
 {'SA': 'A', 'start_time': 8.34, 'end_time': 9.34},
 {'SA': 'A', 'start_time': 10.34, 'end_time': 12.34},
 {'SA': 'S', 'start_time': 12.35, 'end_time': 13.67},
]

ans_que1= Question_1(input_list)
print(ans_que1)
