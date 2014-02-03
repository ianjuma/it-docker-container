#!/usr/bin/env python
# -*- coding: utf-8 -


from flask import Flask
from flask import render_template
from flask.ext.assets import Environment, Bundle
from flask.ext.cache import Cache
# Caching implemented is Caching of Just Views --Database
# from flask import redirect
# from flask.ext.sqlalchemy import SQLAlchemy
# from flask import session
# from flask_oauth import OAuth

"""
RestLess -> JSON -> Oauth2 -> API
Boto - ss3 -EC2 - Heroku - Dotcloud - Redis + Storage instances
Redis in caching --Memcache
MySQL as DB -with redis-cache
Managing Sessions --Google API
UI/UX --perfect + easy
Android APP
MongoDB --free from caching --oauth --google USIU domains --emails
wjuma@students.usiu.ac.ke
Mobile view optimizations --JQuery Mobile -> JQuery Mobile
Managing sessions + logins google API --free from sessions
libs + html5 biolerplate + UI
Security -- domain name + product + about -- contact us -- developers -- Terms and Conditions
HTTPS --NGINX --gevent + gunicorn + meinheld + uwsgi + double layer __>-->
encryption for login + some pages or all

Daemonize gunicorn+uWSGI -Managing sessions
With mongoDB no need to cache -> in-memory DB

Redis cache -> Memcache -> Load balancing/NGINX --Haproxy??
SQUID Cache --httpd headers + http requests -> SQUID on its own server
Database cache on same server
"""


app = Flask(__name__)
cache = Cache(app, with_jinja2_ext=True, config={'CACHE_TYPE': 'RedisCache'})
cache.config = {'CACHE_REDIS_PASSWORD': ''}
cache.config = {'CACHE_REDIS_HOST': '127.0.0.1'}
cache.config = {'CACHE_REDIS_PORT': '6379'}
cache.config = {'CACHE_DEFAULT_TIMEOUT': '5'}


# app.config.from_pyfile(flask-config.cfg) -- import Config
assets = Environment(app)
css = Bundle('bootstrap.css', ' bootstrap.min.css',
             'bootstrap-responsive.css', 'bootstrap-responsive.min.css')
js = Bundle(
    'bootstrap.js', 'bootstrap.min.js', 'jquery.js', 'bootstrap-typeahead.js',
    'bootstrap-carousel.js', 'bootstrap-collapse.js', 'bootstrap-button.js',
    'bootstrap-popover.js', 'bootstrap-tooltip.js', 'bootstrap-tab.js',
    'bootstrap-scrollspy', 'bootstrap-dropdown.js', 'bootstrap-modal.js', 'bootstrap-alert.js',
    'bootstrap-transition.js')

assets.register('css', css)
assets.register('js', js)


@app.errorhandler(404)
def page_not_found(e):
        # return render_template('modal.html'), 404
        return "YOU GOT A 404 --Page Does Not Exist", 404


@cache.cached(timeout=50)
@app.route('/')
def index():
    return render_template('bootstrap.html')


@cache.cached(timeout=50, key_prefix='all_comments')
@app.route('/form')
def form():
    return render_template('form.html')


@cache.cached(timeout=50)
@app.route('/footer')
def footer():
    return render_template('footer.html')


@cache.cached(timeout=5000)
@app.route('/modal')
def modal():
    return render_template('modal.html')


@cache.cached(timeout=50)
@app.route('/login')
def login(name=None):
    return render_template('bootstrap.html')


if __name__ == '__main__':
    import newrelic.agent
    newrelic.agent.initialize('newrelic.ini')
    app.run(port=8000, debug=True, host='0.0.0.0')
    # This can be omitted if using gevent wrapped around gunicorn
