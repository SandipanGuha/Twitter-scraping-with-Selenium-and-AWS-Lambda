#Twitter web scraping app to get 10 trending tweets 
#Written by Sandipan Guha 2023
#License: MIT 

import modules

target_url = 'https://twitter.com/explore/tabs/trending'



if __name__ == "__main__":
  
  api_driver = modules.configure_driver(target_url)
  get_elements = api_driver.find_elements
  print(api_driver.title)
  