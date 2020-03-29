import logging
import random
import uuid
from django_gcp_log_groups import GCPLoggingMiddleware
LOGGER = logging.getLogger(__name__)

print("---")
print(id(LOGGER))
print("---")

nouns = ("puppy", "car", "rabbit", "girl", "monkey")
verbs = ("runs", "pounces", "jumps", "drives", "barfs", "cowers")
adv = ("crazily", "dutifully", "foolishly", "merrily", "occasionally")
adj = ("adorable", "clueless", "dirty", "odd", "stupid")


def sentence():
    return "The {} {} {} {}.".format(
        random.choice(adj),
        random.choice(nouns),
        random.choice(verbs),
        random.choice(adv),
    )


LOGGERS = [LOGGER.warning, LOGGER.debug, LOGGER.error, LOGGER.critical]


class Request:
    METHODS = ["POST", "GET", "PATCH", "PUT"]
    URLS = ["/hello", "/help", "/accounts", "/bits"]

    def __init__(self):
        self.method = random.choice(self.METHODS)
        self.url = random.choice(self.URLS)
        self.remote_addr = "192.168.0.1"
        self.headers = {"user-agent": "Christie's Computer"}
        self.referrer = "Ross Geller"
        self.META = {"HTTP_X_CLOUD_TRACE_CONTEXT": str(uuid.uuid4().hex)}
        self.content_length = "50"


class Response:
    STATUS_CODES = [200, 400, 500]

    def __init__(self):
        self.status_code = random.choice(self.STATUS_CODES)
        self.content_length = 200


def handler(request):
    print(request.url)
    print("-------------------------")
    print("LOGGER.handlers: {}".format(LOGGER.handlers))
    LOGGER.info(sentence())
    random.choice(LOGGERS)(sentence())
    LOGGER.info(sentence())
    response = Response()
    print(response.status_code)
    print(response.content_length)
    return response


def main():
    middleware = GCPLoggingMiddleware(handler)
    request = Request()
    middleware(request)


if __name__ == "__main__":
    main()
