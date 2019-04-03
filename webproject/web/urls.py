from django.urls import path
from .import views
app_name='web'

urlpatterns = [
	path('',views.index,name = 'index'),
	path('category0',views.category0,name='category0'),
	path('category1',views.category1,name='category1'),
	path('category2',views.category2,name='category2'),
	path('category3',views.category3,name='category3'),
	path('post0/<int:post_id>',views.post0,name='post0'),
	path('post1/<int:post_id>',views.post1,name='post1'),
	path('post2/<int:post_id>',views.post2,name='post2'),
	path('post3/<int:post_id>',views.post3,name='post3'),
]