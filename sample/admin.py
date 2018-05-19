# -*- coding: utf-8 -*-
from django.contrib import admin
import models
# Register your models here.

class InlineImage(admin.TabularInline):
  model = models.Image
  extra=0
class Sampleadmin(admin.ModelAdmin):
  inlines = [InlineImage]
  list_display=('id','name','serialnumber','customer','input_date','product_state')
  search_fields=('name',)
  list_filter=('customer','product_state','input_date',)
  list_per_page=5
  list_editable=('product_state',)
  list_select_related=('customer',)
  filter_horizontal=('department',)
  raw_id_fields=('customer',)
  #readonly_fields = ('image_data',)
  actions=['set_status_sealed','set_status_sealing','set_status_wait_sealing','checkout',]

  def set_status_checkout(modeladmin,request,queryset):
    selected=request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    models.Sample.objects.filter(id__in=selected).update(product_state='checkout')
  def set_status_sealed(modeladmin,request,queryset):
    selected=request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    models.Sample.objects.filter(id__in=selected).update(product_state='sealed')
  def set_status_wait_sealing(modeladmin,request,queryset):
    selected=request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    models.Sample.objects.filter(id__in=selected).update(product_state='wait_sealing')
#  def set_status_wait_sealing(modeladmin,request,queryset):
#    selected=request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
#    models.Book.objects.filter(id__in=selected).delete()
#  def image_data(self, obj):
#        return mark_safe(u'< img src="%s" width="100px" />' % obj.image.url)
#  image_data.short_description = u'品牌图片'
  set_status_checkout.short_description="设置所有的样品为--已借出"
  set_status_sealed.short_description="设置所有的样品为--已销毁"
#  set_status_sealing.short_description="设置所有的样品为--待销毁"
  set_status_wait_sealing.short_description="设置所有的样品为--待销毁"
  
class Departmentadmin(admin.ModelAdmin):
  list_display=('name','contact','contact_email')
class Customeradmin(admin.ModelAdmin):
  list_display = ('name','address','country',)

admin.site.register(models.Department,Departmentadmin)
admin.site.register(models.Customer,Customeradmin)
admin.site.register(models.Sample,Sampleadmin)

