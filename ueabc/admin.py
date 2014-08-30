from django.contrib import admin
from ueabc.models import *

class CommitteeAdmin(admin.ModelAdmin):
	list_display = ('position', 'firstname', 'surname')
	ordering = ('id',)

class MemberAdmin(admin.ModelAdmin):
	list_display = ('username', 'usertype')
	search_fields = ('username', 'usertype')

class NewsAdmin(admin.ModelAdmin):
	list_display = ('date', 'title')
	search_fields = ('date', 'title')
	list_filter = ('date',)
	ordering = ('-date',)

class PhotosAdmin(admin.ModelAdmin):
	list_display = ('type_of_photo', 'datetaken', 'url')
	search_fields = ('type_of_photo', 'datetaken')
	list_filter = ('type_of_photo', 'datetaken')
	ordering = ('-datetaken',)

class RacesAdmin(admin.ModelAdmin):
	list_display = ('race_id', 'race_name')
	search_fields = ('race_name',)

class ResultsAdmin(admin.ModelAdmin):
	list_display = ('year', 'race', 'category', 'position')
	search_fields = ('year', 'race')
	list_filter = ('year', 'race')
	ordering = ('-year','-race')

class VideosAdmin(admin.ModelAdmin):
	list_display = ('dateadded', 'name', 'url')
	search_fields = ('dateadded', 'name')
	list_filter =('dateadded',)
	ordering = ('-dateadded',)

class YearTableAdmin(admin.ModelAdmin):
	list_display = ('year_id', 'year_value')
	search_fields = ('year_id', 'year_value')


admin.site.register(Committee, CommitteeAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Photos, PhotosAdmin)
admin.site.register(Races, RacesAdmin)
admin.site.register(Results, ResultsAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(YearTable, YearTableAdmin)