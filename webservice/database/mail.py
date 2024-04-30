import smtplib

def mail(username):
    email="garvkumar059@gmail.com"
    rec="garvkumar68@gmail.com"

    subject="alert"
    msg="someone trying to get unauth access in account: "+username
    txt=f"subject:{subject}\n\n{msg}"
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,"ummfddsecaqclwcp")
    server.sendmail(email,rec,txt)
    print("done")
                        