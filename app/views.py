from django.shortcuts import render_to_response, RequestContext
from harak.app.models import New, WatchNew, Statement, Album
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse

def test(request):
	return HttpResponse('hey you')

def home(request):
	entries = list(New.objects.all()[:3])
	if not entries:
		raise Http404
	
	watch_entries = list(WatchNew.objects.all()[:4])
	if not watch_entries:
		raise Http404
	
	return render_to_response("index.html", locals())
	
def vid(request):
	vi = 'http://www.flickr.com/photos/riklaunim/4859954938/'
	return render_to_response('test.html', locals())
	
def show_news(request):
	news_entry = New.objects.all()
	return render_to_response("news.html", locals())

def show_new(request, num):
	entry = get_object_or_404(New, id=num )
	return render_to_response('new.html', locals())
	
def show_watchnews(request):
	news_entry = WatchNew.objects.all()[:3]
	return render_to_response("watchnews.html", locals())
	
def show_watchnew(request, num):
	entry = get_object_or_404(WatchNew, id=num )
	return render_to_response('watchnew.html', locals())

def state(request):
	entries = list(Statement.objects.all())
	if not entries:
		raise Http404
	return render_to_response('data.html', locals())
	
def show_state(request, num):
	entry = get_object_or_404(Statement, id=num )
	return render_to_response('show_data.html', locals())

def show_img(request):
	return render_to_response("test.html", locals())

def show_album(request):
	entries = list(Album.objects.all())
	if not entries:
		raise Http404
		
	return render_to_response("photo.html", locals())

	
import re

from django.db.models import Q

def normalize_query(query_string,
					findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
					normspace=re.compile(r'\s{2,}').sub):
	''' Splits the query string in invidual keywords, getting rid of unecessary spaces
		and grouping quoted words together.
		Example:

		>>> normalize_query('  some random  words "with   quotes  " and   spaces')
		['some', 'random', 'words', 'with quotes', 'and', 'spaces']

	'''
	return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
	''' Returns a query, that is a combination of Q objects. That combination
		aims to search keywords within a model by testing the given search fields.

	'''
	query = None # Query to search for every search term
	terms = normalize_query(query_string)
	for term in terms:
		or_query = None # Query to search for a given term in each field
		for field_name in search_fields:
			q = Q(**{"%s__icontains" % field_name: term})
			if or_query is None:
				or_query = q
			else:
				or_query = or_query | q
		if query is None:
			query = or_query
		else:
			query = query & or_query
	return query


def search(request):
	
	
	articles = WatchNew.objects.all()

	query_string = ''
	found_entries = None
	
	# if category is checked
	if ('cat' in request.GET):
		
		if (request.GET['cat'] == 'news'):
			if ('s' in request.GET) and request.GET['s'].strip():
				articles = New.objects.all()
				
				query_string = request.GET['s']

				entry_query = get_query(query_string, ['title', 'html_body',])

				found_entries = New.objects.filter(entry_query).order_by('-published')
		else:
			if ('s' in request.GET) and request.GET['s'].strip():
				articles = WatchNew.objects.all()
				
				query_string = request.GET['s']

				entry_query = get_query(query_string, ['title', 'html_body',])

				found_entries = WatchNew.objects.filter(entry_query).order_by('-published')
	
	# category is not checked
	else:
			if ('s' in request.GET) and request.GET['s'].strip():
				articles = New.objects.all()
				
				query_string = request.GET['s']

				entry_query = get_query(query_string, ['title', 'html_body',])

				found_entries = New.objects.filter(entry_query).order_by('-published')	

	return render_to_response('search.html',
			{ 'query_string': query_string, 'found_entries': found_entries, 'articles':articles },
		context_instance=RequestContext(request))

