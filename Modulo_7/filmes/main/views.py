from django.shortcuts import render
from .models import ProjetoFilmes
from .forms import UserForm
# Create your views here.

def homepage(request):
    return render(
                    request=request,
                    template_name="home.html",
                    context={"cursos": ProjetoFilmes.objects.all}
                )