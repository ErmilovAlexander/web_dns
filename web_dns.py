from flask import Flask, render_template, flash, request, url_for, redirect
from werkzeug.datastructures import MultiDict
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import get_dns
import config_parse as CONF
# print (PATH_TO_DBDNS)
app = Flask(__name__)
app.config.from_object('config')
class ReusableForm(Form):
    # name = TextField('DNS:', validators=[validators.Required()])
    # address = TextField('Adress:', validators=[validators.Required()])
    name = TextField('DNS:')
    address = TextField('Adress:')

    def reset(self):
        blankData = MultiDict([('csrf', self.csrf_token())])
        self.process(blankData)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = ReusableForm(request.form)
    # print (get_dns.PATH_TO_DBDNS)
    form.validate()
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        print (request.form.get('name'))
        print(request.form.get('address'))
        if form.validate():
        #     request.
            form.reset()
        # if form.validate_on_submit():
        #     pass
        if len(name) != 0 or len(address) != 0:
            get_dns.add_dns(name=name, address=address)
            print("Name {}".format(name))
            print("Address {}".format(address))
    form.name.data=''
    form.address.data=''
    data = render_template('show.html', message=get_dns.find(),form=form)
    return (data)

@app.errorhandler(404)
def error_404(e):
    data = render_template('error.html', message = 'Not found!')
    return (data, 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5200)
