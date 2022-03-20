# 分步按顺序运行
# from scrapy.crawler import CrawlerRunner
# from twisted.internet import reactor, defer
# from scrapy.utils.log import configure_logging
# from scrapy.utils.project import get_project_settings

# configure_logging()
# settings = get_project_settings()
# runner = CrawlerRunner(settings)

# @defer.inlineCallbacks
# def crawl():
#     yield runner.crawl(Spider1)
#     yield runner.crawl(Spider2)
#     reactor.stop()

# crawl()
# reactor.run()



# 同时运行
# from twisted.internet import reactor
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
# from scrapy.utils.project import get_project_settings

# configure_logging()
# settings = get_project_settings()
# runner = CrawlerRunner(settings)
# runner.crawl(Spider1)
# runner.crawl(Spider2)
# d = runner.join()
# d.addBoth(lambda _: reactor.stop())

# reactor.run()
