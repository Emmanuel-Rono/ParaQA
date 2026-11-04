from helium import click, wait_until, Text

class AccountsPage():
    def __init__(self):
        return self

    def check_if_logged_in(self):
        wait_until(Text("Account Overview").exists, timeout_secs=10)
        return Text("Account Overview").exists
