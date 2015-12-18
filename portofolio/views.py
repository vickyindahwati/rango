from django.shortcuts import render
from portofolio.models import exercise
# Create your views here.
def index(request):
    exercise_list = exercise.objects.order_by('name')
    context_dict = {'exercises': exercise_list}
    return render (request, 'portofolio/index.html', context_dict)


