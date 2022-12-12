import socket
from typing import Optional

from src.measurement import Measurement
from src.config import Config
from src.utils import Utils

class TraceRoute(Measurement):
    def __init__(self, name: Optional[str] = None) -> None:
        super().__init__(name)

    def run_measurement(self):
        params = Config.TRACEROUTE_PARAMS
        _, _, ip_addrs = socket.gethostbyname_ex(params["target"])
        first_ip = ip_addrs[0]
        result = Utils.run(["sudo", "scamper", "-i", first_ip], timeout=60)
        print(result)

if __name__ == "__main__":
    a = TraceRoute(name="temp")
    a.run_measurement()
