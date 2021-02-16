# -*- coding: utf-8 -*-



# You can use the following list as a reference to the log-level priority:
# 1. CRITICAL
# 2. ERROR
# 3. WARNING
# 4. INFO
# 5. DEBUG

LOG_LEVEL = 'INFO'


# limit the number of concurrent requests to one website.
CONCURRENT_REQUESTS = 1


# seconds should wait between downloading another page from the same domain or IP
# non-200-OK responses do not decrease the download delay.
DOWNLOAD_DELAY = 0.125 # 125 milliseconds


# What is behind this setting does is adjust the download delay based on the response times of the server
AUTOTHROTTLE_ENABLED = True
# wait 15 seconds initially between two requests. Based on the server’s response time
AUTOTHROTTLE_START_DELAY = 15
# This setting tells Scrapy to wait at most 25 seconds until the next request.
AUTOTHROTTLE_MAX_DELAY = 25
# enable debugging for auto-throttling.
AUTOTHROTTLE_DEBUG = True


# disable using cookies
COOKIES_ENABLED = False
# disable using cookies
# enable debugging for 
COOKIES_DEBUG = True


