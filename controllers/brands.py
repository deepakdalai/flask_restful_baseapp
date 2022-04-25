from resources.base_resource import BaseResource
from flask.globals import request


class Brand(BaseResource):


    def get(self):
        brandId = request.args.get("brandId")
        name = request.args.get("name")

        return {
            "sentBrandId": brandId,
            "sentName": name
        }
