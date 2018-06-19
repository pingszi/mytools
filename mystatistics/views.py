from xadmin.views.base import CommAdminView, TemplateResponse


class VersionInfoAdminView(CommAdminView):
    def get_breadcrumb(self):
        """获取头部面包屑导航"""
        breadcrumb = CommAdminView.get_breadcrumb(self)
        breadcrumb.append({'title': '版本信息', 'url': '/mystatistics/version/index'})
        return breadcrumb

    def get(self, request, *args, **kwargs):
        """
        @desc ： 版本信息
        @author  pings
        @date    2018/06/13
        @return  TemplateResponse
        """
        return TemplateResponse(request, 'version_info_index.html', self.get_context())


class BusExpenseDetailsAdminView(CommAdminView):
    def get_breadcrumb(self):
        """获取头部面包屑导航"""
        breadcrumb = CommAdminView.get_breadcrumb(self)
        breadcrumb.append({'title': '消费统计', 'url': '/mystatistics/busexpensedetails/index'})
        return breadcrumb

    def get(self, request, *args, **kwargs):
        """
        @desc ： 消费统计
        @author  pings
        @date    2018/06/13
        @return  TemplateResponse
        """
        return TemplateResponse(request, 'expense_details_index.html', self.get_context())
