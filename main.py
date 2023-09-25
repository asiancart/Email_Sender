import smtplib as s

ob = s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("sender@gmail.com","passwordhere")
subject="test python"
body="i love python"
message="subject:{}\n\n{}".format(subject,body)
listadd=["whichemailtosendadd@gmail.com",
         "whichemailtosendadd2@gmail.com"]

ob.sendmail("sender@gmail.com",listadd,message)
print("send mail")
ob.quit()