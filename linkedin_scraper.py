from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openai
import os
import argparse
import random

openai.api_key = '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'

class LinkedInAutomation:

    def __init__(self):
        chrome_options = Options()
        home_directory = os.path.expanduser('~')

	# Define the path to the Chrome user data directory
        chrome_user_data_dir = os.path.join(home_directory, 'AppData', 'Local', 'Google', 'Chrome', 'User Data')
        chrome_options.add_argument(f'--user-data-dir={chrome_user_data_dir}')

        # jaffer path  service = ChromeService('C:\\Windows\\chromedriver-win64\\chromedriver.exe')
        service = ChromeService('C:\\Windows\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 30)  # Waiting for a maximum of 30 seconds

    def navigate_to_linkedin(self):
        self.driver.get('https://www.linkedin.com')
        time.sleep(15)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def enter_search_query(self, query):
        time.sleep(10)                                           
        input_text_element = self.driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
        time.sleep(5)                                                   
        for i in query:
            input_text_element.send_keys(i)
            dice_roll = random.randrange(1, 6)
            if dice_roll == 5 or dice_roll == 2:
                time.sleep(random.randrange(1, 3))
            else:
                time.sleep(random.choice([3.2, 1.4, 0.3, 2, 3, 0.9, 1.5, 2.6, 2.1, 3.3, 1.0, 3.6, 0.3, 0.2, 4.3, 1.9, 0,3.6]))
        #input_text_element.send_keys(query)

        input_text_element.send_keys(Keys.ENTER)
        time.sleep(12)

    def click_people_filter(self):
        Find_People=""
        Find_People_Index=0
        while(True):                                         
          try:                                                       
            Find_People=self.driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li['+str(Find_People_Index)+']/button').text
            if(Find_People=="People"):                          
                break 
            else: 
                Find_People_Index=Find_People_Index+1
          except:
                Find_People_Index=Find_People_Index+1

            
        time.sleep(3)
        people_filter_button = self.driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li['+str(Find_People_Index)+']/button')
        time.sleep(3)
        people_filter_button.click()
        time.sleep(5)
        
    def click_location_filter(self):
        print('inside location filter')
        
        time.sleep(5)
        currenturl=self.driver.current_url
        self.driver.get(currenturl)
        time.sleep(10)
        Find_Location=""
        Find_Location_Index=0
        found = 0
        while(True):
          try:							                     
            Find_Location=self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/section/div/nav/div/ul/li['+str(Find_Location_Index)+']/div/span/button').text      
            print('got location button')
            if(Find_Location=="Locations"):                                                      
                break
            else:
                Find_Location_Index=Find_Location_Index+1
          except:
                Find_Location_Index=Find_Location_Index+1
    
        time.sleep(5)
        location_filter_button = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/section/div/nav/div/ul/li['+str(Find_Location_Index )+']/div/span/button')
        location_filter_button.click()
        time.sleep(5)    
    
    def input_location(self, location):                         
        time.sleep(15)
        try:
            location_input_path = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/div/div/input')
            location_input_xpath = '/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/div/div/input'
        except:                                                             
            location_input_path = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/section/div/nav/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/div/div/input')
            location_input_xpath = '/html/body/div[4]/div[3]/div[2]/section/div/nav/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/div/div/input'
                                        #//*[@id="artdeco-hoverable-artdeco-gen-58"]/div[1]/div/form/fieldset/div[1]/div/div/input
        location_input = self.driver.find_element(by='xpath', value=location_input_xpath )
        for i in location:                                                
            location_input.send_keys(i)
            dice_roll = random.randrange(1, 5)
            if dice_roll == 5 or dice_roll == 2:
                time.sleep(random.randrange(1, 3))
            else:
                time.sleep(random.choice([3.2, 1.4, 0.3, 2, 3, 0.9, 1.5, 2.6, 2.1, 3.3, 1.0, 3.6, 0.3, 0.2, 4.3, 1.9, 0,3.6]))
        
        location_input.send_keys(Keys.DOWN)
        location_input.send_keys(Keys.ENTER)
        time.sleep(5)    

    def click_apply_filter(self):
        time.sleep(5)                                     
        apply_button = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/section/div/nav/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]')
        apply_button.click()                                
        time.sleep(5)
        
    def LinkedinCommentCreator(self, post):
        prompt = post
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a content writer, your job is to make a professional comment content of this post. make short replies. Max words should be 20 words"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1)
        if response and 'choices' in response and len(response['choices']) > 0:
            comment = response['choices'][0]['message']['content']
            return comment
    
    def scrape_home_posts(self):  
        print(f"Enter in home posts ")                             
        count = 1                                              
        while(True):                                       
            try:
                try:                   
                    elem = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div/div/div/div/div[5]/div/div').text                
                    elem_path = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div/div/div/div/div[5]/div/div'     
                except:                           
                    elem = self.driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div/div/div/div/div[4]/div/div').text
                    elem_path = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div/div/div/div/div[4]/div/div'       
                elem = self.driver.find_element(By.XPATH,value= elem_path).text                                  
                comment_data = self.LinkedinCommentCreator(elem)
                time.sleep(2)  
                
                try:
                    comment_button = self.driver.find_element(by='xpath', value= '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div/div/div/div[6]/div[2]/span[2]/span/div[1]/button')
                    comment_buttton_path = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div/div/div/div[6]/div[2]/span[2]/span/div[1]/button'
                except:                                        
                    comment_button = self.driver.find_element(by='xpath', value= '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div/div/div/div/div[7]/div[2]/span[2]/span/div[1]/button')
                    comment_buttton_path = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div/div/div/div/div[7]/div[2]/span[2]/span/div[1]/button'
                                                                                            
                comment_button = self.driver.find_element(by='xpath', value= comment_buttton_path)
                comment_button.click()                                          
                print("Opened the comment")
                time.sleep(5)  
                
                try:
                    comment_field_xpath = self.driver.find_element(by='xpath', value= '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div/div/div/div/div[7]/div[3]/div[1]/div[2]/form/div/div/div[1]/div/div/div/div/div[1]/p')  
                    comment_field_path =  '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div/div/div/div/div[7]/div[3]/div[1]/div[2]/form/div/div/div[1]/div/div/div/div/div[1]/p' 
                except:
                    comment_field_xpath = self.driver.find_element(by='xpath', value= '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div[1]/div/div/div[7]/div[3]/div[1]/div[2]/form/div/div/div[1]/div/div/div/div/div[1]/p')  
                    comment_field_path = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div[1]/div/div/div[7]/div[3]/div[1]/div[2]/form/div/div/div[1]/div/div/div/div/div[1]/p'
                     
                comment_field = self.driver.find_element(by='xpath', value= comment_field_path)
                comment_field.clear()
                comment_field.send_keys(comment_data )
                print("Wrote in comment")
                time.sleep(5)
                
                try:
                    comment_button = self.driver.find_element(by='xpath', value= '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div/div/div/div/div[7]/div[3]/div[1]/div[2]/form/div[2]/button')
                    comment_buttton_path = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div/div/div/div/div[7]/div[3]/div[1]/div[2]/form/div[2]/button'                           
                except:                     
                    comment_button = self.driver.find_element(by='xpath', value= '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div[1]/div/div/div[7]/div[3]/div[1]/div[2]/form/div[2]/button')
                    comment_buttton_path = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[4]/div/div[1]/div['+str(count)+']/div/div[1]/div/div/div[7]/div[3]/div[1]/div[2]/form/div[2]/button'
                       
                comment_button_press = self.driver.find_element(by='xpath', value= comment_buttton_path)
                comment_button_press.click()
                if(count==2):
                    break
                count=count+1
                #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            except:
                count=count+1
                time.sleep(3)
                
    def people_posts_commentor(self, no_of_posts):
        count=0
        post_count = no_of_posts
        while(True):    
                    try:
                        elem = self.driver.find_element(by='xpath', value= '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[4]/div/div').text                                  
                        comment_data = self.LinkedinCommentCreator(elem)
                        comment_button = self.driver.find_element(by='xpath', value= '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[5]/div[2]/span[2]/span/div[1]/button')
                        comment_button.click()
                        print("Opened the comment")
                        comment_field_xpath = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[6]/div[3]/div[1]/div[2]/form/div/div/div[1]/div/div/div/div/div[1]'   
                        comment_field = self.driver.find_element(by='xpath', value= comment_field_xpath) 
                        comment_field.clear()
                        comment_field.send_keys(comment_data )
                        print("Wrote in comment")
                        comment_post_button_xpath = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[5]/div[3]/div[1]/div[2]/form/div[2]/button'   
                        comment_post = self.driver.find_element(by='xpath', value= comment_post_button_xpath)
                        comment_post.click()
                        
                    except Exception as e:
                        print(f"Could not wrote in 'comment' field: {e}")   
                        time.sleep(5)  
                    count=count+1
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    if(count==2):
                        break        
                        
    def scrape_Search_posts(self):
        time.sleep(5)
        profile_count=1
        people_names = []
        next_page = False
        found=0
        currenturl=self.driver.current_url
          
        #currenturl = 'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22104341318%22%5D&keywords=finance&origin=FACETED_SEARCH&searchId=1c5d7dc4-4eb7-40ac-a1d6-698a2ce6cb45&sid=bsc'
        #print(currenturl)
        while(True):
            self.driver.get(currenturl)
            print('first while loop')
            if(next_page == True):
                print('inside pagination loop')
                time.sleep(15)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(15)
                try:                                                       
                    pagination_button = self.driver.find_element(By.XPATH, '//*[@id="ember71"]')
                except:                                                                               
                    pagination_button = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[5]/div/div/button[2]/span')
                                                        
                     #found_pagination_button = False
                     #for count1 in range(4, 6):
                     #   if found_pagination_button:
                     #        break
                     #    for count2 in range(5, 8):  # This will iterate from 5 to 7
                     #       pagination_button_xpath = '/html/body/div['+str(count1)+']/div[3]/div[2]/div/div[1]/main/div/div/div['+str(count2)+']/div/div/ul/li['+str(page_count)+']/button'
                             
                     #        try:
                     #            pagination_button = self.driver.find_element(by='xpath', value=pagination_button_xpath)
                      #           found_pagination_button = True  
                      #           break  
                      #       except Exception as e:
                       #          print(f"Could not find pagination button: {e}")
                time.sleep(5)
                if pagination_button:
                    pagination_button.click()
                else:
                    next_page = False
                    break
                time.sleep(15)
                currenturl = self.driver.current_url
            else:
               currenturl=self.driver.current_url
            
            while(True):   
                self.driver.get(currenturl)
                print('second while loop')
                time.sleep(8)
                try:                                                                  
                                                                                                                                                                                       
                    try:                               
                        person_name = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li['+str(profile_count)+']/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]').text
                        found=1                                           
                    except:                                                                                                                     
                        person_name = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li['+str(profile_count)+']/div/div/div[2]/div[1]/div[1]/div/span/span/a').text
                        found=1
                        
                    if found==0:                                               
                        try:                                #  jaffar name path  /html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li['+str(count)+']/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a
                            person_name = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li['+str(profile_count)+']/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]').text
                        except:                                                                                                                     
                            person_name = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li['+str(profile_count)+']/div/div/div[2]/div[1]/div[1]/div/span/span/a').text
                    print(profile_count)
                    if person_name == 'LinkedIn Member' or person_name in people_names:
                            print(f"{person_name} already in people_names list. Skipping.")
                            if(profile_count==4):
                                next_page = True
                                break
                            profile_count=profile_count+1
                           
                    else:
                        time.sleep(8)
                        people_names.append(person_name)
                        
                        if(found==1):
                            profile_link = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li['+str(profile_count)+']/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a')                                 
                        else:                                                  
                            profile_link = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li['+str(profile_count)+']/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a')
                        time.sleep(5)                                             
                        profile_link.click()                               
                        time.sleep(5) 
                        
                        #try:                               
                        #    follow_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button/span').text
                        #    follow_button_path='/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button/span'                                           
                        #except:                                                                                                                      
                        #   follow_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button/span').text
                        #    follow_button_path='/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button/span'
 
                        #if follow_button == 'Follow':
                        #    find_follow_button = self.driver.find_element(by='xpath', value= follow_button_path)
                        #    find_follow_button.click()
                        #    print("Followed the account")
                        #    time.sleep(10)
                    
                           
                        try:
                            show_all_post_index=1 
                            try:
                                while(True):
                                    try:
                                        try:                     
                                         show_all_posts = self.driver.find_element(by='xpath', value= '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section['+str(show_all_post_index)+']/footer/a')
                                         element_for_press_All_Post='/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section['+str(show_all_post_index)+']/footer/a'
                                        except:                                     
                                         show_all_posts = self.driver.find_element(by='xpath', value= '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section['+str(show_all_post_index)+']/footer/a')
                                         element_for_press_All_Post='/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section['+str(show_all_post_index)+']/footer/a'
    
                                        if(show_all_posts.text=='Show all posts'):
                                            break
                                        else:
                                            show_all_post_index=show_all_post_index+1
                                    except:
                                        show_all_post_index=show_all_post_index+1
                                        if(show_all_post_index==10):
                                            break
                            except:
                                show_all_post_index=show_all_post_index+1
                                
                            if(show_all_post_index < 10):
                                time.sleep(10)
                                show_all_posts_button = self.driver.find_element(by='xpath', value= element_for_press_All_Post)
                                show_all_posts_button.click()
                                print("Show all posts")
                                time.sleep(10)
                                post_count = 1
                                while(True):   
                                    print('third while loop')
                                    try:       
                                        currenturl=self.driver.current_url
                                        self.driver.get(currenturl)
                                        time.sleep(20)
                                        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                        time.sleep(5)

                                        try:    
                                            
                                            elem = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[5]/div/div').text
                                            profile_post_script_elem = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[5]/div/div'
                                        except:                                                                                                           
                                            elem = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[4]/div/div').text
                                            profile_post_script_elem = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[5]/div/div'
                                        elem = self.driver.find_element(By.XPATH, profile_post_script_elem).text                                  
                                        comment_data = self.LinkedinCommentCreator(elem) 
                                        time.sleep(5)
                                        filtered_comment_data = comment_data.encode('utf-16', 'ignore').decode('utf-16')
                                        time.sleep(10)
                                        print('gpt api response')
                                        
                                        try:                                                                                                                                          
                                            comment_button = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[5]/div[2]/span[2]/span/div[1]/button')
                                            comment_buttton_path = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[5]/div[2]/span[2]/span/div[1]/button'
                                            comment_button = self.driver.find_element(by='xpath', value= comment_buttton_path)
                                        except:                                         
                                               found_comment_button = False
                                               for count in range(4, 6):
                                                   time.sleep(2)
                                                   if found_comment_button:
                                                       break
                                                   for count1 in range(5, 8):  # This will iterate from 5 to 7
                                                       comment_button_xpath = '/html/body/div[' + str(count) + ']/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[' + str(count1) + ']/div[2]/span[2]/span/div[1]/button'
                                                       try:   
                                                           time.sleep(2)       
                                                           comment_button = self.driver.find_element(by='xpath', value=comment_button_xpath)
                                                           found_comment_button = True  # Set the flag to True if the button was found
                                                           break  # Exit the inner loop if the button was found
                                                       except Exception as e:
                                                           print(f"Could not find comment button: {e}")
                                        time.sleep(15)
                                        comment_button.click()                                          
                                        print("Opened the comment")
                                        time.sleep(10)    
                                        
                                        try:   
                                            time.sleep(5)
                                            comment_field_xpath = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[7]/div[3]/div[1]/div[2]/form/div/div/div[1]/div/div/div/div/div[1]/p')  
                                            comment_field_path = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[7]/div[3]/div[1]/div[2]/form/div/div/div[1]/div/div/div/div/div[1]/p'
                                            comment_field = self.driver.find_element(by='xpath', value= comment_field_path)
                                        except:                             
                                            found_comment_field = False
                                            for count2 in range(4, 6):
                                                if found_comment_field:
                                                    break
                                                for count3 in range(5, 8):  # This will iterate from 5 to 7
                                                    comment_field_xpath = '/html/body/div[' +str(count2)+ ']/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li[' +str(post_count)+ ']/div/div/div[2]/div/div/div[' +str(count3)+ ']/div[3]/div[1]/div[2]/form/div/div/div[1]/div/div/div/div/div[1]/p'
                                                    try:
                                                        comment_field = self.driver.find_element(by='xpath', value=comment_field_xpath)
                                                        found_comment_field = True  # Set the flag to True if the button was found
                                                        break  # Exit the inner loop if the button was found
                                                    except Exception as e:
                                                        print(f"Could not find comment field: {e}")
                                                        
                                                           
                                        #if found_comment_field == False:
                                        #    profile_count=profile_count+1
                                        #    break
                                        print("Got the comment filed")
                                        time.sleep(10)
                                        comment_field.clear()
                                        for i in comment_data:
                                            comment_field.send_keys(i)
                                            dice_roll = random.randrange(1, 6)
                                            if dice_roll == 5 or dice_roll == 2:
                                                time.sleep(1)
                                            else:
                                                time.sleep(random.choice([1.2, 1.4, 0.3, 1, 2.9, 1.5, 2.6, 1.1, 3.3, 1.0, 1.6, 0.3, 0.2, 1.8, 1.9, 0,1.6]))

                                        print("Wrote in comment")    
                                        time.sleep(10)  
                                                                  
                                        try:                                                                    
                                            comment_post_button_xpath = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[7]/div[3]/div[1]/div[2]/form/div[2]/button')  
                                            comment_post_button_path = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[7]/div[3]/div[1]/div[2]/form/div[2]/button'
                                        except:                         
                                               found_comment_button = False
                                               for count in range(4, 6):
                                                   if found_comment_button:
                                                       break
                                                   for count1 in range(5, 8):  # This will iterate from 5 to 7
                                                       comment_button_xpath = '/html/body/div['+str(count)+']/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div['+str(count1)+']/div[3]/div[1]/div[2]/form/div[2]/button'
                                                       
                                                       try:
                                                           comment_button = self.driver.find_element(by='xpath', value=comment_button_xpath)
                                                           found_comment_button = True  # Set the flag to True if the button was found
                                                           break  # Exit the inner loop if the button was found
                                                       except Exception as e:
                                                           print(f"Could not find comment button: {e}")

                                        comment_button.click()
                                        print(f"Wrote 'comment' post ")
                                        time.sleep(8)
                                        if(post_count==2):
                                            break
                                        post_count=post_count+1
    
                                    except Exception as e: 
                                        print(f"Could not wrote in 'comment' field: {e}")   
                                        time.sleep(5) 
                                if(profile_count>4):
                                    next_page = True
                                    break
                                profile_count=profile_count+1
                                continue  
                                    
                        except Exception as e:
                            print(f"Could not click on the 'show all posts' button: {e}")  
                            time.sleep(10)
                             
                        
                            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        if(profile_count==4):
                            next_page = True
                            break
                        profile_count=profile_count+1
                        
                    
                except:
                    time.sleep(3) 
                    if(profile_count==4):
                       next_page = True
                       break
                   
                    profile_count=profile_count+1
       
    def scrape_connection(self):
        time.sleep(5)
        profile_count=6
        found=0
        people_names = []
        currenturl= 'https://www.linkedin.com/mynetwork/invite-connect/connections/'
        while(True):   
            self.driver.get(currenturl)
            time.sleep(10)
            try:                                                 
                try:                        
                    person_name = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div/div[2]/div/div/main/div/section/div[2]/div[1]/ul/li['+str(profile_count)+']/div/div/div[2]/a/span[2]').text
                    found=1                                           
                    #person_name_path = '/html/body/div[4]/div[3]/div/div/div/div/div[2]/div/div/main/div/section/div[2]/div[1]/ul/li['+str(profile_count)+']/div/div/div[2]/a/span[2]'
                except: 
                    found_person_name = False
                    for count5 in range(4, 6):
                        if found_person_name:
                            break
                        for count6 in range(1, 3):  # This will iterate from 5 to 7
                            person_field_xpath = '/html/body/div[' + str(count5) + ']/div[3]/div/div/div/div/div[2]/div/div/main/div/section/div[2]/div[1]/ul/li['+str(profile_count)+']/div/div/div[' + str(count6) + ']/a/span[2]'
                                   
                            try:
                                person_name = self.driver.find_element(by='xpath', value=person_field_xpath).text
                                found_person_name = True  # Set the flag to True if the button was found
                                found=0
                                break  # Exit the inner loop if the button was found
                            except Exception as e:
                                print(f"Could not find comment field: {e}")                                                                                                                                                                                                                             
                    
                if person_name == 'LinkedIn Member' or person_name in people_names:
                        print(f"{person_name} already in people_names list. Skipping.")
                        profile_count=profile_count+1 
                else:
                    people_names.append(person_name)
                    if(found==1):
                        profile_link = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div/div[2]/div/div/main/div/section/div[2]/div[1]/ul/li['+str(profile_count)+']/div/div/div[2]/a') 
                    else:
                        profile_link_xpath = person_field_xpath.replace('/span[2]',"")
                        profile_link = self.driver.find_element(by='xpath', value = profile_link_xpath )
                        
                    profile_link.click()                               
                    time.sleep(5) 
                    #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    #time.sleep(5)
                    try:
                        show_all_post_index=1
                        try:
                            while(True):
                                try:
                                    try:                                                                                                                         
                                     show_all_posts = self.driver.find_element(by='xpath', value= '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section['+str(show_all_post_index)+']/footer/a')
                                     element_for_press_All_Post='/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section['+str(show_all_post_index)+']/footer/a'
                                    except:                                                                                  
                                     show_all_posts = self.driver.find_element(by='xpath', value= '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section['+str(show_all_post_index)+']/footer/a')
                                     element_for_press_All_Post='/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section['+str(show_all_post_index)+']/footer/a'

                                    if(show_all_posts.text=='Show all posts'):
                                        break
                                    else:
                                        show_all_post_index=show_all_post_index+1
                                except:
                                    print("except 1")
                                    show_all_post_index=show_all_post_index+1
                                    if(show_all_post_index==10):
                                        break
                        except:
                            print("except 2")
                            show_all_post_index=show_all_post_index+1
                            
                            
                        if(show_all_post_index < 10):
                            
                            show_all_posts_button = self.driver.find_element(by='xpath', value= element_for_press_All_Post)
                            time.sleep(5)
                            show_all_posts_button.click()
                            print("Show all posts")
                            time.sleep(6)
                            post_count = 1
                            while(True):    
                                try:
                                    time.sleep(15)
                                    try:
                                        elem = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[4]/div/div').text
                                        profile_post_script_elem = '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[4]/div/div'
                                    except:                                                                                                                                                
                                        elem = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[5]/div/div').text
                                        profile_post_script_elem = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[5]/div/div'
                                    elem = self.driver.find_element(By.XPATH, profile_post_script_elem).text                                  
                                    comment_data = self.LinkedinCommentCreator(elem) 
                                    filtered_comment_data = comment_data.encode('utf-16', 'ignore').decode('utf-16')
                                    
                                    try:                          
                                        comment_button = self.driver.find_element(by='xpath', value= '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[7]/div[2]/span[2]/span/div[1]/button')
                                        comment_buttton_path = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[7]/div[2]/span[2]/div[1]/button'
                                        comment_button = self.driver.find_element(by='xpath', value= comment_buttton_path)
                                    except:                                                                                                                  
                                        found_comment_button = False
                                        for count in range(4, 6):
                                            if found_comment_button:
                                                break
                                            for count1 in range(5, 8):  # This will iterate from 5 to 7
                                                comment_button_xpath = '/html/body/div[' + str(count) + ']/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[' + str(count1) + ']/div[2]/span[2]/div[1]/button'
                                                try:       
                                                    comment_button = self.driver.find_element(by='xpath', value=comment_button_xpath)
                                                    found_comment_button = True  # Set the flag to True if the button was found
                                                    break  # Exit the inner loop if the button was found
                                                except Exception as e:
                                                    print(f"Could not find comment button: {e}")

                                    comment_button.click()                                          
                                    print("Opened the comment")
                                    time.sleep(5)     
                                    
                                    try:
                                        comment_field_xpath = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[7]/div[3]/div[1]/div[2]/form/div/div/div[1]/div/div/div/div/div[1]/p')  
                                        comment_field_path = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[7]/div[3]/div[1]/div[2]/form/div/div/div[1]/div/div/div/div/div[1]/p'
                                        comment_field = self.driver.find_element(by='xpath', value= comment_field_path)
                                    except:                                                                           
                                        found_comment_field = False
                                        for count in range(4, 6):
                                            if found_comment_field:
                                                break
                                            for count1 in range(5, 8):  # This will iterate from 5 to 7
                                                comment_field_xpath = '/html/body/div[' +str(count)+ ']/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li[' +str(post_count)+ ']/div/div/div[2]/div/div/div[' +str(count1)+ ']/div[3]/div[1]/div[2]/form/div/div/div[1]/div/div/div/div/div[1]/p'
                                                       
                                                try:
                                                    comment_field = self.driver.find_element(by='xpath', value=comment_field_xpath)
                                                    found_comment_field = True  # Set the flag to True if the button was found
                                                    break  # Exit the inner loop if the button was found
                                                except Exception as e:
                                                    print(f"Could not find comment field: {e}")
                                    
                                    print("Got the comment filed")
                                    comment_field.clear()
                                    
                                    for i in filtered_comment_data:
                                        comment_field.send_keys(i)
                                        dice_roll = random.randrange(1, 6)
                                        if dice_roll == 5 or dice_roll == 2:
                                            time.sleep(1)
                                        else:
                                            time.sleep(random.choice([1.2, 1.4, 0.3, 1, 0.9, 1.5, 2.6, 1.1, 3.3, 1.0, 1.6, 0.3, 0.2, 1.8, 1.9, 0,1.6]))       
                                    print("Wrote in comment")    
                                    time.sleep(10)   
                                    
                                    try:   
                                        print("Inside comment post button try") 
                                        comment_post_button_xpath = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[7]/div[3]/div[1]/div[2]/form/div[2]/button')  
                                        comment_post_button_path = '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div[7]/div[3]/div[1]/div[2]/form/div[2]/button'
                                        #comment_post_button = self.driver.find_element(by='xpath', value= comment_post_button_path)
                                    except:   
                                        print("Inside comment post button else")
                                        found_comment_post_button = False
                                        for count2 in range(4, 6):
                                            if found_comment_post_button:
                                                break
                                            for count3 in range(5, 8):  # This will iterate from 5 to 7
                                                comment_button_xpath = '/html/body/div['+str(count2)+']/div[3]/div/div/div[2]/div/div/main/div/section/div[2]/div/div/div[1]/ul/li['+str(post_count)+']/div/div/div[2]/div/div/div['+str(count3)+']/div[3]/div[1]/div[2]/form/div[2]/button'
                                                                        
                                                try:
                                                    comment_post_button = self.driver.find_element(by='xpath', value=comment_button_xpath)
                                                    found_comment_post_button = True  # Set the flag to True if the button was found
                                                    break  # Exit the inner loop if the button was found
                                                except Exception as e:
                                                    print(f"Could not find comment post button: {e}")

                                    comment_post_button.click()
                                    time.sleep(5)
                                    print(f"Wrote 'comment' on first post ")
                                    if(post_count==1):
                                        break
                                    post_count=post_count+1

                                except Exception as e: 
                                    print(f"Could not wrote in 'comment' field: {e}")   
                                    time.sleep(5)
                                    post_count=post_count+1
                                    continue
                            
                            if(profile_count==10):
                                break
                            profile_count=profile_count+1    
                            continue  
                                
                    except Exception as e:
                        print(f"Could not click on the 'show all posts' button: {e}")  
                        time.sleep(5)
                        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    if(profile_count==10):
                        break
                    profile_count=profile_count+1    
                    continue
            except:
                profile_count=profile_count+1
                time.sleep(3)
        

    def quit_browser(self):
        time.sleep(30)
        self.driver.quit()

if __name__ == '__main__':
    automation = LinkedInAutomation()
    
# Check the user input    
    parser = argparse.ArgumentParser(description="Data scraper")
    parser.add_argument("-query", type=str, help="Query")
    parser.add_argument("-location", type=str, help="Location")
    parser.add_argument("-value", type=str, help="Home OR Connections")

    args = parser.parse_args()

    query = args.query
    location = args.location
    value = args.value
    
    if value  == "Home":
        print("Checking Home functionality 'Home'. Performing function.")
        automation.navigate_to_linkedin()
        #automation.scrape_home_posts()
        #automation.quit_browser()
    
    elif value == 'Connections':  
        print("Checking 'Connections'. Performing function.")
        automation.navigate_to_linkedin()
        automation.scrape_connection()
        automation.quit_browser() 
        
    else:
        print("You entered 'Search'. Performing function.")
        print(location)
        print(query)
        automation.navigate_to_linkedin()
        automation.enter_search_query(query)
        automation.click_people_filter()
        automation.click_location_filter()
        automation.input_location(location)
        automation.click_apply_filter()
        automation.scrape_Search_posts()
        automation.quit_browser() 
