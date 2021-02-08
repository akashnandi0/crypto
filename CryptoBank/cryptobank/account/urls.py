from django.urls import path
from account.views import createAccount, accountList, loginView, balanceEnq, transfer, accountActivity, \
    registerpage,educationplan,businessplan,carplan,homeplan, deposit, withdraw

urlpatterns = [
    path('login', loginView,name="login"),
    path('register', registerpage),
    path('createaccount/',createAccount),
    path("accountlist/",accountList,name="accountlist"),
    path("balance/", balanceEnq, name="balance"),
    path("transfer", transfer, name="transfer"),
    path("history", accountActivity, name="history"),
    path("educationplan",educationplan),
    path("businessplan",businessplan),
    path("carplan",carplan),
    path("homeplan",homeplan),
    path("deposit", deposit, name="deposit"),
    path("withdraw", withdraw, name="withdraw")
    ]