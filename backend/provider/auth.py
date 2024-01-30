from jwt import JWT, jwk_from_pem
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = '3e479e87b45483476712520c7b7910196a268dfb'
ALGORITHM = 'HS256'
EXPIRES_IN_SEC = (60*60*24)

def criar_token_acesso(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(seconds=EXPIRES_IN_SEC)
    
    dados.update({'exp': expiracao})

    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt

def verificar_acesso_token(token: str):
    carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return carga.get('sub')