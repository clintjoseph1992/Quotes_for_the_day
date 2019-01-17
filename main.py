#!/usr/bin/python
import unirest
from httplib2 import Http
from json import dumps
import datetime


gc_notification_url=<String: GoogleChatBot API URL Here>
xMashapeKey=<String: X-Mashape-Key here>

def google_chat_notify(gcmsg,notification_url):
    """Send Notification to Google chat rooms"""
    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    try:
        response = http_obj.request(
            uri=notification_url,
            method='POST',
            headers=message_headers,
            body=dumps(gcmsg),
        )
        print (response)
    except Exception,e:
        print ("Not able to post message : "+str(e))




def main():
    try:

        # These code snippets use an open-source library. http://unirest.io/python
        response = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous&count=1",
        headers={
            "X-Mashape-Key": xMashapeKey,
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
            }
        )
    except Exception,e:
        print ("Failed at fetching quotes : " + str(e))

    Quote_of_the_day="Goodmorning Ops :) Have a great " + str(datetime.date.today().strftime("%A")) + "!!!" + "\n\n**Quote for the Day**\n\n" + "\"" + str(response.body[0]['quote']) + "\"" + "\n\n" + "-- " + str(response.body[0]['author'])
    #print (Quote_of_the_day)
    msg={'text':Quote_of_the_day}
    google_chat_notify(msg,gc_notification_url)




if __name__=="__main__":
   main()
