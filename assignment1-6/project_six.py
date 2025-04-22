# COUNTDOWN TIMER

import time

def countdown_timer(seconds):
    print(f"Countdown starts for {seconds} seconds!")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02}:{secs:02}"
        print(timer_display, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

# Set countdown time in seconds
time_in_seconds = int(input("Enter time in seconds: "))
countdown_timer(time_in_seconds)
