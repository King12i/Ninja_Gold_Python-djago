from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
import random

# Create your views here.

def index(request):
    if "gold" not in request.session:
        request.session['output'] = []
        request.session['gold'] = 0
        gold = 0
    else:
        gold = request.session['gold']
    context={
        "gold": gold,
    }
    return render(request, "index.html", context)

def process_money(request):
    time = strftime("%b %d %Y %H:%M %p", localtime())
    minus_flag = False
    if request.POST["location"] == "1":
        gold = random.randint(10, 20)
        output_text = (f"Earned {gold} gold from the Farm! ({time})")
    elif request.POST["location"] == "2":
        gold = random.randint(5, 10)
        output_text = (f"Earned {gold} gold from the Cave! ({time})")
    elif request.POST["location"] == "3":
        gold = random.randint(2, 5)
        output_text = (f"Earned {gold} gold from the House! ({time})")
    elif request.POST["location"] == "4":
        gold = random.randint(-50, 50)
        if gold > 0:
            output_text = (f"Entered a casino and won {gold} gold! YAY!! ({time})")
        else:
            output_text = (f"Entered a casino and lost {gold} gold... Ouch.. ({time})")
            minus_flag = True
    request.session['gold'] += gold
    request.session['output'].append({"output_text": output_text, "minus_flag": minus_flag})
    request.session.save()
    return redirect("/")

def reset(request):
    request.session['output'] = []
    request.session['gold'] = 0
    return redirect("/")