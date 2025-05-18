from django.shortcuts import render, redirect
from .models import Staff
from .forms import StaffForm
from django.contrib.auth.decorators import login_required

@login_required
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'staff/staff_list.html', {'staff': staff})

@login_required
def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff/add_staff.html', {'form': form})
