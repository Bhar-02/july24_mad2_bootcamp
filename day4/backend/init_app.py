from app import create_app


app, _ = create_app()

with app.app_context():
    from models import db, user_datastore

    db.drop_all()

    db.create_all()
    user_datastore.find_or_create_role(name='admin', description='Administrator')
    # new_role = Role(name='admin', description='Administrator')
    # db.session.add(new_role)

    user_datastore.find_or_create_role(name='manager', description='manager')
    user_datastore.find_or_create_role(name='customer', description='customer')

    db.session.commit()

    admin_user = user_datastore.find_user(email="admin@a.com")
    from models import User
    admin__user = User.query.filter_by(email="admin@a.com").first()

    if not admin_user:
        User_admin = user_datastore.create_user(email="admin@a.com", password="admin")
        user_datastore.add_role_to_user(User_admin, 'admin')
    db.session.commit()