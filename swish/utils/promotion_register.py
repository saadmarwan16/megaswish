import requests
import json


class ProductsPromotionalSignUp():
    def __init__(self, api_key, data_center, list_id):
        self.api_key = api_key
        self.data_center = data_center
        self.list_id = list_id
        self.api_url = f'https://{self.data_center}.api.mailchimp.com/3.0/'
        self.members_endpoint = f'{self.api_url}/lists/{self.list_id}/members'

    def subscribe(self, email):
        data = {
            "email_address": email,
            "status": "subscribed"
        }

        r = requests.post (
            self.members_endpoint,
            auth=("", self.api_key),
            data=json.dumps(data)
        )

        return r.status_code, r.json()