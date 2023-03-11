# from django.shortcuts import render
# from Main.models import Menu, Review, Booking
# from Main.forms import BookingForm

# # Create your views here.
# class MainPage:            
#     def Home(request):
#         reviews = Review.objects.all()
#         menuItems = Menu.objects.all()
#         items = {'menus': menuItems, 
#                 'discountmenus': menuItems[0:2],
#                 'reviews': reviews}
        
#         if request.method == 'POST':
#             form = BookingForm(request.POST)
#             if form.is_valid():
#                 name = form.cleaned_data['name']
#                 phone = form.cleaned_data['phone']
#                 email = form.cleaned_data['email']
#                 date = form.cleaned_data['date']
#                 booking = Booking(name=name, phone=phone, email=email, date=date)
#                 booking.save()
#                 # Redirect to a success page or render a thank you message
                
#         else:
#             form = BookingForm()
        
#         items['form'] = form
        
#         return render(request, 'index.html', items)

    
#     def Menu(request):
#         menuItems = Menu.objects.all()
#         return render(request, 'menu.html', {'menus': menuItems})
    
#     def About(request):
#         return render(request, 'about.html')
    
#     def Book(request):
#         return render(request, 'book.html')
    
from django.shortcuts import render
from django.views import View
from .models import Review, Menu, Booking
from .forms import BookingForm

class MainPage(View):
    
    def get(self, request):
        reviews = Review.objects.all()
        menuItems = Menu.objects.all()
        items = {'menus': menuItems, 
                'discountmenus': menuItems[0:2],
                'reviews': reviews}
        form = BookingForm()
        items['form'] = form
        return render(request, 'index.html', items)
        
    def post(self, request):
        reviews = Review.objects.all()
        menuItems = Menu.objects.all()
        items = {'menus': menuItems, 
                'discountmenus': menuItems[0:2],
                'reviews': reviews}
        
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            booking = Booking(name=name, phone=phone, email=email, date=date)
            booking.save()
            return render(request, 'SubmitForm.html')
            # Redirect to a success page or render a thank you message
        items['form'] = form
        return render(request, 'index.html', items)

class MenuPage(View):
    def get(self, request):
        menuItems = Menu.objects.all()
        return render(request, 'menu.html', {'menus': menuItems})

class SingleMenuPage(View):
    def get(self, request, id):
        menuItem = Menu.objects.get(pk=id)
        return render(request, 'SingleMenu.html', {'menu': menuItem})
    
class AboutPage(View):   
    def get(self, request):
        return render(request, 'about.html')
    
class BookPage(View):
    def get(self, request):
        return render(request, 'book.html')

    def post(self, request):
        reviews = Review.objects.all()
        menuItems = Menu.objects.all()
        items = {'menus': menuItems, 
                'discountmenus': menuItems[0:2],
                'reviews': reviews}
        
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            booking = Booking(name=name, phone=phone, email=email, date=date)
            booking.save()
            return render(request, 'SubmitForm.html')
            # Redirect to a success page or render a thank you message
        items['form'] = form
        return render(request, 'book.html', items)