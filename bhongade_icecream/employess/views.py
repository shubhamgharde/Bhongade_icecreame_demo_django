from django.shortcuts import render
from employess.models import Employee

def employee_manage_page(request):
    return render(request, template_name='employee_manage.html')

def save_update_employee_informations(req):
    message = ''
    if req.method == 'POST':
        formdata = req.POST

        eid = formdata.get('id')
        emp = Employee.objects.filter(id=eid).first()

        if formdata:
            if not emp:
                emp=Employee(first_name = formdata.get('first_name'),
                             last_name = formdata.get('last_name'),
                             age = formdata.get('age'),
                             email = formdata.get('email'),
                             mobile_no = formdata.get('mobile_No'),
                             address = formdata.get('address'),
                             total = formdata.get('total'),
                             paid = formdata.get('paid'),
                             balance = formdata.get('balance'))

                # emp=Employee(last_name = formdata.get('last_name'))
                # emp=Employee(age = formdata.get('age'))
                # emp=Employee(email = formdata.get('email'))
                # emp=Employee(mobile_no = formdata.get('mmobile_no'))
                # emp=Employee(address = formdata.get('address'))
                # emp=Employee(total = formdata.get('total'))
                # emp=Employee(paid = formdata.get('paid'))
                # emp=Employee(balance = formdata.get('balance'))

                if int(eid):
                    emp.id = eid

                emp.save()
                message = 'Employee Record Saved...!'
            
            else:
                emp.first_name = formdata.get('first_name')
                emp.last_name = formdata.get('last_name')
                emp.age = formdata.get('age')
                emp.email = formdata.get('email')
                emp.mobile_no = formdata.get('mobile_no')
                emp.address = formdata.get('address')
                emp.total = formdata.get('total')
                emp.paid = formdata.get('paid')
                emp.balance = formdata.get('balance')
                emp.save()
                message = 'Employee Record Updated...!'

    return render(req, template_name='add_employee.html',
                  context={"result":message, 
                           'employee': Employee(first_name='',last_name='',age=0,email='',
                                               mobile_no='',address='',total='0.0',paid='0.0',
                                               balance='0.0')}) 


def fetch_employee_for_edit(request, eid):
    employee = Employee.objects.get(id=eid)
    return render(request, template_name='add_employee.html',
                  context={"employee":employee})


def delete_employee_reccord(req, eid):
    emp = Employee.objects.get(id=eid)
    emp.delete()

    emp_list = Employee.objects.all()
    return render(req, template_name='employee_list.html',
                  context={"employee_list": emp_list})


def show_list_of_employee(req):
    emp_list = Employee.objects.all()
    return render(req,template_name='employee_list.html',
                  context={"employee_list": emp_list})


                
