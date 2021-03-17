from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.headless = True
browser = Chrome(options=opts)
link = []
with open('C:/Users/pluhm/Documents/graphics_links.txt', 'r') as f:
    for line in f:
        link = line.strip()
        browser.get(link)

        if "bestbuy" in link: #bestbuy coding needs worked on to get the desired result
            web_class = (
                'sku-title', #title
                'priceView-customer-price', #price
                'fulfillment-add-to-cart-button' #status
            )
        
        if "newegg" in link:
            web_class = (
                'product-title', #title
                'product-price', #price
                'product-buy' #status
            )
        
        title = browser.find_element_by_class_name(web_class[0]).text
        price = browser.find_element_by_class_name(web_class[1]).text
        status = browser.find_element_by_class_name(web_class[2]).text
        
        print("********" + title + "********")
        print(price)
        if status == '':
            print("OUT OF STOCK")
        else:
            print(status)

browser.quit()