from typing import Optional

class Measurement:
    def __init__(self, name: Optional[str] = None) -> None:
        self._name = name
    
    def run_measurement(self):
        pass

    @property
    def name(self):
        return self._name
