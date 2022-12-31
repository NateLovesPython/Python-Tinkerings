import time
import threading

class AlarmClock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
    
    def run(self):
        # Get the current time
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min

        # Calculate the time until the alarm should go off
        time_until_alarm = (self.hour - current_hour) * 3600 + (self.minute - current_minute) * 60
        
        # Sleep for the appropriate amount of time
        time.sleep(time_until_alarm)
        
        # Play an alarm sound
        print("Wake up!")

# Set the alarm for 7:30 AM
alarm = AlarmClock(hour=7, minute=30)

# Run the alarm in a separate thread
thread = threading.Thread(target=alarm.run)
thread.start()

print("Alarm set for 7:30 AM")
