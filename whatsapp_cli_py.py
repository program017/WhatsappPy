from selenium import webdriver as wbd
import time as t
from datetime import datetime as dtn

def send(driver):
    name=raw_input('Enter the contact name or group name\n')
    message=raw_input('Enter message\n')
    try:
        #search=driver.find_element_by_class_name('_2MSJr') # testing for search box
        #msg_box.send_keys(name)
        #search.click()
        #print 'search complete'
        user=driver.find_element_by_xpath('//span[@title="{}"]'.format(str(name)))
        user.click()
    except:
        print 'Selected name is not present. Try Again'
        return
    try:
        #print 'user selected'
        msg_box= driver.find_element_by_class_name('_3F6QL')
        msg_box.click()
        #print 'message box clicked'
        msg_box.send_keys(message)
        #print 'written in message box'
        button=driver.find_element_by_class_name('_2lkdt')
        button.click()
    except:
        print 'Message could not be written. Try Again'

def check(driver):
    #this facility is working for only last message. will extend it later
    name=raw_input('Enter the contact name or group name\n')
    user=driver.find_element_by_xpath('//span[@title="{}"]'.format(str(name)))
    user.click()
    unread=driver.find_element_by_class_name('L89LI')
    print unread
    return

def log(driver):
    name=raw_input('Enter the contact name or group name\n')
    try:
        user=driver.find_element_by_xpath('//span[@title="{}"]'.format(str(name)))
        user.click()
    except:
        print 'Selected name is not present. Try Again.'
        return
    tm=input('for how long you want to run the log. Enter in minutes\n')
    tm=tm*60
    print 'Running log'
    fi=str(name)+'.txt'
    f=open(fi,'a')
    while True:
        try:
            act=driver.find_element_by_xpath('.//span[@class="{}"]'.format('O90ur'))
            if act.text=='click here for contact info':
                pass
            elif act.text.split(' ')[0]=='last':
                temp=act.text.split(' ')
                text=str(temp[2])+' '+str(temp[4])+' '+str(temp[5])+'\n'
                f2=open(fi,'r')
                flag=0
                for lines in f2:
                    if str(lines.strip(' '))==str(text):
                        flag=1
                f2.close()
                if flag==0:
                    f.write(text)
                flag=0
            if act.text=='online':
                #print '{} is online'.format(name)
                time=dtn.now().strftime("%Y-%m-%d %H:%M")
                f2=open(fi,'r')
                flag1=0
                for lines in f2:
                    if str(lines.strip(' '))==str(time):
                        flag1=1
                if flag1==0:
                    f.write(text)
        except:
            print '****************************'
            print 'User have disabled last seen'
            print '****************************'
            print
        tm=tm-1
        t.sleep(1)
        print 'Time left: {} secs'.format(tm)
        if tm<=0:
            f.close()
            return

def activity(driver):
    print '-----------------------------------------------'
    print 'Warning this will only work for recent contacts'
    print '-----------------------------------------------'
    print
    inp=input('Enter your choice\n1.Send Message\n2.Check Messages\n3.Check online log activity\n4.Exit\n')
    if inp==1:
        send(driver)
    elif inp==2:
        check(driver)
    elif inp==3:
        log(driver)
    elif inp==4:
        exit()
    else:
        print 'wrong input'


def main():
    driver = wbd.Chrome('C:\Users\Program017\Downloads\chromedriver')
    driver.get('https://web.whatsapp.com')
    while True:
        activity(driver)

if __name__=='__main__':
    main()
