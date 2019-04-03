from django.db import models
from django.urls import reverse
# Create your models here.
class Category0(models.Model):
	title = models.CharField(max_length = 70)
	#文章标题，字符型数据，长度70
	body = models.TextField()
	#文章主体，用TextField来存储大文本
	def get_absolute_url(self):
		return reverse('web:post0',kwargs={'post_id':self.pk})#用于返回文章编码，导入了reverse函数

class Category1(models.Model):
	title = models.CharField(max_length = 70)
	#文章标题，字符型数据，长度70
	body = models.TextField()
	#文章主体，用TextField来存储大文本
	def get_absolute_url(self):
		return reverse('web:post1',kwargs={'post_id':self.pk})#用于返回文章编码，导入了reverse函数

class Category2(models.Model):
	title = models.CharField(max_length = 70)
	#文章标题，字符型数据，长度70
	body = models.TextField()
	#文章主体，用TextField来存储大文本
	def get_absolute_url(self):
		return reverse('web:post2',kwargs={'post_id':self.pk})#用于返回文章编码，导入了reverse函数

class Category3(models.Model):
	title = models.CharField(max_length = 70)
	#文章标题，字符型数据，长度70
	body = models.TextField()
	#文章主体，用TextField来存储大文本
	def get_absolute_url(self):
		return reverse('web:post3',kwargs={'post_id':self.pk})#用于返回文章编码，导入了reverse函数
		



