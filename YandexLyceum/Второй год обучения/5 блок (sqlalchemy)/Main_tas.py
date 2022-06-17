from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users_task import User
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    # 1 query
    for user in db_sess.query(User).filter(User.address.like('%1')):
        print(user)

    # 2 query
    for user in db_sess.query(User).filter(User.address.like('%1'), User.speciality.notilike('%engineer%'),
                                           User.position.notilike('%engineer%')):
        print(user.id)

    # 3 query
    for user in db_sess.query(User).filter(User.address.like('%1')):
        print(user)
    app.run(host='127.0.0.1', port=8080, debug=True)


if __name__ == '__main__':
    main()

