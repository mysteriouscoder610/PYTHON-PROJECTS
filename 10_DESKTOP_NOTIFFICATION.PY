from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message="Rest is vital for mental health",
          #   app_icon="E:/app.ico",  # Ensure this path points to a valid .ico file
            timeout=5
        )
        time.sleep(20)

# to run it in the system without opening program multiple time 
# we can write in our cmd prmpt as 
# --> pythonw filename
