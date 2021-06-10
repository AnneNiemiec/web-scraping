#Dependencies
import pandas as pd 
from splinter import Browser
from bs4 import BeautifulSoup as bs 
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser

def browser_start():

    # Run the browser start
    executable_path = {'executable_path':ChromeDriverManager().install()}
    
    return Browser('chrome', **executable_path)

def NASA_News(browser):

    NASA_News="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(NASA_News)

    html = browser.html
    soup = bs(html, "html.parser")
    Text=soup.select_one("div.list_text")
    NASA_title=Text.find('div', class_='content_title').get_text()
    NASA_paragraph=Text.find('div', class_='article_teaser_body').get_text()

    return NASA_title, NASA_paragraph

def Space_News(browser):

    Space_News="https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(Space_News)

    featured_image_url=browser.find_by_tag('button')[1]
    featured_image_url.click()
    html = browser.html
    Space_html = bs(html, "html.parser")
    Space_image=Space_html.find('img', class_='fancybox-image').get("src")
    return Space_image 

def mars_facts():
    mars_facts=pd.read_html("https://space-facts.com/mars/")[0]
    mars_facts.columns=['mars_facts','terrestrial_planet ']
    mars_facts.set_index('mars_facts', inplace=True)
    mars_html = mars_facts.to_html()
    return mars_html

def astrogeology(browser):
        
    astrogeology="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(astrogeology)
    hemisphere_links=browser.find_by_css('a.product-item img')
    len(hemisphere_links)

    astrogeology=[]
    hemispheres=["Cereberus", "Schiaparelli", "Syrtis", "Valles"]
    for i in range(len(hemispheres)):
        browser.find_by_css('a.product-item img')[i].click()
        dictionary={}
        html = browser.html
        soup = bs(html, "html.parser")
        images=soup.find_all('img', class_='wide-image')[0].get("src")
        titles=soup.find('div', class_='content').find('h2',class_='title')
        dictionary['title']=titles
        dictionary['url']=images
        astrogeology.append(dictionary)
        browser.back()
    return astrogeology

    #initialize browser and create function
def initialize():
    browser=browser_start()

    #Create variables
    title, paragraph= NASA_News(browser)
    image= Space_News(browser)
    facts= mars_facts()
    hemispheres= astrogeology(browser)

    Dictionary={
        "mars_title":title, 
        "mars_paragraph": paragraph,
        "Space_News": image,
        "mars_facts":facts,
        "hemispheres": hemispheres
    }

    browser.quit()

    return Dictionary





