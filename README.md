# Notification Baby Monitor

Notification Baby Monitor is a baby monitor like script for GitHub notifications instead of babies.



GitHub's notifications are very useful, but they can easily missed if one doesn't remember to check them. Notification Baby Monitor solves the problem by taking the notifications to you!

It is a Python script intended to be run as a cron job. I run it hourly, from 9am to 8pm, during weekdays.

The script calls GitHub's API to retrieve unread notifications and displays them using 'notify-send'. It displays the notifications' titles along with its repositories.
