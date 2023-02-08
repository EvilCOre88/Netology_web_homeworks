from models import User, Session, Advertisement, Token
from errors import HttpError
from app import get_bcrypt
import uuid
import time


bcrypt = get_bcrypt()


def password_auth(session: Session, user_data: dict) -> object:
    user = session.query(User).filter(User.email == user_data['email']).first()
    if not user:
        raise HttpError(404, 'user with such email does not exist')
    if not bcrypt.check_password_hash(user.password.encode(), user_data['password'].encode()):
        raise HttpError(401, 'wrong password')
    print(user)
    return user


def token_auth(session: Session, token: str):
    try:
        token = uuid.UUID(token)
    except (ValueError, TypeError):
        raise HttpError(403, 'incorrect token')
    token = session.query(Token).get(token)
    if not token:
        raise HttpError(403, 'indicated token is not found')
    if time.time() - token.creation_time.timestamp() > 86400:
        raise HttpError(403, 'token has expired, please request new one')
    return token


def owner_token_auth(session: Session, adv_id: int, token: Token) -> object:
    advertisement = session.query(Advertisement).get(adv_id)
    if not advertisement:
        raise HttpError(404, 'advertisement does not exist')
    if advertisement.owner != token.user_id:
        raise HttpError(401, 'advertisements can be deleted only by their owner')
    return advertisement
