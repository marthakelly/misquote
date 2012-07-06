from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from misquote.models import Author
from misquote.models import Quote


def index(request):
	t = get_template('index.html')
	html = t.render(Context( {'Author' : Author.objects.all(), 'Quote' : Quote.objects.all() } ))
	return HttpResponse(html)