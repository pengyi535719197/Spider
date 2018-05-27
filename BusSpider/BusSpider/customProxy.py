import random

from BusSpider.resource import PROXIES

class RandomProxy(object):
    def proccess_request(self, request, spider):
        proxy = random.choice(PROXIES)
        request.meta['proxy'] = 'http://%s' %proxy
