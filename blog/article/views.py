from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: {
        'title': 'fist',
        'text': 'fist_fist_fist',
        'author': 1
    },
    2: {
        'title': 'second',
        'text': 'second_second_second',
        'author': 2
    },
    3: {
        'title': 'third',
        'text': 'third_third_third',
        'author': 3
    }
}


@article.route('/')
def article_list():
    return render_template(
        '/articles/list.html',
        articles=ARTICLES,
    )


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article_name = ARTICLES[pk]
    except KeyError:
        # raise NotFound(f'Article id {pk} not fount')
        return redirect('/articles')

    return render_template(
        '/articles/details.html',
        article_name=article_name,
    )
