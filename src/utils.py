import socket
import subprocess

class Utils:
    @staticmethod
    def execute_commands(commands, timeout=2, stderr=subprocess.STDOUT, shell=False):
        return subprocess.check_output(commands, timeout=timeout, stderr=stderr, shell=shell).decode("utf-8")

    @staticmethod
    def execute_popen(commands, shell=False):
        proc = subprocess.Popen(commands,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=shell)
    
        out, _ = proc.communicate()
        return out.decode("utf-8")

    @staticmethod
    def run(commands, timeout=20, stderr=subprocess.STDOUT, shell=False):
        return subprocess.run(commands, timeout=timeout, stderr=stderr, shell=shell)

    @staticmethod
    def cleanup(target):
        return target.strip().lower()

    @staticmethod
    def is_hostname(target):
        try:
            socket.inet_aton(target)
            return False
        except:
            return True
