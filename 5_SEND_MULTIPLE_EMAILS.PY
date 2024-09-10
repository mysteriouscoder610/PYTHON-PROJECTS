import smtplib as s
ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('mail address will be given here','password will be given here')
subject = "Hey welcome to my first mail"
body = "I love python"
msg = "subject:{}\n\n{}".format(subject,body)
listadd = ['mail address where i have to send the mail',
           'second mail address where i have to send the mail']
ob.sendmail('sender mail address will be given here',listadd, msg)
print("send mail")
ob.quit
