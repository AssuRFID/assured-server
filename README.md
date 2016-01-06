# Assured-server #
Python REST server powering the Assured security suite. Uses lighttpd, flask and an sqlite db for a small footprint.

## Dependencies ##
  * [Python 2.7](http://python.org)
  * [Flask](http://flask.pocoo.org)
  * [SQLAlchemy](http://sqlalchemy.org)
  * [Lighttpd](https://www.lighttpd.net)
  * [SQLite](http://www.sqlite.org)
  
## Instructions ##
  1. Run `sudo lighttpd-enable-mod fastcgi`
  2. Copy <lighttpd.conf> to `/etc/lighttpd/lighttpd.conf`. Adjust values as needed.
  3. Start with `systemctl restart lighttpd`.
  4. Test by visiting <http://localhost/assured/api/v1.0/tags>
  4. To start on bootup, `systemctl enable lighttpd`
