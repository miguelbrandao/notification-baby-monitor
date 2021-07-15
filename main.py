#!/usr/bin/env python3.8
import secrets
import requests
import subprocess

endpoint = "https://api.github.com/notifications"
headers = {"Authorization": "token "+secrets.token,
           "Accept": "application/vnd.github.v3+json"}
params = {"all": "false"}  # only unread notifications

icon = "--icon=/home/miguel/dev/notification-baby-monitor/github_icon_32px.png"
expire = "--expire-time=20000"

raw_response = requests.get(endpoint, headers=headers, params=params)

if raw_response.status_code == requests.codes.ok:
    response = raw_response.json()
    n_notifications = len(response)
    notification_titles = []
    if n_notifications > 0:
        for notification in response:
            notification_titles.append(
                "  • [" + notification["repository"]["name"] + "] " + notification["subject"]["title"])
        title = "There are " + str(n_notifications) + " new notifications:"
        arguments = ["/usr/bin/notify-send", expire, icon,
                     title, "\n".join(notification_titles)]
        subprocess.Popen(arguments)
    else:
        arguments = ["/usr/bin/notify-send", expire, icon, "Everything clear!"]
        subprocess.Popen(arguments)
else:
    print("Request returned code" + raw_response.status_code)
