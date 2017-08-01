from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView
from django.core.urlresolvers import resolve
from .models import URLTable
# Create your views here.

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('503.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response

def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response

def home_view(request):
    template_name = 'index.html'
    done = 'False'
    final = 'None'
    length = len(URLTable.objects.all())
    obj = URLTable.objects.all()[length-3:]
    context = {
        "done":done,
        "output":final,
        "url_list":obj,
        "num":length + 500,
    }
    if request.method == 'POST':
        url = request.POST.get("url_name")
        print(url)
        URLTable.objects.create(name=url)
        qs = URLTable.objects.filter(name=url)
        qs = qs.reverse()[0]
        num = qs.id #ID of url, maybe table sl.no
        print('num' + str(num))
        base = []
        while num > 0:
        	remainder = int(num % 62)
        	base.append(remainder)
        	num = int(num / 62)

        base.reverse()
        print(base)

        mapped_set = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z', 26: 'A', 27: 'B', 28: 'C', 29: 'D', 30: 'E', 31: 'F', 32: 'G', 33: 'H', 34: 'I', 35: 'J', 36: 'K', 37: 'L', 38: 'M', 39: 'N', 40: 'O', 41: 'P', 42: 'Q', 43: 'R', 44: 'S', 45: 'T', 46: 'U', 47: 'V', 48: 'W', 49: 'X', 50: 'Y', 51: 'Z', 52: '0', 53: '1', 54: '2', 55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9'}

        alpha = []
        for i in base:
        	for n, let in mapped_set.items():
        		if n == i:
        			alpha.append(let)

        final = ''.join(alpha)
        print('Final ' + final)
        final = 'backbenchertech.com/short/' + final
        #final is the output url
        '''

        '''
        done = 'True'
        return render(request, template_name,{"done": done, "input":url, "output":final,"url_list":obj,"num":length + 500,})

    return render(request, template_name, context)

def short_view(request):
    try:
        rev = []
        mapped_set = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z', 26: 'A', 27: 'B', 28: 'C', 29: 'D', 30: 'E', 31: 'F', 32: 'G', 33: 'H', 34: 'I', 35: 'J', 36: 'K', 37: 'L', 38: 'M', 39: 'N', 40: 'O', 41: 'P', 42: 'Q', 43: 'R', 44: 'S', 45: 'T', 46: 'U', 47: 'V', 48: 'W', 49: 'X', 50: 'Y', 51: 'Z', 52: '0', 53: '1', 54: '2', 55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9'}

        #print(request.get_full_path())
        get_url = request.get_full_path()
        print(get_url)
        get_url = get_url.replace('/short/', '' ,1)
        url_list = list(get_url)
        print(url_list)
        for i in url_list:
            for n, let in mapped_set.items():
                if let == i:
                    rev.append(n)
        print('Rev')
        print(rev)
        d = len(rev)
        d -= 1
        ans = 0
        for j in rev:
            ans += int(j) * pow(62,d)
            d -= 1
            if d < 0:
                break
        print(ans)
        qs = URLTable.objects.filter(id=ans)
        print("Final: " + qs.reverse()[0].name)
        template_name = qs.reverse()[0].name
        #get data from this(ans) ID, maybe table sl.no
        return redirect("http://" + str(template_name))
    except:
        return redirect("http://bbshort.herokuapp.com/error")
