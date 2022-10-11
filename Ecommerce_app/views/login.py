from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from Ecommerce_app.models.coustmer import Customer
from django.views import  View
class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')
    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:     #I am taking the password from user and matching with the stored password in database using check_password function
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer']=customer.id
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'
        print(email, password)
        return render(request, 'login.html', {'error': error_message})
def logout(request):
    request.session.clear()
    return redirect('login')
