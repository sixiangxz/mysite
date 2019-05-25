from django.contrib import admin
from . import models
import datetime
from django.contrib.contenttypes.models import ContentType
# Register your models here.

# def upper_case_name(obj):
#     return ("%s" % (obj.headline)).upper()
# upper_case_name.short_description = 'Name'
# 自定义过滤器
class PubDateFilter(admin.SimpleListFilter):

    title = "日期过滤"

    parameter_name = 'date'

    def lookups(self, request, model_admin):

        return (

            ('today', '今天的文章'),
            ('before', '以前的文章'),
        )

    def queryset(self, request, queryset):

        if self.value() == 'today':
            return queryset.filter(pub_date__day=datetime.date.today().day)
        if self.value() == 'before':
            return queryset.filter(pub_date__day__lt=datetime.date.today().day)
# 顶部提示修改信息
def check_entries(modeladmin, request, queryset):

    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    print(type(selected))
    print(selected)
    # 获取对应的模型
    ct = ContentType.objects.get_for_model(queryset.model)
    print(ct)
    row_updates = queryset.update(checked=True)
    message_number = '本次操作审阅了%s条文章'% row_updates
    modeladmin.message_user(request, message_number)



check_entries.short_description = "文章审阅通过"

class EntryAdmin(admin.ModelAdmin):

    # 底部增加编辑栏
    actions_on_bottom = True
    # 顶部增加日期过滤
    date_hierarchy = 'pub_date'
    # filter_vertical = ['authors']
    # 显示的列数
    list_display = ('headline', 'color_headline','body_text', 'pub_date','blog',)
    # list_display = (upper_case_name,)
    # 再增加链接选项
    list_display_links = ['headline', 'pub_date']
    # 当前页面修改body_text
    # 设置过滤栏
    list_filter = ('pub_date', 'blog__name', 'checked', PubDateFilter)
    # 每页显示个数
    # list_per_page = 1
    # 排序方式
    ordering = ['pub_date']
    # 外键
    radio_fields = {"blog": admin.VERTICAL}
    # 多对多
    raw_id_fields = ("authors",)
    # 只读不可修改(不显示)
    # readonly_fields = ['body_text']
    # 搜索栏
    search_fields = ['headline', 'body_text']
    # 增加执行动作
    actions = [check_entries]


    # list_editable = ['body_text']
    # fields = (('blog', 'headline'), 'body_text', 'pub_date', 'mod_date')
    # fieldsets = (
    #     ('普通栏', {
    #       'fields': ('blog', 'headline'),
    #     }),
    #     ('时间栏', {
    #         'classes': ('collapse',),
    #         'fields': ('pub_date', 'mod_date')
    #     }),
    # )
    # 顶部提示修改信息
    # def check_entries(self, request, queryset):
    #     row_updates = queryset.update(checked=True)
    #     message_number = '本次操作审阅了%s条文章' % row_updates
    #     self.message_user(request, message_number)

    check_entries.short_description = "文章审阅通过"

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Author)
admin.site.register(models.Blog)

