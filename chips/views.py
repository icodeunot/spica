from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from spica.utils import month_mapping # type: ignore -- date to day of month mapping

import calendar

def day_detail(request, year, month, day):
    # Get a weekday name from yyyy/mm/dd
    weekday = calendar.day_name[datetime(int(year), int(month), int(day)).weekday()]

    context = {
        "year": year,
        "month": month,
        "day": day,
        "weekday": weekday,
        "open_modal": True, # this indicates the modal is open, for rendering on refresh
    }

    if request.headers.get("HX-Request") == "true":
        html = render_to_string("chips/day_detail.html", context)
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

