from django.db import transaction
import logging
from utils import custom_exceptions as ce
from master.models import *
import json
from rest_framework.response import Response
from rest_framework import status
from common import messages

#Logger for recording all the errors
logger = logging.getLogger('master')

def fetch_masslm_helper(self, request):

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
            data_obj = MASSlm.objects.filter(id=id)        
        else:
            data_obj = MASSlm.objects.all().order_by('-id')  # Sort by latest first


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
        logger.error("FETCH MASSlm API FUNCTION HELPER : {}".format(e))
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