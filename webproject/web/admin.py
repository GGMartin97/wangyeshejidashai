from django.contrib import admin
from .models import Category0,Category1,Category2,Category3
#加入创建的模型使的admin知道他们的存在
# Register your models here.

admin.site.register(Category0)
admin.site.register(Category1)
admin.site.register(Category2)
admin.site.register(Category3)