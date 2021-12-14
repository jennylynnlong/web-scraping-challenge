# imports
from splinter import Browser
from bs4 import BeautifulSoup as soup, FeatureNotFound
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

# scrape all function
def scrape_all():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # get information from news page
    news_title, news_p = scrape_news(browser)

    # build a dictionary using info from scrapes
    mars_data = {
        "NewsTitle": news_title,
        "NewsParagraph": news_p,
        "FeaturedImage": scrape_image(browser),
        "TableFacts": scrape_table(browser),
        "Hemispheres": scrape_hemispheres(browser),
        "LastUpdated": dt.datetime.now()
    }

    # stop the webdriver
    browser.quit()

    # display output
    return mars_data

# scrape mars news page
def scrape_news(browser):
    # go to site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object
    html = browser.html
    news_soup = soup(html, 'html.parser')

    slide_elem = news_soup.select_one('div.list_text')

    # Use the parent element to find the news_title
    news_title = slide_elem.find(class_='content_title').text

    # Use the parent element to find the news paragraph
    news_p = slide_elem.find(class_='article_teaser_body').text

    # return title and paragraph
    return news_title, news_p

# scrape featured image page
def scrape_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # Find and click the full image button
    full_image_link = browser.find_by_tag('button')[1]
    full_image_link.click()

    # Parse the resulting html with soup
    # Convert the browser html to a soup object
    html = browser.html
    space_image = soup(html, 'html.parser')

    # find the relative image url
    img_url_rel = space_image.find_all('img')[1]['src']

    # use the base url to create an absolute url
    featured_img_url = url+img_url_rel

    # return image url
    return featured_img_url

# scrape Mars-Earth comparison table page
def scrape_table(browser):
    # visit url
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    # Parse the resulting html with soup
    # Convert the browser html to a soup object
    html = browser.html
    table_soup = soup(html, 'html.parser')

    # find the table location
    table_location = table_soup.find('div', class_='diagram mt-4')
    
    # grab html code for table
    table = table_location.find('table')

    # create an empty string
    facts = ""

    # add text to empty string then return
    facts += str(table)

    # return table information
    return facts

# scrape through hemispheres pages
def scrape_hemispheres(browser):
    # visit base url
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # Create a list to hold the images and titles
    hemisphere_image_urls = []

    # Get a list of all of the hemispheres
    links = browser.find_by_css('a.product-item img')

    # Next, loop through those links, click the link, find the sample anchor, return the href
    for i in range(len(links)):
    
        # hemisphere info dictionary
        hemisphere_info = {}
        
        # We have to find the elements on each loop to avoid a stale element exception
        browser.find_by_css('a.product-item img')[i].click()
        
        # Next, we find the Sample image anchor tag and extract the href
        sample = browser.links.find_by_text('Sample').first
        hemisphere_info['img_url'] = sample['href']
        
        # Get Hemisphere title
        hemisphere_info['title'] = browser.find_by_css('h2.title').text
        
        # Append hemisphere object to list
        hemisphere_image_urls.append(hemisphere_info)
        
        # Finally, we navigate backwards
        browser.back()
    
    # return hemisphere information
    return hemisphere_image_urls

# set up flask app
if __name__ == "__main__":
    print(scrape_all())