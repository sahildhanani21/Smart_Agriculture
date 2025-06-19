from django.shortcuts import render
from .models import userregistertable
from django.contrib import messages
from userapp.models import complaint
import requests
# Create your views here.
def adminindex(request):
    return render(request,'adminindex.html')


def complaints(request):
    complaints = complaint.objects.all()
    context = {
        'complaints':complaints
    }
    return render(request,'complaints.html',context)

def userdatatable(request):
    userdetails = userregistertable.objects.all()
    context = {
        'user':userdetails
    }
    return render(request,'userdatateble.html',context)

def usersensordata(request):
    records = {}
    data = requests.get(url = "https://agriitech.000webhostapp.com/API/fetchSmokeapi.php")
    livedata = data.json()
    records['smokedata']= livedata
    return render(request,'sensordata.html',records)

def flamedatatable(request):
    records = {}
    data = requests.get(url="https://agriitech.000webhostapp.com/API/fetchfireapi.php")
    livedata = data.json()
    records['flamedata'] = livedata
    return render(request,'flamedatatable.html',records)

def securitydatatable(request):
    records = {}
    data = requests.get(url="https://agriitech.000webhostapp.com/API/fetchSecurityapi.php")
    livedata = data.json()
    records['securitydata'] = livedata
    return render(request,'securitydatatable.html',records)

def waterdatatable(request):
    records = {}
    data = requests.get(url="https://agriitech.000webhostapp.com/API/fetchWaterlevelapi.php")
    livedata = data.json()
    records['waterleveldata'] = livedata
    return render(request,'waterdatatable.html',records)

def soildatatable(request):
    records = {}
    data = requests.get(url="https://agriitech.000webhostapp.com/API/fetchSoilapi.php")
    livedata = data.json()
    records['soildatatable'] = livedata
    return render(request,'soildatatable.html',records)

def raindatatable(request):
    records = {}
    data = requests.get(url="https://agriitech.000webhostapp.com/API/fetchrainapi.php")
    livedata = data.json()
    records['raindatatable'] = livedata
    return render(request,'raindatatable.html',records)

def fetchregdata(request):
    if request.method == "POST":
        uemail = request.POST.get("email")
        ufname = request.POST.get("fname")
        ulname = request.POST.get("lname")
        uphone = request.POST.get("phone")
        uaddress = request.POST.get("address")
        # upass = request.POST.get("pass")
        # ucpass = request.POST.get("cpass")

        import random
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = 6
        nr_symbols = 1
        nr_numbers = 3
        password_list = []

        for char in range(1, nr_letters + 1):
            password_list.append(random.choice(letters))

        for char in range(1, nr_symbols + 1):
            password_list += random.choice(symbols)

        for char in range(1, nr_numbers + 1):
            password_list += random.choice(numbers)

        print(password_list)
        random.shuffle(password_list)
        print(password_list)

        password = ""  # we will get final password in this var.
        for char in password_list:
            password += char

        ##############################################################

        msg = "hello here it is your password for agri project:    " + password  # this variable will be passed as message in mail

        ############ code for sending mail ########################

        from django.core.mail import send_mail

        send_mail(
            'Your New Password is::',
            msg,
            'agriproject1310@gmail.com',
            [uemail],
            fail_silently=False,
        )
        # NOTE: must include below details in settings.py
        # detail tutorial - https://www.geeksforgeeks.org/setup-sending-email-in-django-project/
        # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        # EMAIL_HOST = 'smtp.gmail.com'
        # EMAIL_USE_TLS = True
        # EMAIL_PORT = 587
        # EMAIL_HOST_USER = 'mail from which email will be sent'
        # EMAIL_HOST_PASSWORD = 'pjobvjckluqrtpkl'   #turn on 2 step verification and then generate app password which will be 16 digit code and past it here

        #############################################

        insertdata = userregistertable(email=uemail,fname=ufname,lname=ulname,uspass=password,uscpass=password,phone=uphone,address=uaddress)
        insertdata.save()
        messages.success(request,"successfully register")
    else:
        messages.error(request,"error")
    return render(request,'auth-register.html')

# def fetchlogindata(request):
#     if request.method == 'POST':
#         uemail = request.POST.get("useremail")
#         upass = request.POST.get("userpass")
#
#         try:
#             userdetails = userregistertable.objects.get(email=uemail,password=upass)
#         except:
#             userdetails = None
#
#         if userdetails is not None:
#             return render(request,'dashboard.html')
#         else:
#             return render(request,"incorrect email or pass")
#
#     else:
#         pass
#         return render(request,'login.html')

def authconfirm(requests):
    return render(requests,'auth-confirm.html')

def authlogin(requests):
    return render(requests,'auth-login.html')

def authloginhalf(requests):
    return render(requests,'auth-login-half.html')

def authregister(requests):
    return render(requests,'auth-register.html')

def authresetpw(requests):
    return render(requests,'auth-resetpw.html')

def calendar(requests):
    return render(requests,'calendar.html')

def chartapexchart(requests):
    return render(requests,'chart-apexcharts.html')

def chartchartjs(requests):
    return render(requests,'chart-chartjs.html')

def chartinline(requests):
    return render(requests,'chart-inline.html')

def contactsgrid(requests):
    return render(requests,'contacts-grid.html')

def contactslist(requests):
    return render(requests,'contacts-list.html')

def contactsnew(requests):
    return render(requests,'contacts-new.html')

def dashboardanalytics(requests):
    return render(requests,'dashboard-analytics.html')

def dashboardsaas(requests):
    return render(requests,'dashboard-saas.html')

def dashboardsales(requests):
    return render(requests,'dashboard-sales.html')

def dashboardsystem(requests):
    return render(requests,'dashboard-system.html')

def datamaps(requests):
    return render(requests,'datamaps.html')

def filesgrid(requests):
    return render(requests,'files-grid.html')

def fileslist(requests):
    return render(requests,'files-list.html')

def formadvanced(requests):
    return render(requests,'form_advanced.html')

def formaelements(requests):
    return render(requests,'form_elements.html')

def formlayouts(requests):
    return render(requests,'form_layouts.html')

def formaupload(requests):
    return render(requests,'form_upload.html')

def formvalidation(requests):
    return render(requests,'form_validation.html')

def formwizard(requests):
    return render(requests,'form_wizard.html')

def indexboxed(requests):
    return render(requests,'index-boxed.html')

def indexhorizontal(requests):
    return render(requests,'index-horizontal.html')

def indexvertical(requests):
    return render(requests,'index-vertical.html')

def page404(requests):
    return render(requests,'page-404.html')

def page500(requests):
    return render(requests,'page-500.html')

def pageblank(requests):
    return render(requests,'page-blank.html')

def pageinvoice(requests):
    return render(requests,'page-invoice.html')

def pageorders(requests):
    return render(requests,'page-orders.html')

def pagetimeline(requests):
    return render(requests,'page-timeline.html')

def profile(requests):
    return render(requests,'profile.html')

def profilenotification(requests):
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
    return render(requests,'support-tickets.html')

def tableadvanced(requests):
    return render(requests,'table_advanced.html')

def tablebasic(requests):
    return render(requests,'table_basic.html')

def tabledatatables(requests):
    return render(requests,'table_datatables.html')

def uibuttons(requests):
    return render(requests,'ui-buttons.html')

def uicolor(requests):
    return render(requests,'ui-color.html')

def uiicons(requests):
    return render(requests,'ui-icons.html')

def uimodals(requests):
    return render(requests,'ui-modals.html')

def uinotification(requests):
    return render(requests,'ui-notification.html')

def uiprogress(requests):
    return render(requests,'ui-progress.html')

def uitabsaccordation(requests):
    return render(requests,'ui-tabs-accordion.html')

def uitypograpy(requests):
    return render(requests,'ui-typograpy.html')

def widgets(requests):
    return render(requests,'widgets.html')

