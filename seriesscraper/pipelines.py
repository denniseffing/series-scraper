# -*- coding: utf-8 -*-

from jdownloader.jd import Jd
from jdownloader.jdlink import JdLink
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from seriesscraper.config.config import Config
from seriesscraper.items import EpisodeItem


class JDownloaderPipeline(object):
    def __init__(self):
        self.__config: Config = Config.instance()
        self.__jd = Jd()

    def process_item(self, item, spider):
        assert isinstance(item, EpisodeItem)

        tv_show_name = item['tv_show_name']
        release_title, download_link = item['release_downloadlink_tuples'][0]

        jd_link = JdLink(
            autostart=self.__config.get_jd_autostart_downloads(),
            links=download_link,
            packageName='{}'.format(release_title),
            destinationFolder='{}/{}'.format(
                self.__config.get_jd_tv_show_dir(),
                tv_show_name
            ),
            extractPassword='serienjunkies.org'
        )

        self.__jd.add_link(jd_link)
