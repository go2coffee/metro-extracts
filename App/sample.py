from datetime import datetime
from urllib.parse import urljoin

from . import util
from dateutil.tz import tzutc
from flask import Blueprint, render_template, url_for, request, Response

blueprint = Blueprint('Sample', __name__, template_folder='templates')

def apply_sample_blueprint(app, url_prefix):
    '''
    '''
    app.register_blueprint(blueprint, url_prefix=url_prefix)

@blueprint.route('/sample/unknown-unknown')
@util.errors_logged
def sample_unknown_unknown():
    ''' 
    '''
    return render_template('unknown-unknown.html', util=util)

@blueprint.route('/sample/email-body')
@blueprint.route('/sample/email-body.<ext>')
@util.errors_logged
def sample_email_body(ext='html'):
    ''' 
    '''
    args = dict(
        name = 'Null Island',
        link = urljoin(util.get_base_url(request), url_for('ODES.get_extract', extract_id='null')),
        extracts_link = urljoin(util.get_base_url(request), url_for('ODES.get_extracts')),
        created = datetime.now(tz=tzutc())
        )
    
    type = {'html': 'text/html', 'txt': 'text/plain'}.get(ext)

    return Response(render_template('email-body.'+ext, util=util, **args),
                    headers={'Content-type': '{}; charset=utf8'.format(type)})
