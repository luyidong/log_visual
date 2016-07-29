from flask import Flask,request,render_template
app = Flask(__name__)
import MySQLdb as mysql
con = mysql.connect(user='fable',\
                    passwd='fableAdmin',\
                    db='fable_log')
cur = con.cursor()
@app.route('/')
def index():
    table = '<table border="1">'
    cur.execute('select * from fable_log order by value desc limit 20; ')
    for c in cur.fetchall():
        table += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%c
    table +='</table>'
    return table

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000)
