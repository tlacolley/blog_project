# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article, Category, Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('label',)

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'short_description', 'date_create', 'date_update', 'category')
	list_filter = ('category',)
	fieldsets = (
		('General',{
			'fields':(('title','slug'),
					('category', 'date_parution')
					),
		} ),
		('Content',{
			'fields':(('short_description',),
					('content',)
					),
		} ),
			)
	prepopulated_fields = {'slug' : ('title',)}

	search_fields = ('title', 'content')


class CommentAdmin(admin.ModelAdmin):
	pass

admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
