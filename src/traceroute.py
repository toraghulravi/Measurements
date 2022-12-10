import socket
import struct
import time

from config import Config

class TraceRoute:
    def __init__(self, TTL=1, MAX=30) -> None:
        self.TTL = TTL
        self.MAX = MAX
    
    def _icmp_bind(self):
        icmp = socket.socket(socket.AF_INET,socket.SOCK_RAW, socket.IPPROTO_ICMP)
        icmp.bind(("", 33434))
        return icmp
    
    def get_icmp_socket(self):
        icmp = self._icmp_bind()
        return icmp
    
    def _udp_bind(self):
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        udp.setsockopt(0, 4, self.TTL)
        return udp
    
    def get_udp_socket(self):
        udp = self._udp_bind()
        return udp
    
    def get_traceroute(self, hostname: str = Config.HOSTNAME):
        while True:
            start_time = time.time() * 1000
            icmp = self.get_icmp_socket()
            udp = self.get_udp_socket()
            udp.sendto("".encode(),(hostname, 33434))
            try:
                data, router_addr = icmp.recvfrom(1024)
                ICMP_header = data[20:28] 
                type_, code, *_ = struct.unpack('bbHHh', ICMP_header)
                end_time = time.time() * 1000
                if router_addr == ('127.0.0.1', 0) :
                    print(f"* TTL: [{self.TTL}] type: [{type_}] code: [{code}] time: [{end_time - start_time}]")
                else:
                    print(f"{router_addr} TTL: [{self.TTL}] type: [{type_}] code: [{code}] time: [{end_time - start_time}]")
            except Exception as e:
                print(e)
            finally:
                icmp.close()
                udp.close()
            
            self.TTL += 1
            if router_addr[0] == hostname or self.TTL == self.MAX:
                break
    
    def run_measurement(self):
        self.get_traceroute()
