from datetime import datetime, date
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from spica.utils import month_mapping # type: ignore -- date to day of month mapping
from .forms import TransactionForm
from .models import Transaction

import calendar

def day_detail(request, year, month, day):

    # Variables
    selected_date = date(int(year), int(month), int(day))
    weekday = calendar.day_name[selected_date.weekday()]
    transactions = Transaction.objects.filter(date=selected_date)

    # CRUD operations
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.date = selected_date
            transaction.save()

            #Re-fetch to include the new one
            transactions = Transaction.objects.filter(date=selected_date)
            form = TransactionForm() # Clear form after submission
    else:  
        form = TransactionForm()

    context = {
        "year": year,
        "month": month,
        "day": day,
        "weekday": weekday,
        "form": form,
        "transactions": transactions,
        "open_modal": True, # this indicates the modal is open, for rendering on refresh
    }

    if request.headers.get("HX-Request") == "true":
        html = render_to_string("chips/day_detail.html", context, request=request)
        return  HttpResponse(html)
    
    # Fallback for full page load (e.g., refresh)
    months_data = month_mapping(int(year))
    context["months_data"] = months_data
    return render(request, "chips/year.html", context)


def year_view(request):
    year = datetime.now().year
    months_data = month_mapping(year)

    return render(request, "chips/year.html", {
        "year": year,
        "months_data": months_data,
    })

