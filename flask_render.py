#!/usr/bin/env python
# -*- coding: utf-8 -


from flask import Flask
from flask import render_template
from flask.ext.assets import Environment, Bundle
from flask.ext.cache import Cache
# from flask import redirect

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
css = Bundle('cardui.css', ' normalize.css',
             'semantic.min.css', 'pace.css', 'style.css')
js = Bundle(
    'semantic.min.js', 'jquery.min.js', 'pace.min.js')

assets.register('css', css)
assets.register('js', js)


@app.errorhandler(404)
def page_not_found(e):
        # return render_template('modal.html'), 404
        return "YOU GOT A 404 --Page Does Not Exist", 404


@cache.cached(timeout=50)
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
    # This can be omitted if using gevent wrapped around gunicorn
