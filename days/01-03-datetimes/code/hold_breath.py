from datetime import datetime 
from datetime import timedelta
import time

def main():
    show_header()
    event_loop()
    
def event_loop():
    answer= input('Would you like to start timer now?<Yes or No>').lower()
    count= 1
 
    
    while True:
        
        if answer == 'yes':
            seconds= int(input('how many seconds can you hold your breath?'))
            print('session number: ', str(count))
            print(str(seconds), ' seconds started.')
            
            duration= timedelta(seconds= seconds)
            start= datetime.now()
            end= start+ duration
            print('session will end at :', end)
                
            for each in list(range(seconds)):
                time.sleep(1)
                print(each+1, 'seconds.')
            print('The end')
            break
          
        elif answer== 'no':
            print('ok bye')
            break
        else:
            print('Sorry, I Only understand yes or no')
            break
        
    decide= input('CONGRATS.... Would you like to have another session? <yes or no>').lower()
    if decide =='yes':
        main()
    elif decide == 'no':
        print('thank you for using my app. See you next time.')
    else:
        print('Could not understand command. Only understand yes or no.')    
    

def show_header():
    print('------------------------------------------------')
    print('           Hold your breath')
    print('Push yourself to the limit. Just do not pass out.')
    print('------------------------------------------------')

if __name__ == '__main__':
    main()