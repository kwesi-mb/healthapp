from django.shortcuts import render 
from .models import medicalRecord 

# Create your views here.
def statistics(request):
    eb_no = medicalRecord.objects.filter(category='Ebola').count()
    eb_no = int(eb_no)

    co_no = medicalRecord.objects.filter(category='COVID').count()
    co_no = int(co_no)

    ent_no = medicalRecord.objects.filter(category='ENT').count()
    ent_no = int(ent_no)

    hiv_no = medicalRecord.objects.filter(category='HIV').count()
    hiv_no = int(hiv_no)

    mal_no = medicalRecord.objects.filter(category='Malaria').count()
    mal_no = int(mal_no)

    users_no = medicalRecord.objects.filer(created_by=True).count()
    users_no = int(users_no)


    
    category_list = ['eb_no','co_no', 'ent_no', 'hiv_no', 'mal_no']
    total_users = ['users_no']
    context = {'category_list' : category_list, 'total_users': total_users}
    return render(request, 'medicalRecords/statistics.html', context)