from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import User, products, usersContacts, usersrecycling
from django import forms
from .forms import PrivateSignUpForm, CorpSignUpForm, ProductForm, UserDetailsForm, UserDetailsEditForm, UserRecyclingForm
@login_required
def master(request):
    loginuser = request.user
    checkadmin = loginuser.is_superuser
    usertype = loginuser.user_type
    if checkadmin:
        usertype = "a"

    

    return render(request, 'master.html', {'userType': usertype})

def register(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

@login_required
def contact_view(request):
    #צריך לשלוח את הסוג משתמש בכל דף כדי להציג את התפריט הנכון לפי משתמש
    loginuser = request.user
    checkadmin = loginuser.is_superuser
    usertype = loginuser.user_type
    if checkadmin:
        usertype = "a"
    #

    if request.method == 'POST':
        user_id = int(request.POST.get('user_id'))
        userObj = User.objects.get(id=user_id)
        contact_text = request.POST.get('contactText')
        new_contact = usersContacts(user=userObj, content = contact_text)
        new_contact.save()
        return HttpResponse("Data successfully inserted!")
    else:
        return render(request, 'contact_form.html', {'userType': usertype})
    

def display_contacts(request):
    loginuser = request.user
    checkadmin = loginuser.is_superuser
    usertype = loginuser.user_type
    if checkadmin:
        usertype = "a"
    contacts = usersContacts.objects.order_by('status', 'creationDT')
    return render(request, 'display_contacts.html', {'contacts': contacts, 'userType': usertype})

def changestatus(request, pk):
    contact = usersContacts.objects.get(id=pk)
    contact.status = True
    contact.save()
    return HttpResponseRedirect("/website/display_contacts/")


def register_view(request):
    # Your register logic goes here
    return render(request, 'register.html')


class privateuser_register(CreateView):
    model = User
    form_class = PrivateSignUpForm
    template_name = 'privateuser_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class corpuser_register(CreateView):
    model = User
    form_class = CorpSignUpForm
    template_name = 'corpuser_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html', context={'form': AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

def addproduct(request):
    loginuser = request.user
    checkadmin = loginuser.is_superuser
    usertype = loginuser.user_type
    userID = loginuser.id
    userLocation = loginuser.location
    if checkadmin:
        usertype = "a"

    pagetitle = 'הוסף מוצר חדש'
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or wherever you want
            return redirect('productslist')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form, 'pagetitle': pagetitle})

def updateproduct(request, pk):
    loginuser = request.user
    checkadmin = loginuser.is_superuser
    usertype = loginuser.user_type
    userID = loginuser.id
    userLocation = loginuser.location
    if checkadmin:
        usertype = "a"

    pagetitle = 'עדכון פרטי מוצר'
    product = products.objects.get(id=pk)
    form = ProductForm(instance=product) # prepopulate the form with an existing band
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            # Redirect to a success page or wherever you want
            return redirect('productslist')
    
    return render(request, 'product_form.html', {'form': form, 'pagetitle': pagetitle})

    

def searchProduct(request):
	myproducts = products.objects.all().values()
	template = loader.get_template('searchProduct.html')

	if request.method == 'POST':
		selected_product_name = request.POST.get('browser', '')
		selected_product = products.objects.filter(product_name=selected_product_name).first()

		context = {
			'myproducts': myproducts,
			'selected_product': selected_product,
			}
	else:
		context = {
		  'myproducts': myproducts,
	  	}
	return HttpResponse(template.render(context, request))

def productslist(request):
    all_products = products.objects.all()
    return render(request, 'products_list.html', {'products': all_products})

@login_required
def userform(request):
    #צריך לשלוח את הסוג משתמש בכל דף כדי להציג את התפריט הנכון לפי משתמש
    loginuser = request.user
    checkadmin = loginuser.is_superuser
    usertype = loginuser.user_type
    userID = loginuser.id
    if checkadmin:
        usertype = "a"
    #
    userObj = User.objects.get(id=userID)

    form = UserDetailsForm(instance=userObj) # prepopulate the form with an existing band
    if usertype == False:
        form.fields['comp_num'].widget = forms.HiddenInput()

    return render(request, 'user_form.html', {'form': form, 'userType': usertype, 'checkAdmin': checkadmin})


@login_required
def recycling_bin(request):
    #צריך לשלוח את הסוג משתמש בכל דף כדי להציג את התפריט הנכון לפי משתמש
    loginuser = request.user
    checkadmin = loginuser.is_superuser
    usertype = loginuser.user_type
    userID = loginuser.id
    userLocation = loginuser.location
    if checkadmin:
        usertype = "a"
    
    recycling_data = usersrecycling.objects.filter(user__location=userLocation)  # ניגשנו לשדה בתוך שדה עם __
    context = {
        
        'recycling_data': recycling_data,
        'userType': usertype,
    }
    return render(request, 'recycling_bin.html', context)

@login_required
def my_authority(request):
    #צריך לשלוח את הסוג משתמש בכל דף כדי להציג את התפריט הנכון לפי משתמש
    loginuser = request.user
    checkadmin = loginuser.is_superuser
    usertype = loginuser.user_type
    userID = loginuser.id
    userLocation = loginuser.location
    if checkadmin:
        usertype = "a"
    
    recycling_data = usersrecycling.objects.filter(user__location=userLocation)  # ניגשנו לשדה בתוך שדה עם __
    context = {
        
        'recycling_data': recycling_data,
        'userType': usertype,
    }
    return render(request, 'my_authority.html', context)

@login_required
def data_recycling(request):
    #צריך לשלוח את הסוג משתמש בכל דף כדי להציג את התפריט הנכון לפי משתמש
    loginuser = request.user
    checkadmin = loginuser.is_superuser
    usertype = loginuser.user_type
    userID = loginuser.id
    userLocation = loginuser.location
    if checkadmin:
        usertype = "a"
    
    recycling_data = usersrecycling.objects.all()  # ניגשנו לשדה בתוך שדה עם __
    context = {
        
        'recycling_data': recycling_data,
    }
    return render(request, 'data_recycling.html', context)

@login_required
def data_user(request):
    #צריך לשלוח את הסוג משתמש בכל דף כדי להציג את התפריט הנכון לפי משתמש
    loginuser = request.user
    checkadmin = loginuser.is_superuser
    usertype = loginuser.user_type
    userID = loginuser.id
    userLocation = loginuser.location
    if checkadmin:
        usertype = "a"
    
    recycling_data = usersrecycling.objects.all()  # ניגשנו לשדה בתוך שדה עם __
    context = {
        
        'recycling_data': recycling_data,
    }
    return render(request, 'data_user.html', context)


@login_required
def userEditform(request):
    #צריך לשלוח את הסוג משתמש בכל דף כדי להציג את התפריט הנכון לפי משתמש
    loginuser = request.user
    checkadmin = loginuser.is_superuser
    usertype = loginuser.user_type
    userID = loginuser.id
    if checkadmin:
        usertype = "a"
    #
    userObj = User.objects.get(id=userID)

    form = UserDetailsEditForm(instance=userObj) # prepopulate the form with an existing band
    if usertype == False:
        form.fields['comp_num'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = UserDetailsEditForm(request.POST, instance=userObj)
        if form.is_valid():
            form.save()
            # Redirect to a success page or wherever you want
            return HttpResponseRedirect("/website/userform/")

    return render(request, 'edit_user_details.html', {'form': form, 'userType': usertype})



@login_required
def userRecyclingform(request):
    #צריך לשלוח את הסוג משתמש בכל דף כדי להציג את התפריט הנכון לפי משתמש
    loginuser = request.user
    checkadmin = loginuser.is_superuser
    usertype = loginuser.user_type
    userID = loginuser.id
    if checkadmin:
        usertype = "a"
    #
    if request.method == 'POST':
        form = UserRecyclingForm(request.POST, request.FILES)
        if form.is_valid():
            user_recycling_instance = form.save(commit=False)
            user_recycling_instance.user = request.user  # Associate the logged-in user with the saved instance
            user_recycling_instance.save()
            messages.success(request, 'Your data has been saved successfully.')  # Display success message
            # Redirect to a success page or wherever you want
            return HttpResponse("Data successfully inserted!")  # Replace 'success_url' with the URL you want to redirect to after form submission
    else:
        form = UserRecyclingForm()
    
    return render(request, 'user_recycling.html', {'form': form, 'userType': usertype})

@login_required
def Userpointform(request):
    #צריך לשלוח את הסוג משתמש בכל דף כדי להציג את התפריט הנכון לפי משתמש
    loginuser = request.user
    checkadmin = loginuser.is_superuser
    usertype = loginuser.user_type
    userID = loginuser.id
    if checkadmin:
        usertype = "a"
    #
    return render(request, 'user_point.html')
