from app import app
from app import db
from app.model import Info, Quest, Otziv
from app import mail
from flask import request
from flask import jsonify
from flask_mail import Message
from flask_httpauth import HTTPBasicAuth
from flask_httpauth import HTTPTokenAuth


basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


def send_mail(subj, type_mes, name, text=None, phone=None, email=None):
    """
    :param subj: тема письма
    :param text: текст письма
    :param phone: телефон
    :param email: емаил
    :param type: тип ответа(1 - обратная связь)
    :param name: имя к кому обращаться
    :return:
    """
    if type_mes == 1:
        if email:
            text = """Новая заявка на обратную связь от {2}
            Номер телефона - {0};
            Email - {1}""".format(phone, email, name)
        else:
            text = """Новая заявка на обратную связь от {1}
                        Номер телефона - {0};
                        Email - {1}""".format(phone, name)
    else:
        text = """Новый вопрос от {0}:
            "{1}"
            Email - {2}""".format(name, text, email)
    msg = Message(subj, recipients=['bagration1998@gmail.com'])
    msg.body = text
    mail.send(msg)
    return True


@basic_auth.verify_password
def verify_password(username, password):
    f = False
    if username == "admin" and password == "admin":
        f = True
    return f


@app.route('/token', methods=['GET'])
@basic_auth.login_required
def get_token():
    token = 'kimetottokendlyatebya'
    return jsonify({'token': token})


@token_auth.verify_token
def verify_token(token):
    if token == 'kimetottokendlyatebya':
        return True


@app.route('/', methods=['GET'])
def qwe():
    return "hello"


@app.route('/api/new', methods=['POST'])
def new():
    try:
        r = request.json
        if r['email']:
            new_info = Info(name=r['name'], phone=r['phone'], email=r['email'])
        else:
            new_info = Info(name=r['name'], phone=r['phone'])
        db.session.add(new_info)
        db.session.commit()
        send_mail(subj="Новая заявка",
                  phone=r['phone'],
                  email=r['email'],
                  type_mes=1,
                  name=r['name'])
        return jsonify({"status": "OK"})
    except Exception as e:
        print(e)
        return jsonify({"status": "error",
                        "error": str(e)})


@app.route('/api/new_quest', methods=['POST'])
def new_quest():
    try:
        r = request.json
        new_info = Quest(name=r['name'], email=r['email'], text=r['text'])
        db.session.add(new_info)
        db.session.commit()
        send_mail(subj="Новый вопрос",
                  text=r['text'],
                  email=r['email'],
                  type_mes=2,
                  name=r['name'])
        return jsonify({"status": "OK"})
    except Exception as e:
        return jsonify({"status": "error",
                        "error": str(e)})


@app.route('/api/otzivi', methods=['POST'])
def otz():
    r = request.json
    type_otz = r['type_otz']
    if type_otz == 'all':
        otz = Otziv.query.all()
    if type_otz == 'people':
        otz = Otziv.query.filter_by(type_otz=False).all()
    if type_otz == 'company':
        otz = Otziv.query.filter_by(type_otz=True).all()
    otvet = []
    for i in otz:
        otvet.append({
            'id': i.id,
            'name': i.name,
            'text': i.text,
            'file': i.name_pdf,
            'img': i.name_img
        })
    return jsonify({"result": otvet})


@app.route('/api/izm_otzivi', methods=['POST'])
def otz_izm():
    r = request.json
    try:
        if r['type_com'] == 'INSERT':
            otz = Otziv(name=r['name'], text=r['text'],
                        name_pdf=r['name_pdf'], name_img=r['name_img'],
                        type_otz=r['type_otz'])
            db.session.add(otz)
            db.session.commit()
        return jsonify({"status": "OK"})
    except Exception as e:
        print(e)
        return jsonify({"status": "error",
                        "error": str(e)})


@app.route('/api/del_otzivi', methods=['DELETE'])
@token_auth.login_required
def del_otz():
    try:
        r = request.json
        otz = Otziv.query.filter_by(id=r['id']).first()
        db.session.delete(otz)
        db.session.commit()
        return jsonify({"status": "OK"})
    except Exception as e:
        print(e)
        return jsonify({"status": "error",
                    "error": str(e)})
