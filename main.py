from myprotein_scrap import Protein
from sqlalchemy import create_engine
import pandas as pd
import json

if __name__ == '__main__':
    print("Retreiving credentials")
    with open('database_credentials.json') as cred:
        database_cred = json.load(cred)

    Rds_Host = database_cred['RDS_HOST']
    Rds_Password = database_cred['RDS_PASSWORD']
    Rds_Port = database_cred['RDS_PORT']

    #Retieve all new data 
    bot = Protein()
    bot.close_ad('//button[@class="emailReengagement_close_button"]')
    bot.accept_cookies('//*[@id="home"]/div[1]/div/div/div[2]/button')
    bot.click_search_bar('//*[@id="nav"]/div[2]/div[2]/div[2]/div/form/div')
    bot.find_protein(Key_word = "protein")
    bot.click_start_search('//*[@id="nav"]/div[2]/div[2]/div[2]/div/form/div/button[2]')
    bot.protein_link_list()
    clean_link_list = bot.removing_link_list_duplicates()
    myprotein_info = bot.protein_info(clean_link_list)
    

    print('comnnecting to the database')
    my_db =create_engine(f'postgresql+psycopg2://postgres:{Rds_Password}@{Rds_Host}:{Rds_Port}/myprotein-scrapper')
    print('Connected Successfully')
    myprotein_info.to_sql('myprotein_info', my_db, if_exists='replace', index=False)
    print('Done')
    
    