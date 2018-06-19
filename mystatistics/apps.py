import logging

from django.apps import AppConfig


class MystatisticsConfig(AppConfig):
    name = 'mystatistics'

    # **显示的app名称
    verbose_name = "我的统计"

logger = logging.getLogger("mystatistics")
