from django.views.generic import ListView, DetailView
from .models import Proyect


# Create your views here.
class PortfolioPageView(ListView):
    model = Proyect
    template_name = "proyect.html"


class PortfolioDetailedView(DetailView):
    model = Proyect
    template_name = "proyect_detail.html"
