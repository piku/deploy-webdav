import os
from wsgidav.wsgidav_app import WsgiDAVApp
import logging

root = os.environ.get("ROOT", "/home/piku/webdav")

try:
    os.makedirs(root, 0o755)
except FileExistsError:
    pass

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("wsgidav")
logger.propagate = True
logger.setLevel(logging.DEBUG)

passwords = {p.split(":")[0]: {"password": p.split(":")[1]} for p in os.environ.get("PASSWORDS").split(" ")}

config = {
    "provider_mapping": {
      "/": "/home/piku/webdav/",
    },
    "verbose": 1,
    "http_authenticator": {
        "domain_controller": None,
        "accept_basic": True,
        "accept_digest": True,
        "default_to_digest": True,
    },
    "simple_dc": {
        "user_mapping": {
            "*": passwords,
            "/public": True,
        }
    }
}

app = WsgiDAVApp(config)
