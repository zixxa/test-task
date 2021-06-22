from django.shortcuts import render, redirect
from src.backend.models import Profile
from src.backend.forms import ProfileList

def cash_calculation(cashsender,receivers,check):
    income=check/len(receivers)
    for profile in receivers:
        profile.check=profile.check+income
        profile.save()
    cashsender.check -= check
    cashsender.save()

def get_receivers(innset):
    '''Получение массива профилей-получателей'''
    list_inn=list(set(str(innset).split(sep=' ')))
    receivers=Profile.objects.filter(inn__in=list_inn)
    return receivers

def index(request):
    checkerror=0
    if request.method == 'POST':
        form = ProfileList(request.POST, instance=request.user)
        if form.is_valid():
            form=form.cleaned_data
            user=form['user']
            inn=form['innset']
            check=form['check']
            receivers=get_receivers(inn)
            cashsender=Profile.objects.get(user=user)

            if cashsender.check - check >= 0:
                cash_calculation(cashsender,receivers,check)

            return redirect('index')
    else:
        form = ProfileList()

    content = {
            'form':form,
            'checkerror':checkerror,
            }

    return render(request, 'index.html', content)



