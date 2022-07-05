# syslog-event-messenger
This script allows you to check for specific syslog events and set alarms that once triggered can send emails to alert you



## usage:

First of all, you need to setup variables in **pymail.json**:

    {
        "mailsto": [
            "RECIPIENT_MAIL_ADDRESS_1",
            "RECIPIENT_MAIL_ADDRESS_2",
            "RECIPIENT_MAIL_ADDRESS_3"
        ],
        "mailsubject": "MAIL_SUBJECT",
        "mailtext": "MAIL_TEXT",
        "maillogin": "USERNAME_TO_ACCESS_EMAIL_SERVER",
        "mailpwd": "PASSWORD_TO_ACCESS_EMAIL_SERVER",
        "mailfrom": "MAIL_FROM_WHICH_SENDING_FROM",
        "mailserver": "MAILSERVER",
        "error_strings": [
            "ERROR_STRING_1",
            "ERROR_STRING_2",
            "ERROR_STRING_3"
        ]

    }

After setting up **pymail.json** you can run **checksshd**, the only needed argument indicates the timespan of the events you want to check:

    ./checksshd "1 week ago"

