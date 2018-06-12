from django.db import models


class BasData(models.Model):
    """
    @desc ：基础数据
    @author Pings
    @date   2018/04/09
    @Version  V1.0

    v1.1 增加名称字段 Pings 2018-04-13
    """

    class Meta:
        # **表名
        db_table = "bill_bas_data"
        # **菜单名
        verbose_name = "基础数据"
        verbose_name_plural = "基础数据"

    id = models.AutoField(primary_key=True, verbose_name="编号")
    code = models.CharField(max_length=20, unique=True, verbose_name="编码")
    name = models.CharField(max_length=100, verbose_name="名称")
    type = models.CharField(max_length=20, verbose_name="类型")
    type_desc = models.CharField(max_length=100, null=True, blank=True, verbose_name="类型描述")
    sort = models.IntegerField(null=True, blank=True, verbose_name="排序")
    desc = models.CharField(null=True, blank=True, max_length=255, verbose_name="描述")

    add_who = models.IntegerField(verbose_name="添加人", null=True, blank=True)
    add_date = models.DateField(verbose_name="添加日期", auto_now_add=True)
    edit_who = models.IntegerField(verbose_name="编辑人", blank=True, null=True)
    edit_date = models.DateField(verbose_name="编辑日期", auto_now=True)

    def __str__(self):
        return self.name


class BusDebt(models.Model):
    """
    @desc ：欠款
    @author Pings
    @date   2018/04/09
    @Version  V1.0
    """

    class Meta:
        # **表名
        db_table = "bill_bus_debt"
        # **菜单名
        verbose_name = "欠款单"
        verbose_name_plural = "欠款单"

    id = models.AutoField(primary_key=True, verbose_name="编号")
    name = models.CharField(max_length=40, verbose_name="名称")
    value = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="总额")
    status = models.ForeignKey(BasData, on_delete=models.CASCADE, limit_choices_to={"type": "DEBT_STATUS"},
                               verbose_name="状态")
    refund_date = models.DateField(null=True, blank=True, verbose_name="偿还日期")

    add_who = models.IntegerField(verbose_name="添加人", null=True, blank=True)
    add_date = models.DateField(verbose_name="添加日期", auto_now_add=True)
    edit_who = models.IntegerField(verbose_name="编辑人", blank=True, null=True)
    edit_date = models.DateField(verbose_name="编辑日期", auto_now=True)

    def __str__(self):
        return self.name


class BusDebtRefund(models.Model):
    """
    @desc ：还款
    @author Pings
    @date   2018/04/09
    @Version  V1.0
    """

    class Meta:
        # **表名
        db_table = "bill_bus_debt_refund"
        # **菜单名
        verbose_name = "还款单"
        verbose_name_plural = "还款单"

    id = models.AutoField(primary_key=True, verbose_name="编号")
    name = models.CharField(max_length=40, verbose_name="名称")
    value = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="金额")
    refund_date = models.DateField(verbose_name="偿还日期")
    debt = models.ForeignKey(BusDebt, on_delete=models.CASCADE, verbose_name="欠款项")

    add_who = models.IntegerField(verbose_name="添加人", null=True, blank=True)
    add_date = models.DateField(verbose_name="添加日期", auto_now_add=True)
    edit_who = models.IntegerField(verbose_name="编辑人", blank=True, null=True)
    edit_date = models.DateField(verbose_name="编辑日期", auto_now=True)

    def __str__(self):
        return self.name


class BusExpenseDetails(models.Model):
    """
    @desc ： 消费
    @author Pings
    @date   2018/04/10
    @Version  V1.0
    """

    class Meta:
        # **表名
        db_table = "bill_bus_expense_details"
        # **菜单名
        verbose_name = "消费明细"
        verbose_name_plural = "消费明细"

    id = models.AutoField(primary_key=True, verbose_name="编号")
    name = models.CharField(max_length=40, verbose_name="名称")
    type = models.ForeignKey(BasData, on_delete=models.CASCADE, limit_choices_to={"type": "EXPENSE"},
                             verbose_name="消费类型")
    value = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="金额")
    expense_date = models.DateField(verbose_name="消费日期")
    desc = models.CharField(null=True, blank=True, max_length=255, verbose_name="描述")

    add_who = models.IntegerField(verbose_name="添加人", null=True, blank=True)
    add_date = models.DateField(verbose_name="添加日期", auto_now_add=True)
    edit_who = models.IntegerField(verbose_name="编辑人", blank=True, null=True)
    edit_date = models.DateField(verbose_name="编辑日期", auto_now=True)

    def __str__(self):
        return self.name

