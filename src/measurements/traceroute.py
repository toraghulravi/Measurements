from src.measurement import Measurement
from src.config import Config
from src.utils import Utils

class TraceRoute(Measurement):
    def __init__(self) -> None:
        super().__init__(name="traceroute")

    def run_measurement(self):
        params = Config.TRACEROUTE_PARAMS
        target = Utils.cleanup(params["target"])

        if target == "":
            raise Exception("Invalid HostName!!")

        ip_addr = Utils.get_ip_address(target=target, af=params["af"])
        cmd = " ".join(["trace", "-w", str(params["response_timeout"] // 1000), "-P", params["protocol"], "-f", str(params["first_hop"]), "-m", str(params["max_hops"])])
        Utils.run(["scamper", "-c", cmd, "-i", ip_addr], timeout=120)
