from src.measurement import Measurement
from src.config import Config
from src.utils import Utils

class Ping(Measurement):
    def __init__(self) -> None:
        super().__init__(name="ping")

    def run_measurement(self):
        params = Config.PING_PARAMS
        target = Utils.cleanup(params["target"])

        if target == "":
            raise Exception("Invalid HostName!!")
        
        ip_addr = Utils.get_ip_address(target, params["af"])
        cmd = " ".join(["ping", "-c", str(params["packets"]), "-i", str(params["packet_interval"]), "-s", str(params["size"])])
        Utils.run(["scamper", "-c", cmd, "-i", ip_addr], timeout=120)
