from flask_restful import Resource
from datetime import datetime, date
from decimal import Decimal


def sanitize_date(data):
    if isinstance(data, dict):
        for k, v in data.items():
            data[k] = sanitize_date(data[k])
    elif isinstance(data, list):
        data = [sanitize_date(k) for k in data]
    elif isinstance(data, datetime):
        data = datetime.strftime(data, "%Y-%m-%dT%H:%M:%SZ")
    elif isinstance(data, Decimal):
        data = float(data)
    elif isinstance(data, date):
        data = datetime.strftime(data, "%Y-%m-%d")
    return data


def format_response(func):
    
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)

        if isinstance(response, tuple):
            (data, http_status, headers) = response
        else:
            (data, http_status, headers) = response, 200, {}

        data = sanitize_date(data)        
        return (data, http_status, headers)

    return wrapper


class BaseResource(Resource):
    method_decorators = [format_response]

    def options(self, *args, **kwargs):
        return {"status": "OPTIONS OK"}

