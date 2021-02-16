

# creating scrapy project named sainsburys
scrapy startproject sainsburys

#  generate new spider
cd sainsburys
scrapy genspider spidername starturl.com

# example
scrapy genspider basic 'https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish'


# scrapy shell
# start scrapy shell
scrapy shell 
# fetch url using shell
>>> fetch('https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish/')
# or pass url directly
scrapy shell 'https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish/'

# extract urls from response 
# Using xpath selector
urls = response.xpath('//ul[@class="categories departments"]/li/a/@href').extract()
# Or Using CSS selectors
urls = response.css('ul.categories.departments > li > a::attr(href)').extract()

# run spider
scrapy crawl basic



# built-in feed exporters:
# • csv: saves information as CSV
# • json: saves information as JSON
# • jsonlines: saves information as JSON-lines
# • xml: saves information as XML
# • pickle: saves information as Pickle data
# • marshal: saves information in Marshal format, which is similar to Pickle (specific to Python) but doesn’t have any machine architectural issues

# run spider exporting to csv file
scrapy crawl basic -o sainsburys.csv

# run spider exporting to JSON file
scrapy crawl basic -o sainsburys.json

# run spider exporting to JSON-lines files are written to the disk as soon as they’re processed by the item pipelines!
scrapy crawl basic -o sainsburys.jl

# run spider while providing setting option
scrapy crawl basic -s MONGO_URI=localhost:27017
scrapy crawl basic -s SQLITE_LOCATION=sainsburys.db

# run spider exporting to csv filde using custom exporter mycsv
scrapy crawl basic -o mycsv.csv -t mycsv