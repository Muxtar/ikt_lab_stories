from random import choices
from django.shortcuts import render
from home.models import Contact, Stories
from home.forms import ContactForm
import sqlite3

def home(request, slug = None):
    stories = Stories.objects.all()

    if slug:
        stories = Stories.objects.filter(category_id__slug = slug)

    context = {
        'stories': stories
    }
    return render(request, 'index.html', context)

def contact(request):

    # with sqlite3.connect('db.sqlite3') as sql:
    #     cr = sql.cursor()
    #     cr.execute("select * from home_contact")
    #     data = cr.fetchall()
    #     print(data)

    print(Contact.objects.all())

    # form = ContactForm() 
    form = ContactForm()
    if request.method == 'POST':
        result = ContactForm(request.POST)
        if result.is_valid():
            result.save()
            # username = result.cleaned_data.get('username')
            # email = request.POST.get('email')
            # choices = request.POST.get("choices")
            # message = request.POST.get('message')
            # data = Contact(username = username, email=email, subjets = choices, message = message)
            # data.save()
        else:
            form = result


    context = {
        'forms':form,
        # 'forms':ContactForm()
    }
    return render(request, 'contact.html', context)

def stories(request):
    return render(request, 'stories.html')