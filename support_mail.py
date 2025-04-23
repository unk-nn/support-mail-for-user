import smtplib
import random
from email.message import EmailMessage

smtp_server = "smtp.gmail.com"
smtp_port = 587
email = "your_email@gmail.com" # email с которой будут отправляться сообщения
auth_code = "aaaa aaaa aaaa aaaa" # специальный код //по типу пароля\\
def sixCode():
    return str(random.randint(1, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + ' ' + str(
        random.randint(1, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

def password_recovery(uemail: str, id_tg: int):
    sc = sixCode()
    # Создаем объект EmailMessage
    em = EmailMessage()
    # Устанавливаем тему письма
    em['Subject'] = "Запрос на восстановление пароля!!!"
    # Оформляем содержимое письма с использованием HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Запрос на восстановление пароля</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          background-color: #f4f4f4;
          text-align: center;
          margin: 0;
          padding: 20px;
        }}
        .container {{
          background-color: #ffffff;
          border-radius: 10px;
          padding: 20px;
          width: 80%;
          max-width: 600px;
          margin: 0 auto;
        }}
        h2 {{
          color: #333333;
        }}
        p {{
          font-size: 18px;
          color: #555555;
        }}
        .warning {{
          color: red;
          font-weight: bold;
        }}
        .signature {{
          font-weight: bold;
          color: #333333;
          margin-top: 20px;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <h2>Ваш код для подтверждения личности:</h2>
        <p style="font-size: 24px; font-weight: bold;">{sc}</p>
        <p class="warning">ВНИМАНИЕ: Не сообщайте этот код никому!</p>
        <p class="signature">С уважением, TonyLink 💜</p>
      </div>
    </body>
    </html>
    """
    # Устанавливаем содержимое письма
    em.add_alternative(html_content, subtype='html')
    # Устанавливаем имя отправителя
    em['From'] = 'TonyLink <' + email + '>'

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, auth_code)

        # Отправляем письмо, преобразовав объект EmailMessage в байты
        smtp.sendmail(email, uemail, em.as_bytes())
        print('Сообщение: Запрос на восстановление доставлено:', id_tg)
        return sc
def email_confirmation(uemail: str, id_tg: int):
    sc1 = sixCode()
    em1 = EmailMessage()
    em1['Subject'] = "Запрос на подтверждения Email!!!"
    html_content1 = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Запрос на подтверждения Email!!!</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          background-color: #f4f4f4;
          text-align: center;
          margin: 0;
          padding: 20px;
        }}
        .container {{
          background-color: #ffffff;
          border-radius: 10px;
          padding: 20px;
          width: 80%;
          max-width: 600px;
          margin: 0 auto;
        }}
        h2 {{
          color: #333333;
        }}
        p {{
          font-size: 18px;
          color: #555555;
        }}
        .warning {{
          color: red;
          font-weight: bold;
        }}
        .signature {{
          font-weight: bold;
          color: #333333;
          margin-top: 20px;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <h2>Ваш код для подтверждения email:</h2>
        <p style="font-size: 24px; font-weight: bold;">{sc1}</p>
        <p class="warning">ВНИМАНИЕ: Не сообщайте этот код никому!</p>
        <p class="signature">С уважением, TonyLink 💜</p>
      </div>
    </body>
    </html>
    """
    em1.add_alternative(html_content1, subtype='html')
    # Устанавливаем имя отправителя
    em1['From'] = 'TonyLink <' + email + '>'

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, auth_code)

        # Отправляем письмо
        smtp.sendmail(email, uemail, em1.as_bytes())
        print('Сообщение: Запрос на подтверждение доставлено:', id_tg)
        return sc1
#password_recovery('user_email@gmail.com', 123456789)