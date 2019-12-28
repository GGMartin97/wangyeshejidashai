from django.shortcuts import render,get_object_or_404
from .models import Category0,Category1,Category2,Category3
import markdown
# Create your views here.

def index(request):
	return render(request,'web/index.html')


def category0(request):
	category_list=Category0.objects.all()
	return render(request,'web/category.html',{'category_list':category_list})

def category1(request):
	category_list=Category1.objects.all()
	return render(request,'web/category.html',{'category_list':category_list})

def category2(request):
	category_list=Category2.objects.all()
	return render(request,'web/category.html',{'category_list':category_list})

def category3(request):
	category_list=Category3.objects.all()
	return render(request,'web/category.html',{'category_list':category_list})

def post0(request,post_id):
	post = get_object_or_404(Category0,pk=post_id)
	post.body = markdown.markdown(post.body,extensions=[
												'markdown.extensions.extra',
												'markdown.extensions.codehilite',
												'markdown.extensions.toc',
												])
	return render(request,'web/post.html',{'post':post})

def post1(request,post_id):
	post = get_object_or_404(Category1,pk=post_id)
	post.body = markdown.markdown(post.body,extensions=[
												'markdown.extensions.extra',
												'markdown.extensions.codehilite',
												'markdown.extensions.toc',
												])
	return render(request,'web/post.html',{'post':post})

def post2(request,post_id):
	post = get_object_or_404(Category2,pk=post_id)
	post.body = markdown.markdown(post.body,extensions=[
												'markdown.extensions.extra',
												'markdown.extensions.codehilite',
												'markdown.extensions.toc',
												])
	return render(request,'web/post.html',{'post':post})


def post3(request,post_id):
	post = get_object_or_404(Category3,pk=post_id)
	post.body = markdown.markdown(post.body,extensions=[
												'markdown.extensions.extra',
												'markdown.extensions.codehilite',
												'markdown.extensions.toc',
												])
	return render(request,'web/post.html',{'post':post})



