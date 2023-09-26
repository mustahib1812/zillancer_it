
from rest_framework.views import APIView
from django.db import transaction
import logging
from utils import custom_exceptions as ce
from crm.api_function_helper.crm_api_function_helper import fetch_crmled_helper,get_forecast_amount
from crm.serializers import CrmLedSerializer

#Logger for recording all the errors
logger = logging.getLogger('crm')

class CrmApiView(APIView):

    serializer_class = CrmLedSerializer

    @transaction.atomic
    def get(self, request):
        try:
            response = fetch_crmled_helper(self, request)
            return response
        except NameError as e:
            logger.error("FETCH CRMLED API VIEW : {}".format( e), exc_info=True, extra={'request': request})
            raise ce.NameErrorCe

        except AttributeError as e:
            logger.error("FETCH CRMLED API VIEW : {}".format( e), exc_info=True, extra={'request': request})
            raise ce.AttributeErrorCe

        except KeyError as e:
            logger.error("FETCH CRMLED API VIEW : {}".format( e), exc_info=True, extra={'request': request})
            raise ce.KeyErrorCe

        except UnboundLocalError as e:
            logger.error("FETCH CRMLED API VIEW : {}".format( e), exc_info=True, extra={'request': request})
            raise ce.UnknownColumnError

        except Exception as e:
            logger.error("FETCH CRMLED API VIEW : {}".format( e), exc_info=True, extra={'request': request})


class CrmOppApiView(APIView):

    @transaction.atomic
    def get(self, request):
        try:
            response = get_forecast_amount(self, request)
            return response
        except NameError as e:
            logger.error("GET FORECAST AMOUNT API VIEW : {}".format( e), exc_info=True, extra={'request': request})
            raise ce.NameErrorCe

        except AttributeError as e:
            logger.error("GET FORECAST AMOUNT API VIEW : {}".format( e), exc_info=True, extra={'request': request})
            raise ce.AttributeErrorCe

        except KeyError as e:
            logger.error("GET FORECAST AMOUNT API VIEW : {}".format( e), exc_info=True, extra={'request': request})
            raise ce.KeyErrorCe

        except UnboundLocalError as e:
            logger.error("GET FORECAST AMOUNT API VIEW : {}".format( e), exc_info=True, extra={'request': request})
            raise ce.UnknownColumnError

        except Exception as e:
            logger.error("GET FORECAST AMOUNT API VIEW : {}".format( e), exc_info=True, extra={'request': request})