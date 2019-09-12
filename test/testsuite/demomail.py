from lib import send_email


"""喊大家吃饭"""
def chifan_mail():
    contents="!!!GOGO吃饭GOGO!!!"
    send_email.send_mail(title="GO吃饭GO",msg=contents)

chifan_mail()