# Create your views here.
from django.shortcuts import render_to_response
#from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.http import Http404
from django.template import RequestContext
from django.db.models import Avg,Min,Max,Count,F,Q
import datetime, time
from crime.models import Inmate, Inmatewatchlist, Offense
from django.conf import settings 

today_date = datetime.date.today()

today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)


def inmate( request ):
	inmates = Inmate.objects.order_by('-in_time')[:5]
        active_inmate_count = Inmate.objects.filter(active='Y').count()
        today_inmate_count = Inmate.objects.filter(in_time__range=(today_min, today_max)).count()
        today_inmate_released = Inmate.objects.filter(active='N',in_time__range=(today_min, today_max)).count()
        male_inmate_count = Inmate.objects.filter(sex='M', active='Y').count()
        female_inmate_count = Inmate.objects.filter(sex='F', active='Y').count()
        total_count = Inmate.objects.count()

        return render_to_response('index.html', {"total_count": total_count, "male_inmate_count": male_inmate_count, "female_inmate_count": female_inmate_count, "inmates": inmates, "active_inmate_count": active_inmate_count,"today_inmate_count": today_inmate_count, "today_inmate_released": today_inmate_released},context_instance = RequestContext(request))

def inmatelist( request ):
	inmates = Inmate.objects.order_by('-in_time')

        return render_to_response('inmatelist.html', {"inmates": inmates},context_instance = RequestContext(request))

def todayinmates( request ):
	inmates = Inmate.objects.filter(in_time__range=(today_min, today_max)).order_by('-in_time')

        return render_to_response('todayinmates.html', {"inmates": inmates},context_instance = RequestContext(request))

def activeinmates( request ):
	inmates = Inmate.objects.filter(active = 'Y').order_by('lastname')

        return render_to_response('activeinmates.html', {"inmates": inmates},context_instance = RequestContext(request))
