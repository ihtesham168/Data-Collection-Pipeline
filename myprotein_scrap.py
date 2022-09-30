#Importing all essential libraries

from logging import exception
import time 
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
#Protein scrapper class
class Protein():
#Intializing method to get access to Myprotein webpage
    def __init__(self, sleep_time=2 , url: str ='https://www.myprotein.com/', link_list= [] ):
        options = Options()
        options.add_argument('headless')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')        
        self.link_list = link_list
        self.driver = Chrome(ChromeDriverManager().install(),chrome_options=options)
        self.driver.maximize_window()
        self.driver.get(url)
        self.sleep_time = time.sleep(sleep_time)
#Method to click elements in xpath
    def click_element(self, xpath:str):       
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
        self.sleep_time
#Method to close pop-up ad
    def close_ad(self, xpath:str ):
        self.click_element(xpath)
        self.sleep_time
#Method to accept cookies by clicking on accept button
    def accept_cookies(self, xpath:str):       
        self.click_element(xpath)
        self.sleep_time
#Method to click on search bar to find products
    def click_search_bar(self, xpath:str ):
       self.click_element(xpath)   
       self.sleep_time
#Method to find protein and sending keyword in protein to search bar 
    def find_protein(self, Key_word  ):
       TEXT_protein =self.driver.find_element(By.XPATH, value= '//*[@id="header-search-input"]' )
       TEXT_protein.send_keys(Key_word)
       self.sleep_time
#Method to click on start search button
    def click_start_search(self, xpath:str ):
        self.click_element(xpath)
        self.sleep_time
#Collecting all the href's and storing them in list
    def protein_link_list(self):
        links = self.driver.find_elements(By.XPATH, value= '//a[@class="athenaProductBlock_linkImage"]')                
        for link in links:
            link_to_page = link.get_attribute("href")        
            self.link_list.append(link_to_page)
            self.sleep_time
#Removing all the href's duplicate and converting them in list
    def removing_link_list_duplicates(self):
        unique_link_list_set = set(self.link_list)
        unique_href_list= list(unique_link_list_set)
        self.sleep_time
        return(unique_href_list)
#Collecting protein data from the href,s we obtained
    def protein_info(self, unique_href_list):
        info_list=[]        
        for item in unique_href_list:
            self.driver.get(item)
            #all protein data will be stored in dic_proteins
            dict_proteins ={
                "Name" : [] , "Price": [], "Reviews" :[], "Flavours": [], "Key Benefits":[]
            }           
            try:
                product_name = self.driver.find_element(By.XPATH, value = '//h1[@class="productName_title"]').text
                
                dict_proteins['Name'] = product_name
            except:
                dict_proteins['Name'].append("null")
            
            self.sleep_time
            # try:
            #     orignal_price = self.driver.find_element(By.XPATH, value  ='//p[@class="productPrice_rrp"]').text
            #     dict_proteins['Orignal Price']=orignal_price
            # except:
            #     dict_proteins['Orignal Price'].append('No Discount')            
            try:    
                discounted_price = self.driver.find_element(By.XPATH, value = '//p[@class="productPrice_price  "]').text
                dict_proteins['Price']= discounted_price
            except:
                dict_proteins['Price'].append("null")
            try:
                product_review = self.driver.find_element(By.XPATH, value = '//span[@class="productReviewStars_numberOfReviews"]' ).text
                dict_proteins['Reviews']= product_review
            except:
                dict_proteins['Reviews'].append("null")
            self.sleep_time
                
            try:
                product_flavours = self.driver.find_element(By.XPATH, value='//*[@id="athena-product-variation-dropdown-5"]')
                product_flavours.click()
                option_tag = product_flavours.find_elements(By.XPATH, value='.//option')

                flavour_list = []
                for flav in option_tag:
                    flavour_list.append(flav.text)
                    flavours = ", ".join(flavour_list)
                dict_proteins['Flavours'] = flavours
            except:
                dict_proteins['Flavours'].append("null")                
            self.sleep_time
            try:
                
                elements  = self.driver.find_element(By.XPATH, value='//button[@id="product-description-heading-lg-4"]')
                self.sleep_time
                self.driver.execute_script("arguments[0].click();", elements )               
                div_tag= elements.find_element(By.XPATH, value='//div[@id="product-description-content-lg-4"]')
                ul_tag= div_tag.find_element(By.XPATH, value='.//ul')
                li_tag= ul_tag.find_elements(By.XPATH, value='.//li')
                benefits = []
                for items in li_tag:                    
                    benefits.append(items.text)                    
                key_benefits = ", ".join(benefits)
                dict_proteins['Key Benefits'] = key_benefits 
                self.sleep_time
            except Exception as e:
                print(e)
                dict_proteins['Key Benefits'].append('null')                                    
            info_list.append(dict_proteins)
        df_data = pd.DataFrame(info_list)
        print(df_data)
        return df_data

if __name__ =="__main__":
    bot =  Protein()