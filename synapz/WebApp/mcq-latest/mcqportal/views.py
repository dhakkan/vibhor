from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404,HttpResponseRedirect, HttpResponse
from mcqportal.models import Questiondetails,Members,answers
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404,render
import random 
import copy
from django.db.models import Count
from django.db.models import Max

def index(request):
	request.session['counter'] = copy.deepcopy([])
	request.session['mcq'] = copy.deepcopy([[],[],[],[]])
	if 'uid' in request.session :
#		name=request.session['name']	
#		return HttpResponse(name);
		request.session['pg1session']=1
		if 'pg2session' in request.session:
			del request.session['pg2session']
		if 'pg3session' in request.session:
			del request.session['pg3session']
		if 'pg4session' in request.session:
			del request.session['pg4session']
		return render(request,'mcqportal/index.html', {'user':request.session['name']})
	else:
		return render(request,'mcqportal/login.html')
#	return render(request,'mcqportal/index.html')


"""def p1_submit(request):
#	return HttpResponse("sjkdjhasdlfhladsfl")	
    try:
        mcq1 = list(Questiondetails.objects.all())
        random.shuffle(mcq1)
        mcq = mcq1[:15]
    except Questiondetails.DoesNotExist:
        raise Http404
    return render(request,'mcqportal/pg1.html',{'mcq':mcq})"""

def login(request):	
	return render(request,'mcqportal/login.html')

def signin(request):
	try:
		m = Members.objects.get(email=request.POST['eid_signIn'])
	except Members.DoesNotExist:
		context = {
			'alerts': "invalid Email: u may SIGNUP",  
			'class': "error"
		}
		return render(request,'mcqportal/login.html', context)
	if m.password == request.POST['passwd_signIn']:
		request.session['uid'] = m.memberid
		request.session['name'] = m.username
		return render(request,'mcqportal/index.html')
	#	return HttpResponse("You're logged in.")
   	else:
		context = {
			'alerts': "Email and password did not match. Please try again.",  
			'class': "error"
		}
		return render(request,'mcqportal/login.html', context)
	
		#return HttpResponse("Your username and password didn't match.")
#	return HttpResponse("Successfully logged in");

def signup(request):
	name=request.POST['name']
	email=request.POST['eid']
	password=request.POST['passwd']
	try:
		m = Members.objects.get(email=email)
		context = {
			'alerts': "Email already exists.",  
			'class': "error"
		}
		return render(request,'mcqportal/login.html', context)
	except Members.DoesNotExist:
		count = Members.objects.all().count()
		if count == 0:
			memid = 1
		else:
			memid = Members.objects.order_by("-memberid")[0].memberid + 1
		user=Members(memberid=memid,username=name,email=email,password=password)
		user.save()
		request.session['uid']=user.memberid
		request.session['name'] = user.username
#	return HttpResponse(name + "   "  + email + "    " + password);
		return index(request)


def chksession(request):
	if 'page' in request.POST:
		if request.POST['page']=='pg1':
			del request.session['pg1session']
			request.session['pg2session']=1
		if request.POST['page']=='pg2':
			del request.session['pg2session']
			request.session['pg3session']=1
		if request.POST['page']=='pg3':
			del request.session['pg3session']
			request.session['pg4session']=1
		if request.POST['page']=='pg4':
			del request.session['pg4session']
	
	if 'pg1session' in request.session:
		return pg1(request)
	if 'pg2session' in request.session:
		return pg2(request)
	if 'pg3session' in request.session:
		return pg3(request)
	if 'pg4session' in request.session:
		return pg4(request)
	return pg5(request)



def logout(request):
    del request.session
    return render(request,'mcqportal/login.html')

def pg1(request):
    if 'uid' not in request.session:
        return render(request,'mcqportal/login.html')
    if  'pg1session' not in request.session:
	return chksession(request)

#    if request.session['pg1session']==0:
 #       return render(request,'mcqportal/index.html')
    uid=request.session['uid']
    try:
        a = list(Questiondetails.objects.filter(category=1))
        random.shuffle(a)
        mcq = a[:1]
        for i in mcq:
            v=Questiondetails.objects.get(id=i.id)
            b=answers(memberid=uid,qid=v,answer=0)
            b.save()
#        request.session['pg1session']=0;
#     request.session['mcq'][0] = copy.deepcopy(a[:1])
    except Questiondetails.DoesNotExist:
        raise Http404
    return render(request,'mcqportal/pg1.html',{'mcq':mcq,'user':request.session['name']})
  #  return render(request,'mcqportal/pg1.html',{'mcq':request.session['mcq'][0], 'b':"Aptitude"})


"""        try:
            a=answers(memberid=uid,qid=i,answer=request.POST[i])
            a.save()	"""

def pg2(request):
    if 'uid' not in request.session :
        return render(request,'mcqportal/login.html')
    if  'pg2session' not in request.session:
	return chksession(request)

#    global ans1
#	myanswers=""
    uid=request.session['uid']
    for i in request.POST:
        #		myanswers+="qid-"
#		myanswers+=i
#		myanswers+="the answer-"
#		myanswers+=request.POST[i]

#        except:
         try:
             a=answers.objects.filter(qid=i).aggregate(Max('id'))
	     b=answers.objects.get(id=a['id__max'])
             b.answer = request.POST[i]
             b.save()
         except:
             apple=""
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
    try:
        c = list(Questiondetails.objects.filter(category=2))
        random.shuffle(c)
        mcq = c[:1]
        for i in mcq:
            v=Questiondetails.objects.get(id=i.id)
            b=answers(memberid=uid,qid=v,answer=0)
            b.save()	
#     request.session['mcq'][0] = copy.deepcopy(a[:1])
    except Questiondetails.DoesNotExist:
        raise Http404
	
#	return HttpResponse(myanswers)
    return render(request,'mcqportal/pg2.html',{'mcq':mcq,'user':request.session['name']})

def pg3(request):

    #uid=request.session['uid']
    if 'uid' not in request.session :
        return render(request,'mcqportal/login.html')
    if  'pg3session' not in request.session:
	return chksession(request)

    uid=request.session['uid']
    for i in request.POST:
        #		myanswers+="qid-"
#		myanswers+=i
#		myanswers+="the answer-"
#		myanswers+=request.POST[i]
         try:
	     a=answers.objects.filter(qid=i).aggregate(Max('id'))
	     b=answers.objects.get(id=a['id__max'])
             b.answer = request.POST[i]
             b.save()
         except:
             apple=""
#    for i in request.session['mcq'][1]:
#        if str(i.pk) in request.POST:
#            if i.answer == request.POST[str(i.pk)]:
#                count = count + 1
#      #          request.session['counter'][1] = request.session['counter'][1] + 1
#            ans2.append(request.POST[str(i.pk)])
#        else:
#            ans2.append(0)
    #return HttpResponse( request.session['mcq'])
    try:
        c = list(Questiondetails.objects.filter(category=3))
        random.shuffle(c)
        mcq = c[:1]
        for i in mcq:
            v=Questiondetails.objects.get(id=i.id)
            b=answers(memberid=uid,qid=v,answer=0)
            b.save()	
#     request.session['mcq'][0] = copy.deepcopy(a[:1])
    except Questiondetails.DoesNotExist:
        raise Http404
	
#	return HttpResponse(myanswers)
    return render(request,'mcqportal/pg3.html',{'mcq':mcq,'user':request.session['name']})

def pg4(request):
    if 'uid' not in request.session :
        return render(request,'mcqportal/login.html')
    if  'pg4session' not in request.session:
	return chksession(request)

    uid=request.session['uid']
    for i in request.POST:
        #		myanswers+="qid-"
#		myanswers+=i
#		myanswers+="the answer-"
#		myanswers+=request.POST[i]
         try:
             a=answers.objects.filter(qid=i).aggregate(Max('id'))
	     b=answers.objects.get(id=a['id__max'])
             b.answer = request.POST[i]
             b.save()
         except:
             apple=""


#    global ans3
#    global mcq3
#    try:
#        a = list(Questiondetails.objects.all())
#        random.shuffle(a)
#        request.session['mcq'][3] = copy.deepcopy(a[:1])
#        c = Context({"mcq" : request.session['mcq'][3]})
#    except Questiondetails.DoesNotExist:
#        raise Http404
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
    try:
        c = list(Questiondetails.objects.filter(category=4))
        random.shuffle(c)
        mcq = c[:1]
        for i in mcq:
            v=Questiondetails.objects.get(id=i.id)
#            w=Members.objects.get(id=i.id)
            b=answers(memberid=uid,qid=v,answer=0)
            b.save()	
#     request.session['mcq'][0] = copy.deepcopy(a[:1])
    except Questiondetails.DoesNotExist:
        raise Http404
	
#	return HttpResponse(myanswers)
    return render(request,'mcqportal/pg4.html',{'mcq':mcq,'user':request.session['name']})
 #   return HttpResponse( request.session['mcq'][2])

def pg5(request):
    uid=request.session['uid']
    if 'uid' not in request.session :
        return render(request,'mcqportal/login.html')
    uid=request.session['uid']
    for i in request.POST:
        #		myanswers+="qid-"
#		myanswers+=i
#		myanswers+="the answer-"
#		myanswers+=request.POST[i]
         try:
             a=answers.objects.filter(qid=i).aggregate(Max('id'))
	     b=answers.objects.get(id=a['id__max'])
             b.answer = request.POST[i]
             b.save()
         except:
             apple=""

    try:
        mcq = list(answers.objects.filter(memberid=uid))
        mcq = mcq[-4:]
#     request.session['mcq'][0] = copy.deepcopy(a[:1])
    except Questiondetails.DoesNotExist:
        raise Http404
    a=[]
    for i in range(4):
        temp = []
        for j in range(1):
            val = j+i
            temp.append(mcq[val])
        a.append(temp)
    return render(request,'mcqportal/pg5.html',{'mcq':a,'user':request.session['name']})
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

#    	return render(request,'mcqportal/pg5.html')

def save(request):      #for FB login
    #    if request.GET['user'] in
    try:
        user = Members.objects.get(email=request.GET['email'])
        request.session['uid']=user.memberid
	request.session['name'] = user.username
    except:
        count = Members.objects.all().count()
        if count == 0:
            memid = 1
        else:
            memid = Members.objects.order_by("-memberid")[0].memberid + 1
        user=Members(memberid=memid,username=request.GET['user'],email=request.GET['email'])
        user.save()
        request.session['uid']=user.memberid
	request.session['name'] = user.username
#        return render(request,'mcqportal/index.html')
        #return HttpResponseRedirect("mcqportal/index.html")
    return render(request,'mcqportal/index.html')
    #return HttpResponseRedirect("mcqportal/index.html")
#        return render(request,'mcqportal/index.html')
    #except:
        #return render(request,'mcqportal/login.html')
