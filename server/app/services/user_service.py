from starlette.requests import Request
from schemas.user_schema import UserSchema, InsertUser, RegisterUser
from utils.crypt import verify_password
from utils.jwt import generate_token
from data_access.user.user_repository import UserRepository, RoleEnum
from sqlalchemy.orm import Session
from utils.jwt import decode_token
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def register_user(request:Request, user: InsertUser)-> UserSchema:
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        user_repo: UserRepository = request.app.repositories.user_repo(session)
        user = user_repo.add(
           user
        )
        return user

def authenticate_user(request:Request, email: str, password:str):
    try:
        with request.app.session_maker() as temp_session:
            session:Session = temp_session
            user_repo:UserRepository = request.app.repositories.user_repo(session)
            user:UserSchema = user_repo.find_one_by_email(email).dict_with_password()
            print(user)
            if not user:
                return False
            if not verify_password(password, user['password']):
                return False
            token = generate_token({'email': user['email'], 'role': RoleEnum(user['role']).value})
            del user['password']
            tempUser = user.copy()
            tempUser.update({"token": token})
            return tempUser
    except Exception as e:
        print(e)

def get_user_by_email(request:Request, email: str)->UserSchema:
    with request.app.session_maker() as temp_session:
        session:Session = temp_session
        user_repo = request.app.repositories.user_repo(session)
        user:UserSchema = user_repo.find_one_by_email(email).dict()
        return user

def on_board(request:Request, user:RegisterUser):
    decoded = decode_token(request.headers['x-token'])
    if decoded['role'] =='Super Admin':
        send_semail(email_to =user.email, name=user.name)
    if decoded['role'] =='Admin':
        print('admin')
    return

def send_semail(email_to: str, name:str):
    email_from = 'prajwaldeepbhandari@gmail.com'
    password = 'vrkpdmrabbeooshh'
    email_message = MIMEMultipart()
    email_message['From'] = email_from
    email_message['To'] = email_to
    email_message['Subject'] = f'Invitaion email to {name}'
    html = '''
    <html>
        <body>
            <h1>Hello, welcome to your our portal!</h1>
        </body>
    </html>
    '''
    email_message.attach(MIMEText(html, "html"))
    email_string = email_message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_from, password)
        server.sendmail(email_from, email_to, email_string)

