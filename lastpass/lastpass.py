""" Lastpass python interface

"""
import subprocess
import os

lastpass_command = 'lpass'

def login(username):
    proc = subprocess.Popen([lastpass_command, 'login', username], 
                            stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    proc.wait()
    return proc.returncode == 0

def logout():
    proc = subprocess.Popen([lastpass_command, 'logout', '-f'], 
                            stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    proc.wait()
    return proc.returncode == 0

def is_auth():
    filename = os.path.join(os.path.expanduser('~'), '.lpass', 'username')
    if os.path.isfile(filename):
        return True
    return False

def is_account(name):
    proc = subprocess.Popen([lastpass_command, 'show', name], 
                                stdout=subprocess.PIPE, 
                                stdin=subprocess.PIPE)
    proc.wait()
    return proc.returncode == 0

class Account:
    """ Created only for existing accounts
    
    """
    def __init__(self, name):
        if not is_auth():
            raise Exception('must login prior to searching accounts')

        if not is_account(name):
            raise Exception('not valid account name')

        self._name = name

    @property
    def name(self):
        return self._get_attribute('name')

    @name.setter
    def name(self, value):
        self._set_attribute('name', value)

    @property
    def username(self):
        return self._get_attribute('username')

    @username.setter
    def username(self, value):
        self._set_attribute('username', value)

    @property
    def password(self):
        return self._get_attribute('pass')

    @password.setter
    def password(self, value):
        self._set_attribute('pass', value)
        
    @property
    def notes(self):
        return self._get_attribute('notes')

    @notes.setter
    def notes(self, value):
        self._set_attribute('notes', value)

    @property
    def id(self):
        return self._get_attribute('id')

    @property
    def url(self):
        return self._get_attribute('url')

    @url.setter
    def url(self, value):
        self._set_attribute('url', value)

    def _get_attribute(self, attr):
        proc = subprocess.Popen([lastpass_command, 'show', self._name, '--' + attr], 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE)
        proc.wait()
        return proc.stdout.read().decode('utf-8')[:-1]

    def _set_attribute(self, attr, value):
        proc = subprocess.Popen([lastpass_command, 'edit', '--non-interactive', self._name, '--' + attr],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE)
        proc.communicate(input=value.encode())
        return proc.returncode == 0


