import datetime
import requests
import json
from GA.settings import REDIRECT_URI
from details.models import *


TOKEN_URL = "https://gymkhana.iitb.ac.in/sso/oauth/token/"
USER_DATA_URL = "https://gymkhana.iitb.ac.in/sso/user/api/user/?fields=first_name,last_name,roll_number"





def get_ldap_token(code):
    auth_token = "Basic MTJreXl1YWdOVVpLdlNodE1yTFFidk5CQWE1ZFBVdmVNWnE4aUJiSTptR2NpWW9BWmZCQTJpU0p3S3ZmanVJeVlsNDlOUkZwMm9OUEJ6ekEyazlqTzdnN2RvTWFvakdxYnUxUER0eXJpdzBPZURoek04OUlEVGtIdTc2eDlUN3dQdWdHZ1BBa2J5ZnFoaXpmS0RPTHlJTHY1TVFvZUU1c1E0R3lVcW01aQ=="

    headers = {"Authorization": auth_token}
    body = {}
    body["code"] = code
    body["redirect_uri"] = REDIRECT_URI
    body["grant_type"] = "authorization_code"
    print
    code
    r = requests.post(TOKEN_URL, headers=headers, data=body, verify=False)

    return json.loads(r.content)


def fetch_user_data(user):
    auth_token = "Bearer " + user.access_token
    headers = {"Authorization": auth_token}

    r = requests.get(USER_DATA_URL, headers=headers, verify=False)
    data = json.loads(r.content)
    print
    data
    if User.objects.filter(roll_number=data['roll_number']).exists():
        new_user = User.objects.get(roll_number=data['roll_number'])
        new_user.save()
        user = new_user

    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.roll_number = data['roll_number']

    user.save()
    return user
