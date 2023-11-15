from flask import Blueprint, render_template

bp = Blueprint('your_view', __name__, url_prefix='/')


@bp.route('/')
def home():
    return render_template('home.html')
