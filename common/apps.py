import logging

from django.apps import AppConfig


class CommonConfig(AppConfig):
    name = 'common'

    # **app名称
    verbose_name = "基础功能"

logger = logging.getLogger("common")
