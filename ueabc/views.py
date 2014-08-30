from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.template import TemplateDoesNotExist
from django.db import connection
from django.http import Http404
from ueabc.models import *

def home(request):
	try:
		latest_news = News.objects.order_by('-date')[:3]
		return render(request, 'home.html', {'latest_news' :latest_news,'additional_css' : ['nivo-slider.css',], 'additional_js' : ['jquery.nivo.slider.pack.js','home.js',]})
	except TemplateDoesNotExist:
		raise Http404

def general_page(request, template_name):
	try:
		return render(request, template_name+'.html', {})
	except TemplateDoesNotExist:
		raise Http404

def news(request):
	try:
		news = News.objects.order_by('-date')
		return render(request, 'media/news.html',{'news': news})
	except TemplateDoesNotExist, ObjectDoesNotExist:
		raise Http404

def videos(request):
	try:
		videos = Videos.objects.order_by('-dateadded')
		return render(request, 'media/videos.html',{'videos': videos})
	except TemplateDoesNotExist, ObjectDoesNotExist:
		raise Http404

def photos(request, photos):
	try:
		photo_list = Photos.objects.filter(type_of_photo__contains=photos).order_by('-datetaken')
		return render(request, 'media/photos.html', {'photo_list':photo_list, 'photo_type':photos, 'additional_css' : ['lightbox.css',], 'additional_js' : ['lightbox.js',]})
	except TemplateDoesNotExist, ObjectDoesNotExist:
		raise Http404

def contacts(request):
	try:
		committee_list = Committee.objects.order_by('id')[:6]
		return render(request, 'contacts.html',{'committee_list': committee_list})
	except TemplateDoesNotExist, ObjectDoesNotExist:
		raise Http404


def results(request, year):
	try:
		# formats the year to from 2010-11 to 2010/ 11 for database
		database_year_format = year.replace('-', '/ ')
		# gets the year
		year_row = YearTable.objects.get(year_value=database_year_format)
		# gets all the results for the year
		results = Results.objects.select_related('year','race').filter(year=year_row.year_id)
		# makes sure there are some results for the year, if not then an error is generated
		if(len(results) == 0):
			raise Http404
		# gets all the races in results
		race_list = []
		for result in results:
			if(result.race.race_name not in race_list):
				race_list.append(Races.objects.get(race_id=result.race.race_id).race_name)

		return render(request, 'results.html', {'results':results, 'race_list':race_list,})
	except ObjectDoesNotExist:
		raise Http404
	
	