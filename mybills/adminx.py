import xadmin
from mybills.models import *


@xadmin.sites.register(BasData)
class BasDataAdmin(object):
    list_display = ("id", 'code', "name", "type", "sort", "desc", "type_desc")
    search_fields = ("code", "type", "name")
    list_per_page = 20
    fields = ('code', "name", "type", "sort", "desc", "type_desc")
    ordering = ("type", "sort")


@xadmin.sites.register(BusDebt)
class BusDebtAdmin(object):
    list_display = ("id", 'name', "value", "status", "refund_date")

    # **筛选器
    search_fields = ("name",)  # **搜索字段
    # date_hierarchy = "refund_date"    # **时间分层筛选（无效）
    list_filter = ("status", "refund_date")  # **过滤器

    list_per_page = 20
    fields = ('name', "value", "status", "refund_date")
    ordering = ("-id",)


@xadmin.sites.register(BusDebtRefund)
class BusDebtRefundAdmin(object):
    list_display = ("id", 'name', "value", "debt", "refund_date")

    # **筛选器
    search_fields = ("name",)  # **搜索字段
    list_filter = ("debt", "refund_date")  # **过滤器

    list_per_page = 20
    fields = ('name', "value", "debt", "refund_date")
    ordering = ("-refund_date",)


@xadmin.sites.register(BusExpenseDetails)
class BusExpenseDetailsAdmin(object):
    list_display = ('name', "type", "value", "expense_date")

    # **筛选器
    search_fields = ("name",)  # **搜索字段
    list_filter = ("type", "expense_date")  # **过滤器

    list_per_page = 100
    fields = ('name', "type", "value", "expense_date", "desc")
    ordering = ("-expense_date",)
