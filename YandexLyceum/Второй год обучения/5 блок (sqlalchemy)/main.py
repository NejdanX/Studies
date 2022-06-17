from flask import Flask, render_template
from data import db_session
# from data.users import User
from data.news import News
from data.users_task import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private == False)
    return render_template("index.html", news=news)


def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    print(user)
    # app.run(host='127.0.0.1', port=8080, debug=True)


if __name__ == '__main__':
    main()

