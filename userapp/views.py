from django.shortcuts import render
from adminapp.models import userregistertable
from .models import admindata
from adminapp.urls import urlpatterns
from adminapp import templates
from .models import complaint
from django.contrib import messages
import requests
# Create your views here.
def index(request):
    return render(request,'index.html')

def userdashboard(request):
    records = {}
    data1=  requests.get('https://agriitech.000webhostapp.com/API/fetchSecurityapi.php')
    data2 = requests.get('https://agriitech.000webhostapp.com/API/fetchWaterlevelapi.php')
    data3 = requests.get('https://agriitech.000webhostapp.com/API/fetchSoilapi.php')
    data4 = requests.get('https://agriitech.000webhostapp.com/API/fetchrainapi.php')
    data5 = requests.get('https://agriitech.000webhostapp.com/API/fetchfireapi.php')
    data6 = requests.get('https://agriitech.000webhostapp.com/API/fetchSmokeapi.php')
    livedata1 = data1.json()
    lastdata1 = livedata1["security"][-1]
    print(lastdata1)


    livedata2 = data2.json()
    lastdata2 = livedata2["Waterlevel"][-1]
    print(lastdata2)


    livedata3 = data3.json()
    lastdata3 = livedata3["Soil"][-1]
    print(lastdata3)


    livedata4 = data4.json()
    lastdata4 = livedata4["rain"][-1]
    print(lastdata4)

    livedata5 = data5.json()
    lastdata5 = livedata5["fire"][-1]
    print(lastdata5)

    livedata6 = data6.json()
    lastdata6 = livedata6["Smoke"][-1]
    print(lastdata6)

    records['secvalue'] = lastdata1
    records['WaterLevel'] = lastdata2
    records['soil'] = lastdata3
    records['Rain'] = lastdata4
    records['Fire'] = lastdata5
    records['smoke'] = lastdata6

    # profile = userregistertable.objects.all()
    # context = {
    #     'profile':profile
    # }
    return render(request,'userdashboard.html',records)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def complaintregister(request):
    if request.method == "POST":
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        number = request.POST.get("number")

        # uno = request.POST.get("phoneno")
        # uphone = request.POST.get("phoneno")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        # uphone = request.POST.get("phoneno")

        insertdata = complaint(fname=fname,lname=lname,number=number,email=email,subject=subject)
        insertdata.save()
        messages.success(request, "successfully register")
    else:
        messages.error(request, "error")
    return render(request, 'contact.html')

def tablebasic(request):
    records = {}
    data1=  requests.get('https://agriitech.000webhostapp.com/API/fetchSecurityapi.php')
    data2 = requests.get('https://agriitech.000webhostapp.com/API/fetchWaterlevelapi.php')
    data3 = requests.get('https://agriitech.000webhostapp.com/API/fetchSoilapi.php')
    data4 = requests.get('https://agriitech.000webhostapp.com/API/fetchrainapi.php')
    data5 = requests.get('https://agriitech.000webhostapp.com/API/fetchfireapi.php')
    data6 = requests.get('https://agriitech.000webhostapp.com/API/fetchSmokeapi.php')
    livedata1 = data1.json()
    lastdata1 = livedata1["security"][-1]
    print(lastdata1)


    livedata2 = data2.json()
    lastdata2 = livedata2["Waterlevel"][-1]
    print(lastdata2)


    livedata3 = data3.json()
    lastdata3 = livedata3["Soil"][-1]
    print(lastdata3)


    livedata4 = data4.json()
    lastdata4 = livedata4["rain"][-1]
    print(lastdata4)

    livedata5 = data5.json()
    lastdata5 = livedata5["fire"][-1]
    print(lastdata5)

    livedata6 = data6.json()
    lastdata6 = livedata6["Smoke"][-1]
    print(lastdata6)

    records['secvalue'] = lastdata1
    records['WaterLevel'] = lastdata2
    records['soil'] = lastdata3
    records['Rain'] = lastdata4
    records['Fire'] = lastdata5
    records['smoke'] = lastdata6
    return render(request,'table_basic.html',records)

def services(request):
    return render(request,'services.html')

def userlogin(request):
    return render(request,'userlogin.html')

def adminlogin(request):
    return render(request,'adminlogin.html')

def fetchadminlogindata(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        pwd = request.POST.get("adminpassword")

        try:
            userdetails = admindata.objects.get(email=email,password=pwd)
        except:
            userdetails = None

        if userdetails is not None:
            return render(request,'adminindex.html')
        else:
            return render(request,"incorrect Username or pass")

    else:
        pass
        return render(request,'adminlogin.html')

def fetchlogindata(request):
    if request.method == 'POST':
        uemail = request.POST.get("useremail")
        upass = request.POST.get("userpass")

        try:
            userdetails = userregistertable.objects.get(email=uemail,uspass=upass)
        except:
            userdetails = None

        if userdetails is not None:
            return render(request,'userdashboard.html')
        else:
            return render(request,"incorrect email or pass")

    else:
        pass
        return render(request,'adminlogin.html')

def logout(request):
    try:
        del request.session['logid'],
        del request.session['logname'],
    except:
        pass
    return render(request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html')

def logout(request):
    try:
        del request.session['logid'],
        del request.session['logname'],
    except:
        pass
    return render(request,'index.html')



def securitydatatable(requests):
    return render(requests,'securitydatatable.html')

def soildatatable(requests):
    return render(requests,'index.html')

def flamedatatable(requests):
    return render(requests,'index.html')

def calendar(requests):
    return render(requests,'calendar.html')

def indexboxed(requests):
    return render(requests,'index-boxed.html')

def indexhorizontal(requests):
    return render(requests,'index-horizontal.html')

def indexvertical(requests):
    return render(requests,'index-vertical.html')

def profile(requests):
    return render(requests,'profile.html')

def profilenotifications(requests):
    return render(requests,'profile-notification.html')

def profilesecurity(requests):
    return render(requests,'profile-security.html')

def profilesettions(requests):
    return render(requests,'profile-settings.html')

def supportecenter(requests):
    return render(requests,'support-center.html')

def supportfaqs(requests):
    return render(requests,'support-faqs.html')

def supportticketdetail(requests):
    return render(requests,'support-ticket-detail.html')

def supporttickets(requests):
    return render(requests,'support-ticket.html')

def tablebasic(request):
    records = {}
    data1=  requests.get('https://agriitech.000webhostapp.com/API/fetchSecurityapi.php')
    data2 = requests.get('https://agriitech.000webhostapp.com/API/fetchWaterlevelapi.php')
    data3 = requests.get('https://agriitech.000webhostapp.com/API/fetchSoilapi.php')
    data4 = requests.get('https://agriitech.000webhostapp.com/API/fetchrainapi.php')
    data5 = requests.get('https://agriitech.000webhostapp.com/API/fetchfireapi.php')
    data6 = requests.get('https://agriitech.000webhostapp.com/API/fetchSmokeapi.php')
    livedata1 = data1.json()
    lastdata1 = livedata1["security"][-1]
    print(lastdata1)


    livedata2 = data2.json()
    lastdata2 = livedata2["Waterlevel"][-1]
    print(lastdata2)


    livedata3 = data3.json()
    lastdata3 = livedata3["Soil"][-1]
    print(lastdata3)


    livedata4 = data4.json()
    lastdata4 = livedata4["rain"][-1]
    print(lastdata4)

    livedata5 = data5.json()
    lastdata5 = livedata5["fire"][-1]
    print(lastdata5)

    livedata6 = data6.json()
    lastdata6 = livedata6["Smoke"][-1]
    print(lastdata6)

    records['secvalue'] = lastdata1
    records['WaterLevel'] = lastdata2
    records['soil'] = lastdata3
    records['Rain'] = lastdata4
    records['Fire'] = lastdata5
    records['smoke'] = lastdata6
    return render(request,'table_basic.html',records)

def tabledatatables(request):
    records = {}
    data1 = requests.get('https://agriitech.000webhostapp.com/API/fetchSecurityapi.php')
    data2 = requests.get('https://agriitech.000webhostapp.com/API/fetchWaterlevelapi.php')
    data3 = requests.get('https://agriitech.000webhostapp.com/API/fetchSoilapi.php')
    data4 = requests.get('https://agriitech.000webhostapp.com/API/fetchrainapi.php')
    data5 = requests.get('https://agriitech.000webhostapp.com/API/fetchfireapi.php')
    data6 = requests.get('https://agriitech.000webhostapp.com/API/fetchSmokeapi.php')
    livedata1 = data1.json()
    livedata2 = data2.json()
    livedata3 = data3.json()
    livedata4 = data4.json()
    livedata5 = data5.json()
    livedata6 = data6.json()
    records['secvalue'] = livedata1
    records['WaterLevel'] = livedata2
    records['soil'] = livedata3
    records['Rain'] = livedata4
    records['Fire'] = livedata5
    records['smoke'] = livedata6
    return render(request,'table_datatables.html',records)

def securitydatatable(request):
    records = {}
    data1 = requests.get('https://agriitech.000webhostapp.com/API/fetchSecurityapi.php')
    livedata1 = data1.json()
    records['secvalue'] = livedata1
    return render(request, 'securitydatatable.html',records)

def waterdatatable(request):
    records = {}
    data1 = requests.get('https://agriitech.000webhostapp.com/API/fetchWaterlevelapi.php')
    livedata1 = data1.json()
    records['watervalue'] = livedata1
    return render(request, 'waterdatatable.html',records)

def soildatatable(request):
    records = {}
    data1 = requests.get('https://agriitech.000webhostapp.com/API/fetchSoilapi.php')
    livedata1 = data1.json()
    records['soilvalue'] = livedata1
    return render(request, 'soildatatable.html', records)

def raindatatable(request):
    records = {}
    data1 = requests.get('https://agriitech.000webhostapp.com/API/fetchrainapi.php')
    livedata1 = data1.json()
    records['rainvalue'] = livedata1
    return render(request, 'raindatatable.html', records)

def flamedatatable(request):
    records = {}
    data1 = requests.get('https://agriitech.000webhostapp.com/API/fetchfireapi.php')
    livedata1 = data1.json()
    records['firevalue'] = livedata1
    return render(request, 'flamedatatable.html', records)

def Smoke(request):
    records = {}
    data1 = requests.get('https://agriitech.000webhostapp.com/API/fetchSmokeapi.php')
    livedata1 = data1.json()
    records['smokevalue'] = livedata1
    return render(request, 'Smoke.html', records)
def contact(request):
    return render(request,'contact.html')