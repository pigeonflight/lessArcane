import os, sys

import bottle
from bottle import route, run, template, post,request, response

bottle.debug(True)

# main website stuff

@route('/')
def lessArcane():
  return template('static/index.html')
  
@route('/js/<jsfile>')
def js(jsfile):
  response.content_type = 'application/javascript'
  return template('static/js/%s' % jsfile)

@route('/css/<cssfile>')
def css(cssfile):
  response.content_type = 'text/css'
  return template('static/css/%s' % cssfile)
    




run(host=os.getenv("IP", '0.0.0.0'),port=int(os.getenv("PORT", 8080) ),reloader=True)
