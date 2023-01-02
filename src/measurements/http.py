import requests
from http.client import HTTPConnection
from src.measurement import Measurement
from src.config import Config
from src.utils import Utils

class HTTP(Measurement):
    def __init__(self) -> None:
        super().__init__(name="http")

    def run_measurement(self):
        # If needs to resolve for IP addresses use
        # https://stackoverflow.com/questions/29995133/python-requests-use-navigate-site-by-servers-ip

        params = Config.HTTP_PARAMS
        target = Utils.cleanup(params["target"])
        headers = requests.utils.default_headers()

        if not (target and params["target"] and params["port"]):
            raise Exception("Invalid URL Parameters!!")

        request_str = Utils.create_request_string(target, params["path"], params["port"])
        if params["user_agent"]:
            headers.update({"User-Agent": params["user_agent"]})

        # Not recommended
        if params["version"] != "1.1":
            HTTPConnection._http_vsn_str = 'HTTP/1.0'

        if params["method"] == "GET":
            response = requests.get(request_str, params=params["query_string"])
        elif params["method"] == "POST":
            response = requests.post(request_str, data=params["query_string"])
        else:
            response = requests.head(request_str)
        print(response.__dict__)
