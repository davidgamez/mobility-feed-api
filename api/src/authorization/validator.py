from http.client import HTTPException
from okta_jwt.jwt import validate_token as validate_locally
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='feeds')
OKTA_ISSUER = 'dev-ovbi33yatgrs8k5i.us.auth0.com'
OKTA_AUDIENCE= 'https://dev-ovbi33yatgrs8k5i.us.auth0.com/api/v2/'
OKTA_CLIENT_ID = 'DiDvq4lzlAtae4IC74cqC7kddNzzhcQc'

def validate(token: str = Depends(oauth2_scheme)):
    try:
        res = validate_locally(
            token,
            OKTA_ISSUER,
            OKTA_AUDIENCE,
            OKTA_CLIENT_ID
        )
        return bool(res)
    except Exception:
        raise HTTPException(status_code=403)    