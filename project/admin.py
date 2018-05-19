# -*- coding: utf-8 -*-
from django.contrib import admin
import models
# Register your models here.

class InlineImage(admin.TabularInline):
  model = models.Image
class InlineDocument(admin.StackedInline):
  model = models.Document
  extra = 0
class Projectadmin(admin.ModelAdmin):
  inlines = [InlineDocument]
  list_display=('id','name','customer','create_date','project_state')
  search_fields=('name',)
  list_filter=('customer','project_state','create_date',)
  list_per_page=5
  list_editable=('project_state',)
  list_select_related=('customer',)
  #filter_horizontal=('department',)
  raw_id_fields=('customer',)
  #readonly_fields = ('image_data',)
  actions=['set_status_onging','set_status_finished','set_status_quoting','set_status_sustaining',]

  def set_status_ongoing(modeladmin,request,queryset):
    selected=request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    models.Book.objects.filter(id__in=selected).update(publisher_state='ongoing')
  def set_status_finished(modeladmin,request,queryset):
    selected=request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    models.Book.objects.filter(id__in=selected).update(publisher_state='finished')
  def set_status_quoting(modeladmin,request,queryset):
    selected=request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    models.Book.objects.filter(id__in=selected).update(publisher_state='quoting')
  def set_status_sustaining(modeladmin,request,queryset):
    selected=request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    models.Book.objects.filter(id__in=selected).update(publisher_state='sustainning')
#  def set_status_wait_sealing(modeladmin,request,queryset):
#    selected=request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
#    models.Book.objects.filter(id__in=selected).delete()
#  def image_data(self, obj):
#        return mark_safe(u'< img src="%s" width="100px" />' % obj.image.url)
#  image_data.short_description = u'品牌图片'
  set_status_ongoing.short_description="设置所有的样品为--进行中"
  set_status_finished.short_description="设置所有的样品为--已完成"
  set_status_sustaining.short_description="设置所有的样品为--维护中"
  set_status_quoting.short_description="设置所有的样品为--报价中"
  
class Departmentadmin(admin.ModelAdmin):
  list_display=('name','contact','contact_email')
class Customeradmin(admin.ModelAdmin):
  list_display = ('name','address','country',)

admin.site.register(models.Department,Departmentadmin)
admin.site.register(models.Customer,Customeradmin)
admin.site.register(models.Project,Projectadmin)

