from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import User, products
from .forms import PrivateSignUpForm, CorpSignUpForm, updateProductForm, createProductForm

def register(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

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
    if request.method == 'POST':
        form = createProductForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or wherever you want
            return render(request, 'addProduct.html', {'form': form, 'success': 'המוצר נוסף בהצלחה!'})
    else:
        form = createProductForm()
    return render(request, 'addProduct.html', {'form': form})

def updateProduct(request, id):
    instance = get_object_or_404(products, id = id)
    if request.method == 'POST':
        form = updateProductForm(request.POST, instance = instance)
        if form.is_valid(): #validation
            form.save()
            # Redirect to a success page or wherever you want
            return render(request, 'updateProduct.html', {'form': form, 'success': 'המוצר עודכן בהצלחה!'})
    else:
        form = updateProductForm(instance = instance)
    return render(request, 'updateProduct.html', {'form': form})
    
      
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

