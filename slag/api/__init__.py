
from flask import Blueprint, url_for, g, request, session

from .cpu import get_cpu

__all__ = ['bp_api', 'cpu']

bp_api = Blueprint('api', __name__, url_prefix='/api')

@bp_api.route('/cpu', methods=('GET', 'POST'))
def cpu():
    return get_cpu()
