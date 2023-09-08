from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Services, Art, Booking, Contact

# Create your views here.

def index(request):
	s = Services.objects.all()
	return render(request, 'index.html', {
		'service' : s,
		})

def about(request):
	return render(request, 'about.html')

def register(request):
	return render(request, 'register.html')

def handlesignup(request):
	u = User.objects.all()
	l1 = []
	for i in u:
		l1.append(i.username)

	if request.method == 'POST':
 		# get parameters
 		username = request.POST['email']
 		email = request.POST['email']
 		fname = request.POST['firstname']
 		lname = request.POST['lastname']
 		pass1 = request.POST['passwd']

 		if username in l1:
 			return render(request, 'register.html', {
 				'yes' : "yes",
 				'msg' : "Email already exists.."
 				})

 		# Create user
 		myuser = User.objects.create_user(username, email, pass1)
 		myuser.first_name = fname
 		myuser.last_name = lname
 		myuser.save()
 		return render(request,'register.html', {
 			'yes' : "yes",
 			'msg' : "Successfully signed up..."
 			})

def handlesignin(request):
	s = Services.objects.all()
	if request.method == 'POST':
		loginusername = request.POST['username']
		loginpassword = request.POST['password']

		user = authenticate(username=loginusername, password=loginpassword)

		if user is not None:
			login(request,user)
			return render(request, 'home.html', {
			'service' : s,
			'yes' : "yes",
			'msg' : "Successfully logged in.."
			})
		else:
			return redirect('/login/')
	return render(request, 'register.html')

def handlelogout(request):
	logout(request)
	return redirect('/')

def contact(request):
	if request.method == "POST":
		cname = request.POST['Name']
		cemail = request.POST['Email']
		cphone = request.POST['Phone']
		cmsg = request.POST['Message']

		con = Contact(c_name=cname, c_email=cemail, c_phone=cphone, c_msg=cmsg)
		con.save()
		yes = "yes"
		return render(request, 'contact.html', {
			'yes' : yes,
			'msg' : "Thank you for contacting us..."
			})
	else:
		yes = "no"
		return render(request, 'contact.html', {
			'yes' : yes
			})

def home(request):
	s = Services.objects.all()
	yes = "no" 
	return render(request, 'home.html', {
		'service' : s,
		'yes' : yes,
		})

def services(request):
	s = Services.objects.all()
	yes = "no"
	return render(request, 'services.html', {
		'service' : s,
		'yes' : yes,
		})

def subservice(request, myservice):
	subs = Art.objects.all()
	list1 = []
	for i in subs:
		if i.a_service.service == myservice:
			list1.append(i)
	
	return render(request, 'subservice.html', {
		'subservice' : list1,
		})

def checkout(request, myid):
	serve1 = Art.objects.filter(a_id=myid)
	return render(request, 'checkout.html', {
		's' : serve1[0],
		})

def booking(request, sid):
	booking_of = Art.objects.filter(a_id=sid)
	s = Services.objects.all()
	if request.method == "POST":
		baddress = request.POST.get('uadd', '')
		bcontact = request.POST.get('ucontact', '')
		bdate = request.POST.get('udate', '')

		book = Booking(booking_user=request.user, booking_phone=bcontact, booking_address=baddress, 
			booking_date_of_service=bdate, booking_service=booking_of[0])
		book.save()
		yes = "yes"
		return render(request, 'home.html', {
			'ss' : booking_of[0],
			'service' : s,
			'yes' : yes,
			'msg' : f"Thanks For Booking, You will get a call soon from the {booking_of[0].a_name}."
			})

def mybooking(request):
	u1 = Booking.objects.filter(booking_user=request.user)
	return render(request, 'mybooking.html', {
		'booking' : u1,
		})

def cancelbooking(request, cid):
	s = Services.objects.all()
	c = Booking.objects.filter(booking_id=cid)
	c.delete()
	return render(request, 'home.html', {
		'service' : s,
		'yes' : "yes",
		'msg' : "Your booking is cancelled.."
		})