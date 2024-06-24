import datetime
import time
import os

def diagnose():
    with open("./data/mood_diary.txt", "r") as file:
        lines = file.readlines()
    length = len(lines)
    if length < 7:
        return
    sum = 0
    mood_count = {-2:0, -1:0, 0:0, 1:0, 2:0}
    for i in range(7):
        value = int(lines[length - i - 1].strip().split(' ')[0])
        sum += value
        mood_count[value] += 1
    average = round(sum / length)
    score_to_mood = {2: "happy", 1: "relaxed", 0: "apathetic", -1: "sad", -2: "angry"}
    # happy
    if mood_count[2] >= 5:
        result = "manic"
    # sad
    elif mood_count[-1] >= 4:
        result = "depressive"
    # apathetic 
    elif mood_count[0] >= 6:
        result = "schizoid"
    else:
        result = score_to_mood[average]
    
    print("Your diagnosis: "+result+"!\n")

def assess_mood():
    moods = {"happy":2, "relaxed": 1, "apathetic": 0, "sad": -1, "angry": -2}
    date_today = datetime.date.today()
    date_today = str(date_today)

    sub_dir = 'data'  
    file_name = 'mood_diary.txt'
    sub_dir_path = os.path.join(os.getcwd(), sub_dir)  
    file_path = os.path.join(sub_dir_path, file_name)  
    if not os.path.exists(sub_dir_path):  
        os.makedirs(sub_dir_path) 

    with open(file_path, "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
        else:
            last_line = None
    
    # not first day
    if last_line is not None:
        latest_date = last_line.strip().split(' ')[1]
        if latest_date == date_today:
            print("Sorry, you have already entered your mood today.\n")
            return

    # wait 1 second
    time.sleep(1)

    while True:
        cur_mood = input("please enter your current mood\n")
        if cur_mood not in moods.keys():
            continue
        mood_value = moods[cur_mood]

        # update date
        date_today = datetime.date.today()
        date_today = str(date_today)
        
        with open(file_path, "a") as file:
            file.write(str(mood_value)+" " + date_today +"\n")
            file.close()
        break
    diagnose()
