from django.shortcuts import render
from django.core.serializers import serialize

from .models import TodoApp
from django.http import JsonResponse
import json
# Create your views here.







def getRecords(request):
    if request.method == 'GET':
            try:
                #records = list(TodoApp.objects.all().values_list('id','title','created_date'))

                result = TodoApp.objects.all().order_by('-id').values('id','title','created_date')
                records= list(result.values())
                return JsonResponse({'message': 'Data Fetch SuccessFully','flag': 'success','value':records})

            except Exception as e:
                return JsonResponse({'message': f'Data Fetch Failed: {str(e)}', 'flag': 'fail','value':[]})

    else:
        return JsonResponse({'error': 'Invalid request method','flag':'fail','value':[]}, status=400) 

def home(request):
    return render(request,'home.html')


def addFormData(request):
    if request.method == 'POST':
        getTitle = request.POST.get('title', '')  # Assuming 'title' is the key for the POST data
        if getTitle!='':
            try:
                TodoApp.objects.create(title=getTitle)
                return JsonResponse({'message': 'Data Inserted successfully', 'flag': 'success'})
            except Exception as e:
                return JsonResponse({'message': f'Data Insertion Failed: {str(e)}', 'flag': 'fail'})
        else:
            return JsonResponse({'error': 'Value noit Exist','flag':'fail'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method','flag':'fail'}, status=400)
    




def deleteData(request):
    if request.method == 'POST':
        id = request.POST.get('id', '')  # Assuming 'title' is the key for the POST data
        if id!='':
            try:
                # Assuming you want to delete an object with a specific ID

                TodoApp.objects.get(pk=id).delete()
                return JsonResponse({'message': 'Data Deleted successfully', 'flag': 'success'})
            except Exception as e:
                return JsonResponse({'message': f'Data Deletion Failed: {str(e)}', 'flag': 'fail'})
        else:
            return JsonResponse({'error': 'Value not Exist','flag':'fail'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method','flag':'fail'}, status=400)
    