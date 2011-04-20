from django.views.generic import TemplateView, DetailView, ListView
from svarmeh.models import Product

class TitledDetailView(DetailView):
    def get_context_data(self, **kwargs):
        return dict(super(TitledDetailView, self).get_context_data(**kwargs),
            title=self.object)

class TitledListView(ListView):
    title = ''

    def get_context_data(self, **kwargs):
        return dict(super(TitledListView, self).get_context_data(**kwargs),
            title=self.title)

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return dict(super(HomeView, self).get_context_data(**kwargs), **{
            'projects': Product.objects.filter(status='published'),
        })



