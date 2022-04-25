from resources.base_resource import BaseResource

class Brand(BaseResource):
    def get(self):
        return {
            "brandList": [ {
            "brandId": 343,
            "brandName": "Mamaearth"
             }
            ]
        }
