import random
from BusSpider.resource import USER_AGENT_LIST
# from scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware import UserAgentMiddlear

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers.setdefault('User-Agent', ua)