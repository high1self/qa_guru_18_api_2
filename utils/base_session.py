from requests import Session, Response


class BaseSession(Session):
    def __init__(self, url):
        super(BaseSession, self).__init__()
        self.url = url

    def request(self, method, url, **kwargs) -> Response:
        return super().request(method, self.url + url, **kwargs)