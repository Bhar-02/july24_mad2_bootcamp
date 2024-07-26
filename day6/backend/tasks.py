from app import celery_app
from celeryContext import ContextTask
from mailer import mail


@celery_app.task(base=ContextTask)
def sum():
    print("Sum function called")
    import time
    time.sleep(10)
    return 1+2


@celery_app.task(base=ContextTask)
def test_db():
    from models import Category
    var1 = Category.query.first()
    print(var1.name)
    return "DB test done"

@celery_app.task(base=ContextTask)
def test_mail(base=ContextTask):
    from flask_mail import Message
    from models import User
    users = User.query.all()
    email_sub = "Test email"
    email_body = "This is a test email"

    for user in users:
        html_body = "<html><body>"
        html_body += "<h1>Hi"
        html_body += f"{user.id}</h1>"
        html_body += f"<p>{user.email}</p>"
        html_body += "</body></html>"
        msg = Message(subject=email_sub, recipients=[user.email])
        msg.body = email_body
        msg.html = html_body
        mail.send(msg)


    return "Mail sent"
