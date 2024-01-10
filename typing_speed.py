## check your typing speed 

import datetime

para="this is a simple paragraph that is meant to be nice and easy to type which is why there will be mommas no periods or any capital letters so i guess this means that it cannot really be considered a paragraph but just a series of run on sentences this should help you get faster at typing as im trying not to use too many difficult words in it although i think that i might start making it hard by including some more difficult letters I'm typing pretty quickly so forgive me for any mistakes."
def checkspeed():
    min=datetime.datetime.now().minute
    print(min)
    user=input('Start Typing \n')
    min1=datetime.datetime.now().minute
    if min1==min:
        minutes=1
    else:
        minutes=min1-min
    return user,minutes

def accuracy(user):
    error=0

    for i in user.split(" "):
        if i in para:
            pass
        else:
            error+=1
    return error



if __name__=="__main__":
    user,minutes=checkspeed()
    er=accuracy(user)
    length=len(user.split(" "))
    print(f"TYPING SPEED >>> {length/minutes}" )
    print(f"ERROR --> {er}")
    print(f"ACCURACY --> {((length-er)/length)*100}")
