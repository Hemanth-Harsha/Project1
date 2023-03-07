import smtplib
s = smtplib.SMTP('smtp@gmail.com', 587)
s.starttls()
s.login("hemanthkumar.edcs@gmail.com", "wjiulhegwdlbagdk")
message = "hi"
s.sendmail("hemanthkumar.edcs@gmail.com", "bindushreesn8@gmail.com", message)
s.quit()
