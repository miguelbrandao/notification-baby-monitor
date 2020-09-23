# Notification Baby Monitor

Notification Baby Monitor is a baby monitor like script for GitHub notifications instead of babies.



GitHub's notifications are very useful, but they can easily missed if one doesn't remember to check them. Notification Baby Monitor solves the problem by taking the notifications to you!

It is a Python script intended to be run as a cron job. I run it hourly, from 9am to 8pm, during weekdays.

The script calls GitHub's API to retrieve unread notifications and displays them using 'notify-send'. It displays the notifications' titles along with its repositories.


### Setting up the Cron job

Here is an example crontab entry:

`0 9-20 * * 1-5 export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus && python /home/miguel/dados/dev/notification-baby-monitor/main.py`

This runs the script hourly, from 9am to 8pm, during weekdays.

The `export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus` bit is necessary because `notify-send` needs this variable. This works for my system (Manjaro i3) but your mileage may vary; you may need to tweak the exported variables.
