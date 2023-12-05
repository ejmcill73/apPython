tv_channels = ["ESPN", "ABC","National Geographic", "Discovery"]

currentChannel=int(input('What channel do you want to go to? '))

if currentChannel==0 :
    print("You are watching ESPN")
if currentChannel==1:
    print("You are watching ABC")
if currentChannel==2:
    print("You are watching National Geographic")
if currentChannel==3 :
    print("You are watching Discovery")
    

stream_services = ["Hulu", "Netflix", "Paramount Plus", "Disney Plus"]

currentservice=int(input("What service do you wnat to go to?"))

if currentservice==0 :
    print("You are watching Hulu")

if currentservice==1:
    print("You are watching Netflix")      
if currentservice==2 :
    print("You are watching Paramount Plus")

if currentservice==3:
   print("You are watching Disney Plus")
    


def change_volume():
    current_volume = 0
    max_volume = 10

    while current_volume < max_volume:
        userAnswer=input('do you want to increase the volume? ')
        if userAnswer =='y':
            current_volume+=1   
            print('volume is now : ' + str(current_volume))
        else:
         break




    change_volume()
