class Config:
    # Functionalities - comma separated
    # Possible functions: traceroute
    FUNCTIONS: str = "all,traceroute"

    # Traceroute
    TTL: int = 1
    MAX: int = 30
    HOSTNAME: int = "google.com"
