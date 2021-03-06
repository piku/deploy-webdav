With this application you can deploy a simple password-protected webdav server using [Piku](https://github.com/rcarmo/piku).

```
git remote add piku piku@yourserver.net:webdav
git push piku master
piku config:set NGINX_SERVER_NAME=somedomain.net PASSWORDS="username:password username2:password2 ..." FOLDERS="/joplin:/home/piku/joplin"
```

 * `NGINX_SERVER_NAME` is the domain name you want for the webdav server (the domain must point at the machine already).
 * `PASSWORDS` is a list of space separated `username:password` pairs.
 * `FOLDERS` is a list of `/URL:/FOLDER` mappings, defaulting to `/webdav:/home/piku/webdav`.

This app has been successfully tested with [Joplin](https://github.com/laurent22/joplin) sync.
