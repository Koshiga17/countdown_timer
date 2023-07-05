import datetime
import time

def get_target_datetime():
    target_date_str = input("Enter the target date (YYYY-MM-DD): ")
    target_time_str = input("Enter the target time (HH:MM:SS): ")
    target_datetime_str = target_date_str + " " + target_time_str
    target_datetime = datetime.datetime.strptime(target_datetime_str, "%Y-%m-%d %H:%M:%S")
    return target_datetime

def calculate_time_difference(target_datetime):
    current_datetime = datetime.datetime.now()
    time_difference = target_datetime - current_datetime
    return time_difference

def display_countdown(time_difference):
    while time_difference.total_seconds() > 0:
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        countdown = f"{days} day(s), {hours:02d}:{minutes:02d}:{seconds:02d}"
        print(countdown, end="\r")
        time.sleep(1)

        current_datetime = datetime.datetime.now()
        time_difference = target_datetime - current_datetime

    print("Countdown finished!")

target_datetime = get_target_datetime()
time_difference = calculate_time_difference(target_datetime)
display_countdown(time_difference)
