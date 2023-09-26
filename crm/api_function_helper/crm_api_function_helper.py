from django.db import transaction
import logging
from utils import custom_exceptions as ce
from crm.models import *
from django.core import serializers
import json
from rest_framework.response import Response
from rest_framework import status
from common import messages
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.db.models import F

#Logger for recording all the errors
logger = logging.getLogger('crm')

def fetch_crmled_helper(self, request):

    try:

        #Pagination

        try:
            page = int(request.query_params.get("page",1))
        except Exception as e:
            page = 1

        try:
            limit = int(request.query_params.get("limit",10))
        except Exception as e:
            limit = 30


        # Getting query params

        id = request.query_params.get('crm_id')
        start_page = (page-1)*limit
        end_page = start_page+limit


        if id:
            data_obj = CRMLed.objects.filter(id=id)        
        else:
            data_obj = CRMLed.objects.all().order_by('-id')  # Sort by latest first


        if data_obj.exists():
            list_count = data_obj.count()
            list_data = self.serializer_class(data_obj, many=True).data

            data_obj = data_obj[start_page:end_page]


            if list_data:

                final_data = {
                    "total_count":list_count,
                    "results":list_data
                }
                return Response({
                                'success': True,
                                'status_code': status.HTTP_200_OK,
                                'message': messages.DATA_FOUND,
                                'data': final_data},
                                status = status.HTTP_200_OK)

        else:
             return Response({
                            'success': False,
                            'status_code': status.HTTP_200_OK,
                            'message': messages.DATA_NOT_AVAILABLE,
                            'data': None},
                            status = status.HTTP_200_OK)
            


    except NameError as e:
        logger.error("FETCH CRMLED API FUNCTION HELPER : {}".format(e))
        raise ce.NameErrorCe

    except AttributeError as e:
        logger.error("FETCH CRMLED API FUNCTION HELPER : {}".format(e))
        raise ce.AttributeErrorCe

    except KeyError as e:
        logger.error("FETCH CRMLED API FUNCTION HELPER : {}".format(e))
        raise ce.KeyErrorCe

    except UnboundLocalError as e:
        logger.error("FETCH CRMLED API FUNCTION HELPER : {}".format(e))
        raise ce.UnknownColumnError

    except Exception as e:
        logger.error("FETCH CRMLED API FUNCTION HELPER : {}".format(e))
        raise ce.InternalServerError
    


def get_forecast_amount(self, request):

    try:

        #Get Probablity percentage 
        probability_percent_val = 0

        forecase_amount_dict = {}

        probability_percent = CRMPil.objects.filter(
            is_active=True
        )
        if probability_percent.exists():

            probability_percent_val = probability_percent.last().probability_percent



        # # Filter CRMopp records where closed_on date is null or blank
        filtered_opportunities = CRMOpp.objects.filter(closed_on__isnull=True)

        # Calculate the forecast amount for each opportunity
        filtered_opportunities = filtered_opportunities.annotate(forecast_amount=F('amount') * probability_percent_val)

        # Group by month based on target_date and calculate the sum of forecast amounts
        forecast_by_month = filtered_opportunities.annotate(
            month=TruncMonth('target_date')
        ).values('month').annotate(monthly_forecast=Sum('forecast_amount')).order_by('month')

        # Create a list of forecast values by month
        forecast_list = [(entry['month'].strftime('%b'), entry['monthly_forecast']) for entry in forecast_by_month]

        # Print the forecast values by month
        for month, forecast in forecast_list:
            print(f"{month} {forecast}")

            if month not in forecase_amount_dict:
                forecase_amount_dict[month]=forecast
        
        return Response({
                    'success': True,
                    'status_code': status.HTTP_200_OK,
                    'message': messages.DATA_FOUND,
                    'data': forecase_amount_dict},
                    status = status.HTTP_200_OK)


    except NameError as e:
        logger.error("GET FORECAST AMOUNT API FUNCTION HELPER : {}".format(e))
        raise ce.NameErrorCe

    except AttributeError as e:
        logger.error("GET FORECAST AMOUNT API FUNCTION HELPER : {}".format(e))
        raise ce.AttributeErrorCe

    except KeyError as e:
        logger.error("GET FORECAST AMOUNT API FUNCTION HELPER : {}".format(e))
        raise ce.KeyErrorCe

    except UnboundLocalError as e:
        logger.error("GET FORECAST AMOUNT API FUNCTION HELPER : {}".format(e))
        raise ce.UnknownColumnError

    except Exception as e:
        logger.error("GET FORECAST AMOUNT API FUNCTION HELPER : {}".format(e))
        raise ce.InternalServerError