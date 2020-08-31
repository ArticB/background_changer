from server import get_data, save_image, change_background_image

import schedule
import time

def job():    
    print("Doing Job....")
    get_data()
    save_image()
    change_background_image()


schedule.every(10).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
