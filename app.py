from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# SMTP服务器配置
app.config.update(
    MAIL_SERVER='smtp.qq.com',
    MAIL_PORT='587',
    MAIL_USE_TLS=True,
    MAIL_USERNAME='726616825@qq.com',
    MAIL_PASSWORD='' #此处为qq校验码
)

mail = Mail(app)


@app.route('/')
def index():
    msg = Message(subject='来自flask的邮件', sender='726616825@qq.com', recipients=['993109652@qq.com'])
    msg.body = '123456'
    mail.send(msg)
    return '<h1>邮件发送成功</h1>'


if __name__ == '__main__':
    app.run(debug=True)