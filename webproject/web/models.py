from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length = 100)
	#分类，字符型数据，长度100

class Post(models.Model):
	title = models.CharField(max_length = 70)
	#文章标题，字符型数据，长度70
	body = models.TextField()
	#文章主体，用TextField来存储大文本
	category = models.ForeignKey(Category,on_delete = models.CASCADE)
	#关联分类，一对多关系