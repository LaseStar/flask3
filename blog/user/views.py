from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

USER = {
    1: 'Alice',
    2: 'Jon',
    3: 'Mike'
}

@user.route('/')
def user_list():
    return render_template(
        '/users/list.html',
        users=USER,
    )


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_name = USER[pk]
    except KeyError:
        # raise NotFound(f'User id {pk} not fount')
        return redirect('/users')

    return render_template(
        '/users/details.html',
        user_name=user_name,
    )
