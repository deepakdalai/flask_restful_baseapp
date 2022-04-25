from resources.base_resource import BaseResource

class Ping(BaseResource):
    def get(self):
        return {
            "status": "OK"
        }
