from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404,HttpResponseRedirect, HttpResponse
from mcqportal.models import Questiondetails,Members
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404,render
import random 
import copy

def index(request):
	request.session['counter'] = copy.deepcopy([])
	request.session['mcq'] = copy.deepcopy([[],[],[],[]])
	if 'name' in request.session :
		name=request.session['name']	
#		return HttpResponse(name);
		return render(request,'mcqportal/index.html')
	else:
		return render(request,'mcqportal/login.html')
#	return render(request,'mcqportal/index.html')


def p1_submit(request):
#	return HttpResponse("sjkdjhasdlfhladsfl")	
    try:
        mcq1 = list(Questiondetails.objects.all())
        random.shuffle(mcq1)
        mcq = mcq1[:15]
    except Questiondetails.DoesNotExist:
        raise Http404
    return render(request,'mcqportal/pg1.html',{'mcq':mcq})

def login(request):	
	return render(request,'mcqportal/login.html')

def signin(request):
	try:
		m = Members.objects.get(email=request.POST['eid_signIn'])
	except Members.DoesNotExist:
		return HttpResponse("invalid Email: u may SIGNUP")
	if m.password == request.POST['passwd_signIn']:
		request.session['name'] = m.username
		return render(request,'mcqportal/index.html')
	#	return HttpResponse("You're logged in.")
   	else:
		return HttpResponse("Your username and password didn't match.")
#	return HttpResponse("Successfully logged in");

def signup(request):
	name=request.POST['name']
	email=request.POST['eid']
	password=request.POST['passwd']
	try:
		m = Members.objects.get(email=email)
		return HttpResponse("Email already exists")
	except Members.DoesNotExist:
		user=Members(username=name,email=email,password=password)
		user.save()
		request.session['name']=name
#	return HttpResponse(name + "   "  + email + "    " + password);
		return render(request,'mcqportal/index.html')

def logout(request):
	del request.session['name']
	return render(request,'mcqportal/login.html')

def pg1(request):
    if 'name' not in request.session:
        return render(request,'mcqportal/login.html')
    try:
        a = list(Questiondetails.objects.get(category=4))
        random.shuffle(a)
        request.session['mcq'][0] = copy.deepcopy(a[:1])
    except Questiondetails.DoesNotExist:
        raise Http404
    return HttpResponse(request.session['mcq'][0])
 #   return HttpResponse("")
  #  return render(request,'mcqportal/pg1.html',{'mcq':request.session['mcq'][0], 'b':"Aptitude"})

def pg2(request):
	if 'name' not in request.session :
		return render(request,'mcqportal/login.html')
#    global ans1
	count = 0
   	try:
       		a = list(Questiondetails.objects.all())
        	random.shuffle(a)
#        request.session['mcq'][1] = copy.deepcopy(a[:1])
   	except Questiondetails.DoesNotExist:
       		raise Http404
	
	myanswers=""
	for i in request.POST:
		myanswers+="qid-"
		myanswers+=i
		myanswers+="the answer-"
		myanswers+=request.POST[i]
		
#    for i in request.session['mcq'][0]:
#        if str(i.pk) in request.POST:
#            if i.answer == request.POST[str(i.pk)]:
#                count = count + 1
#            ans1.append(request.POST[str(i.pk)])
#        else:
#            ans1.append(0)
#    lis = request.session['counter']
#    lis.append(count)
#    request.session['counter'] = copy.deepcopy(lis)
    #return HttpResponse( request.session['mcq'][0])
#  return render(request,'mcqportal/pg2.html',{'mcq':request.session['mcq'][1], 'b':"Programming"})
#   return render(request,'mcqportal/pg2.html')
	
	return HttpResponse(myanswers)

def pg3(request):
    if 'name' not in request.session :
        return render(request,'mcqportal/login.html')
    count = 0
    global ans2
    try:
        a = list(Questiondetails.objects.all())
        random.shuffle(a)
        request.session['mcq'][2] = copy.deepcopy(a[:1])
    except Questiondetails.DoesNotExist:
        raise Http404
#    for i in request.session['mcq'][1]:
#        if str(i.pk) in request.POST:
#            if i.answer == request.POST[str(i.pk)]:
#                count = count + 1
#      #          request.session['counter'][1] = request.session['counter'][1] + 1
#            ans2.append(request.POST[str(i.pk)])
#        else:
#            ans2.append(0)
    lis = request.session['counter']
    lis.append(count)
    request.session['counter'] = copy.deepcopy(lis)
    #return HttpResponse( request.session['mcq'])
    return render(request,'mcqportal/pg3.html',{'mcq':request.session['mcq'][2], 'b':"Datastructures"})

def pg4(request):
    if 'name' not in request.session :
        return render(request,'mcqportal/login.html')
    count = 0
#    global ans3
#    global mcq3
    try:
        a = list(Questiondetails.objects.all())
        random.shuffle(a)
        request.session['mcq'][3] = copy.deepcopy(a[:1])
        c = Context({"mcq" : request.session['mcq'][3]})
    except Questiondetails.DoesNotExist:
        raise Http404
#    for i in request.session['mcq'][2]:
#        if str(i.pk) in request.POST:
#            if i.answer == request.POST[str(i.pk)]:
#                count = count + 1
# ##               request.session['counter'][2] = request.session['counter'][2] + 1
#            ans3.append(request.POST[str(i.pk)])
#        else:
#            ans3.append(0)
#    lis = request.session['counter']
#    lis.append(count)
#    request.session['counter'] = copy.deepcopy(lis)
#    request.session['counter'].append(count)
#    return render(request,'mcqportal/pg4.html',{'mcq':request.session['mcq'][3], 'b':"Reasoning"})
    return render(request,'mcqportal/pg4.html')
 #   return HttpResponse( request.session['mcq'][2])

def pg5(request):
	if 'name' not in request.session :
		return render(request,'mcqportal/login.html')
	count = 0
#    global ans4
#    for i in request.session['mcq'][3]:
#        if str(i.pk) in request.POST:
#            if i.answer == request.POST[str(i.pk)]:
#                count = count + 1
#                #request.session['counter'][3] = request.session['counter'][3] + 1
#            ans4.append(request.POST[str(i.pk)])
#        else:
#            ans4.append(0)
#    lis = request.session['counter']
#    lis.append(count)
#    request.session['counter'] = copy.deepcopy(lis)
#    request.session['counter'].append(count)
    #return render(request,'mcqportal/pg5.html',{'counter':request.session['counter'],'mcq':request.session['mcq'],'ans1':ans1,'ans2':ans2,'ans3':ans3,'ans4':ans4})
#   return render(request,'mcqportal/pg5.html',{'counter':request.session['counter'],'mcq0':request.session['mcq'][0],'mcq1':request.session['mcq'][1],'mcq2':request.session['mcq'][2],'mcq3':request.session['mcq'][3],'ans1':ans1,'ans2':ans2,'ans3':ans3,'ans4':ans4})
	return HttpResponse(request.session['mcq'][0]+request.session['mcq'][2])

