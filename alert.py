import requests

def alert():
     
    url = "https://www.fast2sms.com/dev/bulk"
     
    payload = "sender_id=FSTSMS&message=Alert!!! Please refer to camera0&language=english&route=p&numbers=8839814848"
    headers = {
     'authorization': "WVjhBbLnsc4TFXNxrRvl5eo3u8UQKMq67wIZz0yPHt1ADG2ECmJRAlsSIkQM3F1CY9q7NOyhn64juXLH",
     'Content-Type': "application/x-www-form-urlencoded",
     'Cache-Control': "no-cache",
     }
     
    response = requests.request("POST", url, data=payload, headers=headers)
     
    print(response.text)


if __name__ == '__main__':
   alert()