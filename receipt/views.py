from celery.result import AsyncResult
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template.loader import render_to_string
from drf_spectacular.utils import extend_schema
from rest_framework import authentication, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ReceiptSerializer
from .tasks import generate_receipt_pdf


class CreateReceiptRequest(APIView):
    """
    View to create task that genereate 10 different pdf copies  of the receipt.
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    @extend_schema(
        request=ReceiptSerializer        
    )
    def post(self, request):
        """
            Return a task id of created task.
        """        
        serializer = ReceiptSerializer(data=request.data)
        if serializer.is_valid():            
            result = generate_receipt_pdf.delay(dict(serializer.validated_data))
            return Response({"task_id" : result.id})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GetStateOfTaskById(APIView):
    """
    View to create task that genereate 10 different pdf copies  of the receipt.
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]    


    def get(self, request, task_id):
        result = AsyncResult(task_id)
        if result.state == "PROGRESS":
            return Response({"state": result.state, "detail": result.info})
        else:
            return Response({"state": result.state})
