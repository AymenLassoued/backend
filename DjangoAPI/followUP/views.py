from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from followUP.models import OF
from followUP.serializers import OFSerializer
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def fabOrderApi(request,id=0):
    if request.method=='GET':
        fabOr = OF.objects.all()
        of_serializer = OFSerializer(fabOr, many=True)
        return JsonResponse(of_serializer.data, safe=False)

    elif request.method=='POST':
        of_data=JSONParser().parse(request)
        of_serializer = OFSerializer(data=of_data)
        if of_serializer.is_valid():
            of_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        of_data = JSONParser().parse(request)
        faborder=OF.objects.get(RefPr=of_data['RefPr'])
        of_serializer=OFSerializer(faborder,data=of_data)
        if of_serializer.is_valid():
            of_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        faborder=OF.objects.get(RefPr=id)
        faborder.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)





# @csrf_exempt
# def SaveFile(request):
#     file=request.FILES['myFile']
#     file_name = default_storage.save(file.name,file)

#     return JsonResponse(file_name,safe=False)