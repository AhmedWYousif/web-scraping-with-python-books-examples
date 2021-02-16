

# from string html
from scrapy.selector import Selector

selector = Selector(text='<html><body><h1>Hello Selectors!</h1></body></html>')
print(selector.xpath('//h1/text()').extract()) # ['Hello Selectors!']


# or from a response
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

response = HtmlResponse(url='http://my.domain.com',
body='<html><body><h1>Hello Selectors!</h1></body></html>',
encoding='UTF-8')
print(Selector(response=response).css('h1::text').extract()) # ['Hello Selectors!']

# conveniently access them from your response using
response.xpath()
# or
response.css()