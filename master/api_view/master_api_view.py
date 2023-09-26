
from rest_framework.views import APIView
from django.db import transaction
import logging
from utils import custom_exceptions as ce
from master.api_function_helper.master_api_function_helper import *
from master.serializers import MASSlmSerializer

#Logger for recording all the errors
logger = logging.getLogger('master')

class MASSlmApiView(APIView):

    serializer_class = MASSlmSerializer

    @transaction.atomic
    def get(self, request):
        try:
            response = fetch_masslm_helper(self, request)
            return response
        except NameError as e:
            logger.error("FETCH MASSlm API VIEW : {}".format( e), exc_info=True, extra={'request': request})
            raise ce.NameErrorCe

        except AttributeError as e:
            logger.error("FETCH MASSlm API VIEW : {}".format( e), exc_info=True, extra={'request': request})
            raise ce.AttributeErrorCe

        except KeyError as e:
            logger.error("FETCH MASSlm API VIEW : {}".format( e), exc_info=True, extra={'request': request})
            raise ce.KeyErrorCe

        except UnboundLocalError as e:
            logger.error("FETCH MASSlm API VIEW : {}".format( e), exc_info=True, extra={'request': request})
            raise ce.UnknownColumnError

        except Exception as e:
            logger.error("FETCH MASSlm API VIEW : {}".format( e), exc_info=True, extra={'request': request})