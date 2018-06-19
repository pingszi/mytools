import logging

from django.apps import AppConfig


class MybillsConfig(AppConfig):
    name = 'mybills'

    # **显示的app名称
    verbose_name = "我的账单"

logger = logging.getLogger("mybills")
