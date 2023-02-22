"""A3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views
from banks import views as bank_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/register/", account_views.RegisterFormView.as_view(), name="register"),
    path("accounts/login/", account_views.LoginView.as_view(), name='login'),
    path("accounts/logout/", account_views.logout_view, name='logout'),
    path("accounts/profile/view/", account_views.profile_view, name='profile_view'),
    path("accounts/profile/edit/", account_views.ProfileEditFormView.as_view(), name='profile_edit'),
    path("banks/add/", bank_views.BankAddFormView.as_view(), name='bank_add'),
    path("banks/<int:bank_id>/branches/add/", bank_views.BranchAddFormView.as_view(), name='branch_add'),
    path("banks/all/", bank_views.BankListView.as_view(), name='bank_list'),
    path("banks/<int:bank_id>/details/", bank_views.BankDetailView.as_view(), name='bank_detail'),
    path("banks/branch/<int:branch_id>/details/", bank_views.branch_detail_view, name='branch_detail'),
    path("banks/<int:bank_id>/branches/all/", bank_views.branch_all_view, name='branch_detail'),
]
