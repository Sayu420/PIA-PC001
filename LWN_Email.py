import smtplib
import ssl
import getpass
import mimetypes
from email.message import EmailMessage
from email.utils import make_msgid


def email(dest, subject, msj):
    """Esta función recibe 3 parámetros para el envió de correos electrónicos:
        [dest] = Correo electrónico de quien recibe el mensaje
        [subject] = Asunto del correo
        [msj] = Mensaje que será el cuerpo del correo
        """
    try:
        correo = "testmail420.uanl@gmail.com"
        password = "420420420420"

        destinatario = dest
        asunto = subject
        cuerpo = msj

        mensaje = EmailMessage()
        asparagus_cid = make_msgid()

        mensaje['From'] = correo
        mensaje['To'] = destinatario
        mensaje['Subject'] = asunto
        mensaje.set_content(cuerpo)
        mensaje.add_alternative("""\
        <html>
            <body>
                <p><h1>""" + str(cuerpo) + """</h1><br>
                </p>
            </body>
        </html>
        """.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)as server:
            server.login(correo, password)
            server.sendmail(correo, destinatario, mensaje.as_string())
        print("\nMensaje enviado!")
    except:
        print("No fue posible enviar el correo.")
