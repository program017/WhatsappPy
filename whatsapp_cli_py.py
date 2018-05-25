from selenium import webdriver as wbd
import time as t

def send(driver):
    name=raw_input('Enter the contact name or group name\n')
    message=raw_input('Enter message\n')
    try:
        user=driver.find_element_by_xpath('//span[@title="{}"]'.format(str(name)))
        user.click()
        #print 'user selected'
        msg_box= driver.find_element_by_class_name('_3F6QL')
        msg_box.click()
        #print 'message box clicked'
        msg_box.send_keys(message)
        #print 'written in message box'
        button=driver.find_element_by_class_name('_2lkdt')
        button.click()
    except:
        print 'something is wrong. Trying again'

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
    user=driver.find_element_by_xpath('//span[@title="{}"]'.format(str(name)))
    user.click()
    fi=str(name)+'.txt'
    f=open(fi,'a')
    loc='O90ur'
    while True:
        act=driver.find_element_by_xpath('.//span[@class="{}"]'.format(str(loc)))
        if act.text=='click here for contact info':
            pass
        elif act.text.split(' ')[0]=='last':
            temp=act.text.split(' ')
            f.write(str(temp[2])+str(temp[4])+str(temp[5]))
            t.sleep(30)
        if act.text=='online':
            print '{} is online'.format(name)
            f.close()
            return

def activity(driver):
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
