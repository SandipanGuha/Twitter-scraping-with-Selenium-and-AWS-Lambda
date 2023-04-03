#Twitter web scraping app to get 10 trending tweets 
#Written by Sandipan Guha 2023
#License: MIT 

import modules
import re

target_url = 'https://twitter.com/explore/tabs/trending'



if __name__ == "__main__":
  
  api_driver = modules.configure_driver(target_url)
  
  print(api_driver.title)
  def trending_data(driver):
    get_elements = api_driver.find_elements    
    divs = get_elements(modules.By.CLASS_NAME,'r-1adg3ll')
    trending=[]
    append = False
    for i in divs:
      for j in i.find_elements(modules.By.TAG_NAME,'span'):
        if re.match(r'^1$',j.text) or re.match(r'^11$',j.text):
          append = not append
        
        if append and j.text!='·':
          trending.append(j.text)
    out=[]
    temp=[]
    for item in trending:
    
      if re.match(r'^([1-9]|10)$',item):
        if temp:
          out.append(temp.copy())
          temp.clear()
      else:
        temp.append(item)
    else:
      out.append(temp.copy())
      del temp
    return out
    
  df = modules.pandas.DataFrame(trending_data(api_driver))
  #df.to_csv("Top 10 Twitter trends.csv")
  print(df)
        
        
        
  
  