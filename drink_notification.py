import time
from plyer import notification

def notifyme():
    try:
        title="DRINK WATER NOTIFICATION."
        message=" it's important to drink plenty of fluids when the temperatures soar outside. But staying hydrated is a daily necessity, no matter what the thermometer says."
        app_name="H2O nice"
        app_icon="waterico.ico"
        timeout=20
        ticker="Hello Panni Pe loo"
        toast=False
        notification.notify(title,message,app_name,app_icon,timeout,ticker,toast)

    except Exception as e:
        print(e)

if __name__=="__main__":
    try:
        # while True:
            # time.sleep(9000)        ## it will remind me every 2 and half hour 9000 seconds
        notifyme()
    except Exception as e:
        print(e)


