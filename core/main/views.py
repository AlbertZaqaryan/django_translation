from django.shortcuts import render
from .models import News
from django.views.generic import ListView
# Create your views here.

class NewsListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        news = News.objects.all()
        return render(request, self.template_name, {'news':news})