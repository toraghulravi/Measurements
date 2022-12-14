import dns.resolver

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

    @staticmethod
    def get_ip_address(target, af):
        if Utils.is_hostname(target):
            result = []
            if af == 4:
                result = dns.resolver.resolve(target, "A")
            elif af == 6:
                result = dns.resolver.resolve(target, "AAAA")
            else:
                raise Exception("Unable to resolve hostname!!!")

        if not result:
            raise Exception("No resolved IP addresses")

        ip_addr = result[0].to_text()
        return ip_addr
