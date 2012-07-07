from django.views.generic.base import TemplateView
from misquote.models import Author
from misquote.models import Quote

# extend TemplateView and override template_name with index.html
class MasterView(TemplateView):
	template_name = "index.html"
	
	# update context dictionary with Author value and Quote value
	def get_context_data(self, **kwargs):
		context = super(MasterView, self).get_context_data(**kwargs)
		context["Author"] = Author.objects.all().order_by('?')[0]
		context["Quote"] = Quote.objects.all().order_by('?')[0]
		return context