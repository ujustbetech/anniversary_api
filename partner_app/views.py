# from rest_framework import viewsets
# from partner_app.serializers import partnerSerializer
# from partner_app.models import partner


# class partnerViewSet(viewsets.ModelViewSet):
#    queryset = partner.objects.all()
#    serializer_class = partnerSerializer

# class LoginViewSet(viewsets.ModelViewSet):
#    queryset = partner.objects.all()
#    serializer_class = partnerSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from partner_app.models import partner,postimage
from partner_app.serializers import partnerSerializer,postimageSerializer


@api_view(['GET', 'POST'])
def Registration(request):
    if request.method == 'GET':
        # print("hello")
        snippets = partner.objects.all()
        serializer = partnerSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = partnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def partnerlogin(request,pk):
    try:
        partner_data = partner.objects.get(pk=pk)
        print("partner data",partner_data)
    except partner_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = partnerSerializer(partner_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = partnerSerializer(partner_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        print("inside delete")
        partner_data.delete()
        return Response({'message': 'Data was deleted successfully!'},status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def postimg(request):
    if request.method == 'GET':
        snippets = postimage.objects.all()
        serializer = postimageSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = postimageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'DELETE'])
# def imgdata(request,post):
#     try:
#         img_data = postimage.objects.get(id=post)
#         print("partner data",img_data)
#     except img_data.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = partnerSerializer(img_data)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         print("inside delete")
#         img_data.delete()
#         return Response({'message': 'Data was deleted successfully!'},status=status.HTTP_204_NO_CONTENT)
    
