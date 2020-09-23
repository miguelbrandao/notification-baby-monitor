#!/usr/bin/env python3.8
import secrets
import requests
import subprocess

endpoint = "https://api.github.com/notifications"
headers = {"Authorization": "token "+secrets.token,
           "Accept": "application/vnd.github.v3+json"}
params = {"all": "false"}  # only unread notifications

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
        icon = "--icon=/home/miguel/dados/dev/notification-baby-monitor/github_icon_32px.png"
        arguments = ["/usr/bin/notify-send", icon,
                     title, "\n".join(notification_titles)]
        subprocess.Popen(arguments)
    else:
        pass
else:
    print("Request returned code" + raw_response.status_code)
