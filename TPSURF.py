import os
import sys
import time
import names
import asyncio
import names
import re
import random
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from web3.auto import w3
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import threading
import pyautogui
from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN
from concurrent.futures import ThreadPoolExecutor, as_completed
import string
#url = "https://tpow.app/ee0913ba"
url = 'https://tpow.app/dbb5aa7e'
#url = 'https://tpow.app/a0162769'
#urle = 'https://tpow.app/fed486b9'
#url = 'https://tpow.app/2766bd9e' #url null
#url = 'https://tpow.app/ceef2523'
#url2 = 'https://bit.ly/3leAms6'
#uri = 'https://tpow.app/4936650e'

banners = (         '\nBOTS Register TonicPow AUTOSURF\n'
          '======================================================\n'
          ' Feature : > Random User-Agent'
          '\n           > Random Proxy (If You Have Proxy)'
          '\n           > FREE TO USE!'
          '\n           > USING PYAUTOGUI\n'
          '[!] DISCLAMER!: YOU TRY THIS BOT YOU KNOW DYOR!\n'
          '[!] Just Give Me Coffee ! :D\n'
          '               *MONNALISA-ID (OWNNER)\n'
          '=======================================================\n')


def kuli():
    try:
        if os.name == 'nt':os.system('cls')
        else:os.system('clear')
        print(banners)
        time.sleep(0.5)

        # User-Agent
        #ua = UserAgent()
        #user_agent = ua.random
        user_agent = random.choice(open('usrgt.txt').readlines())
        First_name = names.get_first_name()
        Last_name = names.get_last_name()
        
        #NORD ROTATION!
        nords = initialize_VPN(area_input=['united states', 'united kingdom', 'canada', 'new zealand', 'netherlands', 'australia'])
        #nords = initialize_VPN(area_input=['united kingdom','united states', 'switzerland','sweden','spain','south africa','singapore','poland','norway','new zealand','netherlands','mexico','luxembourg','latvia','ireland', 'iceland','hungary','denmark','czech republic','croatia','canada','austria'])
        #nords = initialize_VPN(area_input=['complete rotation']) #// For ALL COUNTRY
        time.sleep(0.8)
        #rotate_VPN(nords)
        rotate_VPN(nords,google_check=1)
        
        # Email
        extensions = ['com', 'net', 'org', 'xyz']
        domains = ['gmail', 'yahoo', 'icloud', 'hotmail', 'outlook', 'yandex']
        randomzer = names.get_last_name()
        numberz = random.randint(1, 20)
        winext = extensions[random.randint(0, len(extensions)-1)]
        windom = domains[random.randint(0, len(domains)-1)]
        emaz = ''.join(random.choice(randomzer) for _ in range(numberz))
        exx = emaz + "@" + windom + "." + winext
        emails = exx
        
        
        # Options ChromeDriver!
        option = uc.ChromeOptions()
        #option.add_argument("--start-maximized")
        #option.add_argument('--headless')
        option.add_argument("--mute-audio")
        option.add_argument('--incognito')
        option.add_argument("--disable-blink-features=AutomationControlled")
        option.add_argument("--disable-infobars")
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--disable-gpu')
        option.add_argument('--disable-notifications')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--no-sandbox')
        option.add_argument("user-agent=" + user_agent)
        #option.add_extension('./buster_ext.crx')
        option.add_argument('--ignore-certificate-errors')
        option.add_argument('--allow-running-insecure-content')
        driver = uc.Chrome(options=option)
        
        l = ['|', '/', '-', '\\']
        for i in l+l+l+l+l:
            sys.stdout.write('\r' + '[*] Loading... '+i)
            sys.stdout.flush()
            time.sleep(0.2)
        print('')
        
        if os.name == 'nt':os.system('cls')
        else:os.system('clear')
        time.sleep(0.7)
        #driver.minimize_window()
        #driver.maximize_window()
        driver.get(url)
        #driver.get(url2)
        print(banners)
        print(user_agent)
        time.sleep(0.5)
        print('AUTO SURF BEGIN....')
        time.sleep(5)
        #driver.switch_to.window(driver.window_handles[1])
        #driver.execute_script('window.scrollBy(0,755)',"")
        #time.sleep(5)
        #Register 
        #driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/a/h2').click()
        #driver.find_element_by_xpath('//*[@id="openRegistrationModal"]').click() #register(Button)
        #time.sleep(0.8)
        #print('First Name : ', First_name)
        #driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[1]/div/input').send_keys(First_name) # First Name
        #time.sleep(0.8)
        #print('Last Name : ',Last_name)
        #driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[2]/div/input').send_keys(Last_name) # Last Name
        #time.sleep(0.8)
        #print('Email : ', exx)
        #driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/form/p[1]/input').send_keys(exx) # Email
        #driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[3]/div/input').send_keys(exx) # Email
        #time.sleep(0.8)
        #driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[4]/div/input').send_keys("Burik12345@") # Password
        #time.sleep(0.8)
        #driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[5]/div/input').send_keys("Burik12345@") # Password Confirmation
        #time.sleep(0.8)
        
        #driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div/form/div/div').click()
        #driver.find_element_by_name("Value").send_keys(Keys.ENTER)
        #driver.find_element_by_xpath('//*[@id="registerButton"]').click() # Register Now ! (Button)
        #time.sleep(5)
        
        #LOGIN
        if os.name == 'nt':os.system('cls')
        else:os.system('clear')
        print(banners)
        print('Login...')
        #driver.find_element_by_xpath('//*[@id="email"]').send_keys(exx) #Email
        #time.sleep(0.8)
        #driver.find_element_by_xpath('//*[@id="password"]').send_keys("Burik12345@") #Password
        #time.sleep(0.8)
        #driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/button').click() #Login Now !(Button)
        #time.sleep(3)
        #print('Please Wait... Enroll....')
        #driver.find_element_by_xpath('/html/body/main/div/div/div/div/div[1]/div[9]/form/button').click() #Enroll(BUTTON)
        #time.sleep(5)
        #driver.execute_script('''window.open();''')
        time.sleep(0.3)
        #driver.get(uri)
        #time.sleep(5)
        
        #driver.switch_to.window(driver.window_handles[0])
        
        #print('AUTO SURF Part 2 BEGIN....')
        #time.sleep(5)
        #driver.switch_to.window(driver.window_handles[1])
        #driver.execute_script('window.scrollBy(0,755)',"")
        #time.sleep(5)
        #print('Please Wait... Enroll....')
        #driver.find_element_by_xpath('/html/body/main/div/div/div/div/div[1]/div[9]/form/button').click() #Enroll(BUTTON)
        #time.sleep(5)
        print('AUTO SURF DONE!')
        print('TASK COMPLETE!')
        time.sleep(3)
        terminate_VPN(nords)
        driver.quit()
    except Exception as e:
        print(e)
        print('Your User Agent Is To Old Please Change To Newest!')
        #sys.exit()
        terminate_VPN(nords)
        driver.close()
        pass

while True:
    time.sleep(3)
    kuli()


#i =0
#while i <= 100:
#    i += 1
#                                                                                                                                                
#thread_count = i
#for i in range(thread_count):
#    t = threading.Thread(target=kuli)
#    t.start()
#    t.join()
#Course
#        driver.find_elements_by_xpath('/html/body/main/div/div/div/div/div[2]/div[9]/a').click() #Continue COurse
#        time.sleep(0.8)
#        time.sleep(0.8)
#        driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div[2]/a').click() #Proceed To Next Lesson 1
#        time.sleep(0.8)
#        driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div/a').click() #Proceed To Next Lesson 2
#        time.sleep(0.8)
#        driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div/a').click() #TAKE THE ASSESSMENT (Proceed To Next Lesson 3)
#        time.sleep(0.8)
#        #The Bitcoin transaction history is:
#        driver.find_elements_by_xpath('//*[@id="answer-1"]').click() #Public
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[1]/a').click() #NEXT Button
#        time.sleep(0.8)
#        #Abstract Assessment No.1 (2/4)
#        #The Bitcoin protocol is limited only by the__________________rather than arbitrary parameters.:
#        driver.find_elements_by_xpath('//*[@id="answer-7"]').click #Economics of processing each transaction
#        time.sleep(0.8)
#        driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[2]/a[2]').click() #NEXT Button
#        time.sleep(0.8)
#        #Abstract Assessment No.1 (3/4)
#        #Which part of the transaction do the transaction processors create?
#        driver.find_elements_by_xpath('//*[@id="answer-12"]').click() #None of it
#        time.sleep(0.8)
#        driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[3]/a[2]').click()
#        time.sleep(0.8)
#        #Abstract Assessment No.1 (4/4)
#        #How much do transaction processors take for writing a transaction to the ledger?
#        driver.find_elements_by_xpath('//*[@id="answer-16"]').click() #A sufficient value acceptable to transaction processors
#        time.sleep(0.8)
#        driver.find_elements_by_xpath('//*[@id="test-pane-4"]/button').click() # Complete Assessment
#        time.sleep(0.8)
#        driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[10]/a').click() #Proceed To Next Lesson 4
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div/a').click() #Proceed To Next Lesson 5
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div/a').click() #Proceed To Next Lesson 6
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div/a').click() #TAKE THE ASSESSMENT (Proceed To Next Lesson 7)
#        time.sleep(0.8)
#        #Abstract Assessment No.2 (1/5)
#        #A double spend refers to:
#        driver.find_element_by_xpath('//*[@id="answer-19"]').click() #Sending a transaction and then sending a different transaction spending the same funds to a different address prior to confirmation of the original transaction.
#        time.sleep(0.8)
#        driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[1]/a').click() #NEXT BUTTON 1
#        time.sleep(0.8)
#        #Abstract Assessment No.2 (2/5)
#        #Changing blocks that have had several blocks built on top of them is rendered almost impossible through the ____________.
#        driver.find_element_by_xpath('//*[@id="answer-21"]').click() #Accumulation of proof-of-work
#        time.sleep(0.8)
#        driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[2]/a[2]').click() #NEXT BUTTON 2
#        time.sleep(0.8)
#        #Abstract Assessment No.2 (3/5)
#        #Blocks are a _________i) for all the transactions they contain and represent a __________ii)
#        driver.find_element_by_xpath('//*[@id="answer-26"]').click() #i) timestamp, ii) proof of their existence and validity.
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[3]/a[2]').click() #Next Button 3
#        time.sleep(0.8)
#        #Abstract Assessment No.2 (4/5)
#        #The block solution represents proof that the node proposing the block has _________ necessary for that block to be valid.
#        driver.find_element_by_xpath('//*[@id="answer-29"]').click() #Performed the work
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[4]/a[2]').click() #Next Button 4
#        time.sleep(0.8)
#        #Abstract Assessment No.2 (5/5)
#        #A node must be able to keep up with the rest of the network in the tasks of downloading, _________ i) all of the transactions taking place in the world in real time. The hashing machinery used to generate ________ ii) votes for the most capable node, incentivising node operators to build the fastest most capable machines in order to attract the most ________iii)
#        driver.find_element_by_xpath('//*[@id="answer-33"]').click() # i) validating and storing, ii) proof of work, iii) hash
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[5]/button').click() # Complete Assessment
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[12]/a').click() #Proceed To Next Lesson 9
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div/a').click() #Proceed To Next Lesson 10
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div/a').click() #Proceed To Next Lesson 11
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div/a').click() #Proceed To Next Lesson 12
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div[2]/a').click() #TAKE THE ASSESSMENT (Proceed To Next Lesson 13)
#        time.sleep(0.8)
#        #Abstract Assessment No.3 (1/7)
#        driver.find_element_by_xpath('//*[@id="answer-40"]').click() # i) hashpower, ii) energy investment
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[1]/a').click() # NEXT BUTTON 1
#        time.sleep(0.8)
#        #Abstract Assessment No.3 (2/7)
#        driver.find_element_by_xpath('//*[@id="answer-42"]').click() # i) double spends, ii) network hashpower
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[2]/a[2]').click() # Next Button 2
#        time.sleep(0.8)
#        #Abstract Assessment No.3 (3/7)
#        driver.find_element_by_xpath('//*[@id="answer-47"]').click() # Double spend
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[3]/a[2]').click() # Next Button 3
#        time.sleep(0.8)
#        #Abstract Assessment No.3 (4/7)
#        driver.find_element_by_xpath('//*[@id="answer-51"]').click() # i) fee revenue ii) infrastructure
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[4]/a[2]').click() # Next Button 4
#        time.sleep(0.8)
#        #Abstract Assessment No.3 (5/7)
#        driver.find_element_by_xpath('//*[@id="answer-56"]').click() # i) first seen, ii) double spending
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[5]/a[2]').click() # Next Button 5
#        time.sleep(0.8)
#        #Abstract Assessment No.3 (6/7)
#        driver.find_element_by_xpath('//*[@id="answer-59"]').click() # The longest chain that is compliant to the network rules is valid.
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[6]/a[2]').click() # Next Button 6
#        time.sleep(0.8)
#        #Abstract Assessment No.3 (7/7)
#        driver.find_element_by_xpath('//*[@id="answer-62"]').click() # Using block announcements, nodes accept the first valid block which builds upon the longest proof-of-work chain as the next block in the chain, and will begin building their block upon it. Occasionally, two blocks are discovered simultaneously, leading to one of those blocks being orphaned.
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[7]/button').click() # Complete Assessment (Next Button 7)
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[16]/a').click() # Process To Next Chapter
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div[2]/a').click() # 01 Proceed To Introduction read-through
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div/a').click() # 02 Commerce on the internet
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div/a').click() # 03 Non reversible transactions(TAKE THE ASSESSMENT)
#        time.sleep(0.8)
#        #Introduction Assessment No.1 (1/3)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[1]/a').click() # Next Button 1
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[2]/a[2]').click() # Next Button 2
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/form/div/div[3]/button').click() # Complete Assessment (Next Button 3)
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)
#        driver.find_element_by_xpath()
#        time.sleep(0.8)


#  Answer Course
# 04 Abstract Assessment No.1
# 
# Answer
# 
# 1. Public
# 2.Economics of processing each transaction
# 3.None of it
# 4.A sufficient value acceptable to transaction processors
# 
# 
# 08 Abstract Assessment No.2
# 
# Answer
# 
# 1. Sending a transaction and then sending a different transaction spending the same funds to a different address prior to confirmation of the original transaction.
# 2. Accumulation of proof-of-work
# 3. i) timestamp, ii) proof of their existence and validity.
# 4. Performed the work 
# 5. i) validating and storing, ii) proof of work, iii) hash
# 
# 
# 
# 13 Abstract Assessment No.3
# 
# Answer
# 
# 1. i) hashpower, ii) energy investment
# 2. i) double spends, ii) network hashpower 
# 3. Double spend
# 4. i) fee revenue ii) infrastructure
# 5. i) first seen, ii) double spending
# 6. The longest chain that is compliant to the network rules is valid.
# 7. Using block announcements, nodes accept the first valid block which builds upon the longest proof-of-work chain as the next block in the chain, and will begin building their block upon it. Occasionally, two blocks are discovered simultaneously, leading to one of those blocks being orphaned.
# 
# 
# 
# 04 Introduction Assessment No.1
# 
# Answer
# 
# 1.
# 2. The non-reversibility and low fees of Bitcoin, provides the best service.
# 3.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#