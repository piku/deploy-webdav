import os
from wsgidav.wsgidav_app import WsgiDAVApp
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("wsgidav")
logger.propagate = True
logger.setLevel(logging.DEBUG)

passwords = os.environ.get("PASSWORDS", "")
passwords = {p.split(":")[0]: {"password": p.split(":")[1]} for p in passwords.split(" ")} if passwords else {}
folders = {p.split(":")[0]: {"password": p.split(":")[1]} for p in os.environ.get("FOLDERS", "/webdav:/home/piku/webdav").split(" ")}

for f in folders:
    try:
        os.makedirs(folders[f], 0o755)
    except FileExistsError:
        pass

config = {
    "provider_mapping": folders,
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
