from expense.models import Expenses
from django.contrib.auth import get_user_model
from django.db.models import Sum
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from expense.expensserializer import ExpensiveSerializer
from .adminpermission import Adminonly
from datetime import timedelta
import datetime
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
import pdb
from django.db.models import Sum

User = get_user_model()


class ExpensesUserList(ListAPIView):
    serializer_class = ExpensiveSerializer
    permission_classes = [Adminonly]

    def get(self, request, user_id, *args, **kwargs):

        # users = User.objects.all()
        # expense_list = []

        # for user in users:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'User Not found '}, status=status.HTTP_404_NOT_FOUND)

        expens_total = Expenses.objects.filter(created_by=user).aggregate(total=Sum('amount'))['total']or 0.00
            # expense_list.append({
            #     'user': user.username,
            #     'total_expenses': expens_total
            # })
        return Response({'user': user.username,
                'total_expenses': expens_total,
                'user_id': user.id})

        

class AllUserExpenses(ListAPIView):
    serializer_class = ExpensiveSerializer
    permission_classes = [Adminonly]

    def get(self, request, *args, **kwargs):
        expens_total = Expenses.objects.aggregate(total=Sum('amount'))['total']or 0.00

        return Response({'total expenses': expens_total})


class ExpensUserView(ListAPIView):
    serializer_class = ExpensiveSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = request.user
        todays = timezone.now()
        time_for_last7day = todays - timedelta(days=7)
        last_30_days =     todays - timedelta(days=30)

        last30_days_expenses = Expenses.objects.filter(created_by=user,
        date__gte=last_30_days).values('category__name').annotate(total_amount=Sum('amount'))

        last7_days_expenses = Expenses.objects.filter(created_by=user,
        date__gte=time_for_last7day).values('category__name').annotate(total_amount=Sum('amount'))

        res_data = {
            "expenses for last 7 days": last7_days_expenses,
            "expensive for last 30 days":last7_days_expenses


        }
       
       
        return Response(res_data)
        
        