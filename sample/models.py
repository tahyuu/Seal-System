# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
#先设计部门Department对象(表)[models.py]
class Department(models.Model): #继承于models.Model这个父类,从而实现多态
  name=models.CharField(max_length=32) #名字的字段,使用字符串格式,最大长度32
  contact=models.CharField(max_length=32)
  contact_email=models.EmailField()         #email字段,使用email自带的格式
  def __unicode__(self):           #定义unicode函数,是为了让对象在实例化的时候,可以返回打印输出它的名字<阿文>.不至于显示为<** object>
    return "%s"%(self.name)

#客户
class Customer(models.Model):
  name=models.CharField(max_length=64,unique=True) #客户名称,唯一,是主键
  address=models.CharField(max_length=64,unique=True)
  city=models.CharField(max_length=32)
  state_province=models.CharField(max_length=32)
  country=models.CharField(max_length=32)
  website=models.URLField()            #主页,采用自带的url格式
  def __unicode__(self):
    return "%s"%(self.name)



#定义一个选项,里面包含3个可选框,用以下面的书籍表current_state下拉选择
STATUS_CHOICES=(
  ('sealed',u'已销毁'),
#  ('sealing',u'[出库]销毁中'),
  ('wait_sealing',u'待销毁'),
  ('checkout',u'被借出'),
)

#样品表
class Sample(models.Model):
  name=models.CharField(max_length=64)  
  serialnumber=models.CharField(max_length=64,unique=True)  
  department=models.ManyToManyField(Department) #部门,多对多的关系
  customer=models.ForeignKey(Customer) #客户,外键管理到Customer表
  input_date=models.DateField(auto_now_add=True)
#  image_data = models.ImageField(upload_to='photos/%Y/%m/%d')
#  image = models.ImageField(upload_to='images')
#  def image_data(self, obj):
#        return mark_safe(u'< img src="%s" width="100px" />' % obj.image.url)
#  image_data.short_description = u'品牌图片'
  product_state=models.CharField(max_length=20,choices=STATUS_CHOICES,default='wait_sealing') #Status,是一个可选框
  def __unicode__(self):
    return "%s--%s"%(self.name,self.input_date)

class Image(models.Model):
  sample = models.ForeignKey(Sample)
  image = models.ImageField(upload_to='images')

  
