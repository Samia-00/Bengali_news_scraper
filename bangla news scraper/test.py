import chromedriver_autoinstaller

from scraping.helpers import scraper_driver
from scraping.samakal import DcraScraper
chrome_version = chromedriver_autoinstaller.get_chrome_version()
driver_dcra = scraper_driver('https://samakal.com/', chrome_version=chrome_version, headless=False)
scraper = DcraScraper(driver_dcra)
categories = {'technology':'technology'}
scraper.scrape_site(categories, 'technology')
driver_dcra.quit()