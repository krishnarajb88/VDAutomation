import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.text import MIMEText

fromaddr = "cauto@contus.in"
toaddr = "@contus.in"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python_Selenium_Magento2_Web_FF45_Automation_Report_20171215_19_36_47.html"

body = "Hi Team, \n\n Please find the automation report of Magento Web in Firefox Browser \n\n Modules Covered: \n 1. Signin \n 2. Add Product \n 3. Add Customer \n 4. Admin Settings \n 5. Notifications \n 6. Add New Store \n \n Download view Magento2_TestReport_20171213_21_03_05.html file"

msg.attach(MIMEText(body, 'plain'))

filename = "Magento2_TestReport_20171215_19_36_47.html"
attachment = open("/home/user/PycharmProjects/magento2/Magento2_TestReport_20171215_19_36_47.html", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "contusauto123")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()