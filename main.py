#Pomodoro Timer

import time
import sys

interval = int(input('Please Enter duration (mins) of interval: '))
break_duration = int(input('Please Enter break duration(mins) of interval: '))
total_duration = int(input('Please enter number of sessions: '))

interval = 5
for i in range(interval,-1,-1):
    for j in range(59,-1,-1): 
        
        time.sleep(1)

def user_input():
    interval = int(input('Please Enter duration (mins) of interval: '))
    break_duration = int(input('Please Enter break duration(mins) of interval: '))
    total_duration = int(input('Please enter number of sessions: '))
    return interval, duration, break_session

def countdown(interval):
    for i in range(interval,-1,-1):
        for j in range(59,-1,-1):
            sys.stdout.write(f'\rDuration: \
            Minutes {j} Seconds {i} to go')
            time.sleep(1)
            sys.stdout.flush()

if __name__ == "__main__":
    session_count = 0
    interval, total_duration, break_duration = user_input()
    while session_count < total_duration:
        countdown(interval)
        print('\nBreak!')
        countdown(break_duration)
        session_count += 1
        print('\nsession: ',session_count)
    print('\nEnd of Session!')
