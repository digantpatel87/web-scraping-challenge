from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape():
#def scrape_NASAMarsNews():
    # browser = init_browser() get information from NASA Mars News
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_title = soup.find("div", class_="content_title").get_text()
    news_title = news_title.replace("'", "")
    news_p = soup.find("div", class_="article_teaser_body").get_text()
    news_p = news_p.replace("'", "")
   
    # Quit the browser
    browser.quit()
    
    # get from image from JPL Mars Space Images - Featured Image
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit visitcostarica.herokuapp.com
    url = "https://spaceimages-mars.com/"
    browser.visit(url)


    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    featured_image_path = soup.find_all('img')[2]["src"]
    featured_image_url = url + featured_image_path

    # Close the browser after scraping
    browser.quit()
    
    #get Mars Facts
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    tables
    df = tables[1]
    MarsFacts_df = df.rename(columns={0:"Profile",1:"Value"}, errors="raise")
    MarsFacts_df.set_index("Profile",inplace=True)
    
    fact_table=MarsFacts_df.to_html()
    fact_table= fact_table.replace('\n','')

    #get Mars Hemispheres images information
    # Store data in a dictionary
    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"},
        {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"}
    ]
    
      
    FinalDictionary ={
        'news_title':news_title,
        'news_p': news_p,
        'featured_image_url' : featured_image_url,
        "fact_table":fact_table,
        'hemisphere' : hemisphere_image_urls
    }


    return FinalDictionary
    
#if __name__ == "__main__":
#   print(scrape())