import xadmin
from xadmin import views
from .views import *


class BaseSetting(object):
    """基本管理器配置"""

    # **开启主题功能
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
    """全局配置"""

    # **设置base_site.html的Title
    site_title = 'Pings的账单系统'
    # **设置base_site.html的Footer
    site_footer = 'Pings'

    # **菜单折叠
    # menu_style = "accordion"

    def get_site_menu(self):
        return [{
            'title': '我的统计',
            # 'icon': 'fa fa-users',
            'menus': (
                {'title': '消费统计', 'url': "/mystatistics/busexpensedetails/index"},
                {'title': '版本信息', 'url': "/mystatistics/version/index"},
            )
        }]

xadmin.site.register(views.CommAdminView, GlobalSetting)


# **===================我的统计===================
# **消费统计
xadmin.site.register_view('mystatistics/busexpensedetails/index', BusExpenseDetailsAdminView, name='index')
# **版本信息
xadmin.site.register_view('mystatistics/version/index', VersionInfoAdminView, name='index')
# **===================我的统计===================
