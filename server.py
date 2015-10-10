from flask import *
from seaRead import *
app = Flask(__name__)
@app.route('/search', methods=['POST', 'GET'])
def hello_world():
            key=request.args.get('key', '')
            #return render_template('a.html',name=name)
            return read(key)
        
if __name__ == '__main__':
#        app.debug = True
        app.run(host='0.0.0.0',port=8080)
