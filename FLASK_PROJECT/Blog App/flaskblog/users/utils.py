import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender = 'lathanhmta@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password , visit the following link:
    {url_for('reset_token', token = token, _external = True)}
    '''
    mail.send(msg)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    #get name picture
    _, f_text = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_text
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    out_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail
    i.save(picture_path)
    return picture_fn