from django.shortcuts import render
from dailylog.models import Log, Question, Answer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView, View
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
# Create your views here.


def log(request):
    return render(request, 'log/create_log.html', {'questions': Question.objects.all()})

def save_log(request):
    log = Log.objects.create(user_id = request.user.id)
    for key, value in request.POST.dict().items():
        if key == 'csrfmiddlewaretoken':
            continue
        # Create Answer
        answer = Answer.objects.create(log_id = log.id, question_id = int(key[:len(key)-1]), text = value)

    return HttpResponseRedirect('/log/' + str(log.id))

class LogDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = 'log/detail.html'

    model = Log

class Home(TemplateView):
    template_name = "home.html"

class LogListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = 'log/list.html'

    def get_queryset(self):
        return Log.objects.filter(user = self.request.user)


class QuestionCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = "question/create.html"
    model = Question
    fields = ['text', 'question_type', 'default']
    success_url = '/create/question'

class SignUp(CreateView):
    model = User
    fields = ['username', 'password']
    template_name = 'auth/signup.html'
    success_url = 'login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(form.cleaned_data['password'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
