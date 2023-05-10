from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

@app.route('/index')
def index():
    birds = ["Great Blue Heron", "Laughing Gull", "Sandwich Tern"]

    return render_template("index.html", \
                           title="This is title from def index()", \
                           data_list=birds)

@app.route('/add/user', methods=["GET", "POST"])
def add_user():
    # if we are not getting data from user
    if request.method == "GET":
        return render_template("add_user.html")

    username = request.form.get('user')
    email = request.form.get('email')
    password = request.form.get('psw')
    mobile = request.form.get('mobile')
    print(username, email, mobile, password)

    # connect MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="348432", charset='utf8',
                           db="web_intro")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # send
    sqlStr = "insert into SQL_import_add_user(user, email, password, mobile) value(%(user)s, %(email)s, %(psw)s, %(mobile)s)"
    cursor.execute(sqlStr, {
        "user": username,
        "email": email,
        "psw": password,
        "mobile": mobile
    })
    conn.commit()

    # close
    cursor.close()
    conn.close()

    return "success"

@app.route('/show/user')
def show_user():
    import pymysql

    # connect MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="348432", charset='utf8',
                           db="web_intro")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # send
    sqlStr = "SELECT * FROM SQL_import_add_user"
    cursor.execute(sqlStr)
    data_list = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('show_user.html', data_list=data_list)

if __name__ == '__main__':
    app.run()