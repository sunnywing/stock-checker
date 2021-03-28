from selenium.webdriver import Chrome #next step let's scrape brand name and model number from bb and ne
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
opts = Options()
opts.headless = True
browser = Chrome(options=opts)
link = []
with open('C:/Users/pluhm/Documents/graphics_links.txt', 'r') as f:
    for line in f:
        link = line.strip()
        browser.get(link)

        if "bestbuy" in link:
            web_class = (
                "sku-title", #title
                "div.priceView-hero-price.priceView-customer-price", #price
                "div.fulfillment-add-to-cart-button" #status
            )
            
            title = browser.find_element_by_class_name(web_class[0]).text
            #price = browser.find_element_by_css_selector(web_class[1]).text
            html = browser.page_source
            soup = BeautifulSoup(html, 'html.parser')
            price = soup.find("div", class_="priceView-price-match-guarantee").next_sibling.find('span').text

            try:
                #status = browser.find_element_by_css_selector(web_class[2]).text
                status = soup.find("div", class_="fulfillment-add-to-cart-button").find('button').text
            except:
                status = "OUT OF STOCK"
            print("********" + title + "********")
            print(price)
            print(status)
        
        if "newegg" in link:
            web_class = (
                "product-title", #title
                "li.price-current", #price
                "button.btn.btn-primary.btn-wide" #status
            )
            title = browser.find_element_by_class_name(web_class[0]).text
            price = browser.find_element_by_css_selector(web_class[1]).text
            try:
                status = browser.find_element_by_css_selector(web_class[2]).text
                
            except:
                status = "OUT OF STOCK"

            html = browser.page_source
            soup = BeautifulSoup(html, 'html.parser')
            brand_search = soup.find_all("tr")
            for i in brand_search:
                if "Brand" in i.text:
                    brand = i.text.strip("Brand ")

                if "Model" in i.text:
                    model = i.text.strip("Model ")
            
                    
                

            print("********" + title + "********")
            print("Price: " + price)
            print("Availability: " + status)
            print("Brand: " + brand)
            print("Model: " + model)
browser.quit()