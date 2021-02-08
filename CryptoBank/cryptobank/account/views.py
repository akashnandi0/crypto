from django.shortcuts import render, redirect
import random
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from account.forms import AccountCreateForm, TransferAmountForm, LoginForm, BalanceCheckForm, DepositWithdrawAmountForm
from account.models import CreateAccount, Transferdetails


def loginpage(request):
    template = loader.get_template("loginpage.html")
    return HttpResponse(template.render({}, request))

def educationplan(request):
    template = loader.get_template("educationplans.html")
    return HttpResponse(template.render({}, request))

def businessplan(request):
    template = loader.get_template("businessplans.html")
    return HttpResponse(template.render({}, request))

def carplan(request):
    template = loader.get_template("carplans.html")
    return HttpResponse(template.render({}, request))

def homeplan(request):
    template = loader.get_template("homeplans.html")
    return HttpResponse(template.render({}, request))


def registerpage(request):
    template = loader.get_template("registerpage.html")
    return HttpResponse(template.render({}, request))


def transfer(request):
    form = TransferAmountForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = TransferAmountForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            amount = form.cleaned_data.get("amount")
            accno = form.cleaned_data.get("accno")
            try:
                object = CreateAccount.objects.get(mpin=mpin)
                object1 = CreateAccount.objects.get(accno=accno)
                bal = object.balance - amount
                bal1 = object1.balance + amount
                object.balance = bal
                object1.balance = bal1
                object.save()
                object1.save()

            except Exception:
                context["form"] = form
                return render(request, "transferamount.html", context)

            form.save()

            return redirect("balance")
        else:
            context["form"] = form
            return render(request, "transferamount.html", context)

    return render(request, "transferamount.html", context)

def randomGen():
    # return a 6 digit random number
    return int(random.uniform(100000, 999999))

def randomGen1():
    # return a 6 digit random number
    return int(random.uniform(1000, 9999))

def createAccount(request):
    form = AccountCreateForm()
    context = {}
    context["form"] = form
    if (request.method == 'POST'):
        form = AccountCreateForm(request.POST)
        if form.is_valid():
            personname = form.cleaned_data.get("personname")
            # accno = form.cleaned_data.get("accno")
            accno = randomGen()
            # acctype = form.cleaned_data.get("acctype")
            balance = form.cleaned_data.get("balance")
            phonenumber = form.cleaned_data.get("phonenumber")
            # mpin = form.cleaned_data.get("mpin")
            mpin = randomGen1()

            print(personname, ",", accno, ",", balance, ",", phonenumber, ",", mpin)
            account = CreateAccount(personname=personname, accno=accno, balance=balance,
                                    phonenumber=phonenumber, mpin=mpin)
            account.save()

            return redirect("accountlist")
    return render(request, "createaccount.html", context)


# def createAccount(request):
#     if request.method == 'POST':
#         if request.POST.get('name') and request.POST.get('psw'):
#             post = CreateAccount()
#             post.title = request.POST.get('name')
#             post.content = request.POST.get('psw')
#             post.save()
#
#             return render(request, 'createaccount.html')
#
#     else:
#         return render(request, 'createaccount.html')


def accountList(request):
    account = CreateAccount.objects.all()
    context = {}
    context["account"] = account
    return render(request, "accountlist.html", context)


def loginView(request):
    form=LoginForm()
    context={}
    context["form"]=form

    form=LoginForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            phone=form.cleaned_data.get("phonenumber")
            mpin=form.cleaned_data.get("mpin")

            try:

                object=CreateAccount.objects.get(phonenumber=phone)

                if((object.phonenumber==phone) & (object.mpin==mpin)):
                    print("user exist")

                    return render(request, "accounthome.html")

            except Exception as e:
                print("invalid user")
                context["form"]=form
                return render(request,"login.html",context)

    return render(request, "login.html",context)

def balanceEnq(request):
    form = BalanceCheckForm()
    context = {}
    context["form"] = form
    if (request.method == "POST"):
        form = BalanceCheckForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            try:

                object = CreateAccount.objects.get(mpin=mpin)
                context["balance"] = object.balance

                return render(request, "checkbalance.html", context)
            except Exception as e:
                context["form"] = form
                return render(request, "checkbalance.html", context)

    return render(request, "checkbalance.html", context)


def accountActivity(request):
    form = BalanceCheckForm()
    context = {}
    context["form"] = form
    if (request.method == "POST"):
        form = BalanceCheckForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")

            trans = Transferdetails.objects.filter(mpin=mpin)

            context["transaction"] = trans
            return render(request, "accounthistory.html", context)

    return render(request, "accounthistory.html", context)

def deposit(request):
    form = DepositWithdrawAmountForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = DepositWithdrawAmountForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            amount = form.cleaned_data.get("amount")
            # accno = form.cleaned_data.get("accno")
            try:
                object = CreateAccount.objects.get(mpin=mpin)

                bal = object.balance + amount

                object.balance = bal

                object.save()


            except Exception:
                context["form"] = form
                return render(request, "deposit.html", context)

            form.save()

            return redirect("balance")
        else:
            context["form"] = form
            return render(request, "deposit.html", context)

    return render(request, "deposit.html", context)

def withdraw(request):
    form = DepositWithdrawAmountForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = DepositWithdrawAmountForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            amount = form.cleaned_data.get("amount")
            # accno = form.cleaned_data.get("accno")
            try:
                object = CreateAccount.objects.get(mpin=mpin)

                bal = object.balance - amount

                object.balance = bal

                object.save()


            except Exception:
                context["form"] = form
                return render(request, "withdraw.html", context)

            form.save()

            return redirect("balance")
        else:
            context["form"] = form
            return render(request, "withdraw.html", context)

    return render(request, "withdraw.html", context)

