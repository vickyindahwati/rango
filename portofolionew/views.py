from django.shortcuts import render
from portofolionew.models import portofolio
# Create your views here.

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    portofolio_list = portofolio.objects.order_by('name')
    context_dict = {'portofolios': portofolio_list}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'portofolionew/index.html', context_dict)

