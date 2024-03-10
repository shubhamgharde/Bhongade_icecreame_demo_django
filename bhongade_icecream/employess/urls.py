from django.urls import path
from registration import views
from employess import views

urlpatterns=[
    
    path('save/employee_manage/', views.employee_manage_page, name='employee_manage'),
    path('delete/employee_manage/', views.employee_manage_page, name='employee_manage'), 
    path('list/edit/employee_manage/', views.employee_manage_page, name='employee_manage'),
    path('list/employee_manage/', views.employee_manage_page, name='employee_manage'),
    path('edit/employee_manage/', views.employee_manage_page, name='employee_manage'),
    path('employee_manage/', views.employee_manage_page, name='employee_manage'),

    path('save/', views.save_update_employee_informations, name='save'),
    path('list/', views.show_list_of_employee, name='list'),
    path('edit/<int:eid>', views.fetch_employee_for_edit , name='edit'),
    path('list/edit/<int:eid>', views.fetch_employee_for_edit , name='edit'),
    path('delete/<int:eid>', views.delete_employee_reccord, name='delete'),
    path('list/delete/<int:eid', views.delete_employee_reccord, name='delete'),
    
 

]