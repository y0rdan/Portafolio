
class SecurityEvent:
    def __init__(self, timestamp, device, command, remote_ip, remote_url):
        self._timestamp = timestamp
        self._device = device
        self._command = command
        self._remote_ip = remote_ip
        self._remote_url = remote_url


    @property
    def timestamp(self):
        return self._timestamp

    @property
    def device(self):
        return self._device

    @property
    def command(self):
        return self._command

    @property
    def remote_ip(self):
        return self._remote_ip

    @property
    def remote_url(self):
        return self._remote_url



