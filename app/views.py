from multiprocessing import context
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from time import time
from app.models import *

import razorpay
from bestchoicesolution_com.settings import *

client = razorpay.Client(auth=(KEY_ID,KEY_SECRET))



# Create your views here.
def BASE(request):
    return render(request,'base.html', )

def HOME(request):
    cotegory = Categories.objects.all().order_by('id')[0:7]
    service = Service.objects.filter(status = 'PUBLISH').order_by('-id')

    context = {
        'cotegory' : cotegory,
        'service' : service,
    }
    return render(request,'Main/home.html', context)

def ABOUT_US(request):    
    cotegory = Categories.objects.all().order_by('id')[0:5]

    context = {
        'cotegory' : cotegory,
    }
    return render(request,'Main/about_us.html',context)

def CONTCAT(request):
    cotegory = Categories.objects.all().order_by('id')[0:5]

    context = {
        'cotegory' : cotegory,
    }
    return render(request,'Main/contact_us.html',context)

#-------------------------------------------------------------------------------------------------------------
def SINGLE_COURS(request):
    cotegory = Categories.objects.all().order_by('id')[0:5]
    service = Service.objects.filter(status = 'PUBLISH').order_by('-id')
    FreeService_count = Service.objects.filter(price = 0).count()
    PaidService_count = Service.objects.filter(price__gte=1).count()


    context = {
        'cotegory' : cotegory,
        'service' : service,
        'FreeService_count': FreeService_count,
        'PaidService_count': PaidService_count,
    }
    return render(request, 'Main/single_service.html',context)



#-----------------------------------------------------------------------------------------------------
def filter_data(request):
    categories = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')
    


    if price == ['pricefree']:
       service = Service.objects.filter(price=0)

    elif price == ['pricepaid']:
       service = Service.objects.filter(price__gte=1)
       
    elif price == ['priceall']:
       service = Service.objects.all()


    elif categories:
       service = Service.objects.filter(category__id__in=categories).order_by('-id')

    elif level:
       service = Service.objects.filter(level__id__in = level).order_by('-id')

    else:
       service = Service.objects.all().order_by('-id')


    t = render_to_string('ajax/service.html', {'service': service})

    return JsonResponse({'data': t})

#-----------------------------------------------------------------------------------------
@login_required(login_url='/accounts/login/')

def SERVICE_DETAILS(request,slug):
    cotegory = Categories.get_all_category(Categories)
    
   
    service_id = Service.objects.get(slug = slug)   

    try:
        enroll_status = UserService.objects.get(user=request.user, service=service_id)
    except UserService.DoesNotExist:
        enroll_status = None

    service = Service.objects.filter(slug = slug)
    if service.exists():
        service = service.first()
    else:
        return redirect('404')

    context = {
        'service':service,
        'cotegory':cotegory,
        
        'enroll_status':enroll_status
    }
    return render(request,'service/service_details.html', context)

#--------------------------------------------------------------------------------------------------------#

def SEARCH_SERVICE(request):
    query = request.GET['query']
    service = Service.objects.filter(title__icontains = query)
    context = {
        'service':service,
    }
    return render(request,'search/search.html',context)



#----------------------------------------------------------------------------------------------------------#
def PAGE_NOTFOUND(request):
    cotegory = Categories.objects.all()    
    context = {        
        'cotegory' : cotegory,       
        
    }
    return render(request, 'error/error404.html',context)


#-------------------------------------------------------------------------------------------------------------#
def CHECKOUT(request,slug):
    cotegory = Categories.objects.all() 
    service = Service.objects.get(slug = slug)
    action = request.GET.get('action')
    
    if  service.price == 0:
        service = UserService(
            user = request.user,
            service = service,
        )
        service.save()
        messages.success(request,'Service are successfully Enrolles !')
        return redirect('my_service')
    
    elif action == 'create_payment':
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            country = request.POST.get('country')
            address_1 = request.POST.get('address_1')
            address_2 = request.POST.get('address_2')
            city = request.POST.get('city')
            postcode = request.POST.get('postcode')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            order_comments = request.POST.get('order_comments')

            amount = service.price * 100
            currency = "INR"

            notes = {
                "Name": first_name,
                "last_name": last_name,
                "country": country,
                "address_1": address_1,
                "address_2": address_2,
                "city": city,
                "postcode": postcode,
                "phone": phone,
                "email": email,
                "order_comments": order_comments,

            }
            receipt = " BCS {int(time())}"
            order = client.order.create(
                {
                    'receipt': receipt,
                    'notes': notes,
                    'amount': amount,
                    'currency': currency,

                }
            )
            payment = Payment(
                service=service,
                use=request.user,
                order_id=order.get('id')
            )
            payment.save()



    context = {        
        'cotegory' : cotegory,  
        'service'  : service,    
        'order'  : order,    
        
    }
    return render(request, 'checkout/checkout.html',context)
#--------------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/accounts/login/')
def MY_SERVICE(request):
    cotegory = Categories.objects.all()
    service = UserService.objects.filter(user = request.user)
    
    
    context = {        
        'cotegory' : cotegory,
        'service' : service,       
        
    }
    return render(request, 'service/my_service.html',context)
    
#-------------------------------------------------------------------------------------------------------------------------------
