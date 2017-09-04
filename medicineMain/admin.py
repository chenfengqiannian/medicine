from django.contrib import admin
import models
# Register your models here.

class ImageInline(admin.StackedInline):
    model = models.UserImage


class CaseHistoryAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]

    list_display = (
    'name','tel','modDateTime','physicalCondition' )
    search_fields = ['name', 'tel']
class XcxUserAdmin(admin.ModelAdmin):
    list_filter = ('body',)
    list_display = (
    'phone','nickname')
    search_fields = ['nickname', 'phone','body']


admin.site.register(models.CaseHistory,CaseHistoryAdmin)
admin.site.register(models.XcxUser,XcxUserAdmin)
admin.site.register(models.ScrollImage)
admin.site.register(models.Message)
admin.site.register(models.Symptom)
admin.site.register(models.UserImage)
admin.site.register(models.IndexImage)


