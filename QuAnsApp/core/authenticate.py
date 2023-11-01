import jwt
from QuAnsApp.settings import SECRET_KEY
import datetime

JWT_ALGORITHM = "HS256"

def authenticate(request):
    req =  request.META.get('HTTP_AUTHORIZATION', None)
    if req != '' and req is not None:
        token = req.split(" ", 1)[1]
        if not token:
            return False
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except:
            return False
        return payload
    else:
        return False
    

def create_access_token(id):
    payload = {
        "user_id": str(id),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=500),
        "iat": datetime.datetime.utcnow(),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')