##import smtplib, ssl
##
##port = 465  # For SSL
##password = input("Type your password and press enter: ")
##
### Create a secure SSL context
##context = ssl.create_default_context()
##
##with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
##    server.login("imjacksdad@gmail.com", password)
##    # TODO: Send email here


import smtplib
import email.message
import email.utils


def send_email(send_from, send_to):

    msg = email.message.Message()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Subject'] = "Python E-mail Subject - File Found"
    msg.add_header('Content-Type', 'text')
    msg.set_payload("I have found the CWCEXPORT.FIL file on the Compuweigh FTP site.")

    smtp_obj = smtplib.SMTP("smtpapp.gavilon.com")
    smtp_obj.sendmail(msg['From'], [msg['To']], msg.as_string())
    smtp_obj.quit()

#send_email("eric.carstensen@gavilon.com", "imjacksdad@gmail.com,")
