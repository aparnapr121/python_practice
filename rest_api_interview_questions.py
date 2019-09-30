"""
What are sessions in flask

Some web applications use client or the browser as a lightweight cache.
cookies are a method to implement this.
Cookie is some data added by the server in the http header when the server sends a response
Browser stores this and sends this back to the server in the subsequent requests issued, again
by way of http headers. Thus the data contained in the cookie creates an illusion of statefulness.
Upon receiving a request server reads the cookie content to establish the context of the communication
with the client. It then handles the request within that context and updates the cokking before returning the response
to the client.

sessions are a way of implementing cryptographically signed cookies to prevent man in the middle attacks
user can look at the contents of the cookies but not modify it unless they know the secret key for signing
Flask has a config called SERCRET_KEY to set the secret for signing the cookie


"""

from flask import Flask, session, redirect, url_for, escape, request
from flask_restful import reqparse
app=Flask(__name__)
app.secret_key="something_secret"

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return "you are not logged in"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username']=request.form['username']
        return redirect(url_for('index'))
    return '''
            <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
        '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
if __name__=="__main__":
    app.run(port=5000, debug=True)


"""
serialization-convert the state of python object into a form so that it can be transported to a client or it can be persisted
deserilization-convert the serialized object back to it's state
flask has a method called jsonify which would serialize python object. Flask restful handles this implicitly
parse arguments from the request using reqparse module


def put(self, name):
    parser=reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True)
    data=parser.parse_args()
    item = next(filter(lambda x:x['name']==name, items),Nonw)
    if item is None:
        item = {'name':name, 'price': data['price']}
        items.append(item)
        

"""

########################################################################################################################


"""
What is REST architecture

client and server based: Client and server can work independently
Statelessness : Server does not keep any data, each request is treated as a new one, payload is lighter
Interfave Uniformity; Application interface must be uniform and resources to be distributed for users to access

Layered architecture
"""
########################################################################################################################

"""
The RESTAPI has four types of parameters, which are:

Request parameters – These are submitted as JSON parameters present in the request.
Header parameters – These are present in the request header.
Query string parameters – These are provided at the endpoint of the query.
Path parameters – These are provided in the endpoint path.

Can RESTAPI be asynchronous?

Yes, RESTAPI can be asynchronous. However, the asynchronous or synchronous behaviour is dependent on the client who is making the request for the resource.

"""
"""
We have a microservice which exposes REST API that processes some images. One endpoint is responsible for image resizing. It can take more than a minute. How to design and implement a solution that works and makes system robust?
By default gunicorn spawns synchronous workers which are bound to processes. When you make an HTTP request it is queued by gunicorn, waiting to be consumed by one of the workers, make computation and return results. They recommend spawning 2–4 workers per core in the server.
"""