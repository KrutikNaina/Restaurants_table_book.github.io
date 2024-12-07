from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from db.models import customer

def home(request):
    return render(request,"index.html")

# def invoice(request,id):
# 	showdata = customer.objects.get(rname=id)
# 	dd={
# 	'showdata':showdata
# 	}
# 	return render(request,'invoice.html',dd)


def insert(request):
    rname = (request.POST["rname"])
    rlastname =  (request.POST["rlastname"])
    remail = (request.POST["remail"])
    rphone = int (request.POST["rphone"])
    rperson = (request.POST["rperson"])
    rtable = (request.POST["rtable"])
    rdate =  (request.POST["rdate"])
    rtime =  (request.POST["rtime"])
    rcomment = (request.POST["rcomment"])
    res = customer( rname = rname, rlastname = rlastname,remail = remail,  rphone = rphone, rperson = rperson,rtable = rtable, rtime = rtime, rdate = rdate, rcomment = rcomment)
    res.save()
    return HttpResponseRedirect("/home/")

def invoice(request,id):
	showdata = customer.objects.all(rname = id)
	display={
	'showdata':showdata
	}
	return render(request,"invoice.html",display)

def delete(request,id):
	empdata = customer.objects.get(id=id)
	empdata.delete()
	return HttpResponseRedirect('/addcart/')