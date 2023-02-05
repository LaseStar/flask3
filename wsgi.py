import os

from blog.app import create_app

app = create_app()


@app.cli.command('init-db')
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    from blog.models.database import db
    db.create_all()
    print('done!')


@app.cli.command("create-admin")
def create_admin():
    """
    Run in your terminal:
    ➜ flask create-admin
    > created admin: <User #1 'admin'>
    """
    from blog.models import User
    from blog.models.database import db

    admin = User(username='admin', is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"

    db.session.add(admin)
    db.session.commit()

    print("created admin", admin)


@app.cli.command('create-users')
def create_users():
    """
    Rin in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """

    from blog.models import User
    from blog.models.database import db

    admin = User(username='admin', is_staff=True)
    james = User(username='james')

    db.session.add(admin)
    db.session.add(james)
    db.session.commit()

    print('done! created users:', admin, james)
