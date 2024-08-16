```bash
docker-compose run --rm web bundle exec rails mastodon:setup
```

Nginx

```
sudo ln -sf /etc/nginx/sites-available/mastodon.jimchen.me.conf /etc/nginx/sites-enabled/
```

## Troubleshooting

### User Doesn't Exist

```
2024-08-03T12:57:07.280Z pid=7 tid=5en WARN: ActiveRecord::StatementInvalid: PG::UndefinedTable: ERROR:  relation "users" does not exist
/opt/mastodon/vendor/bundle/ruby/3.2.0/gems/activesupport-7.0.8.4/lib/active_support/concurrency/load_interlock_aware_monitor.rb:25:in `handle_interrupt'
/opt/mastodon/vendor/bundle/ruby/3.2.0/gems/activesupport-7.0.8.4/lib/active_support/concurrency/load_interlock_aware_monitor.rb:21:in `handle_interrupt'
```

### Solution:

```
docker-compose run --rm web rails db:migrate
```

### Error loading page

```
root@ip-172-31-25-211:~/mastodon# cat /var/log/nginx/error.log|tail -n 5
2024/08/03 12:26:23 [error] 605545#605545: *14000 connect() failed (111: Connection refused) while connecting to upstream, client: 175.159.120.173, server: mastodon.jimchen.me, request: "GET /oops.gif HTTP/1.1", upstream: "http://127.0.0.1:3050/oops.gif", host: "mastodon.jimchen.me", referrer: "http://mastodon.jimchen.me/"
2024/08/03 12:26:26 [error] 605546#605546: *14005 connect() failed (111: Connection refused) while connecting to upstream, client: 175.159.120.173, server: mastodon.jimchen.me, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3050/", host: "mastodon.jimchen.me"
2024/08/03 12:26:27 [error] 605546#605546: *14005 connect() failed (111: Connection refused) while connecting to upstream, client: 175.159.120.173, server: mastodon.jimchen.me, request: "GET /favicon.ico HTTP/1.1", upstream: "http://127.0.0.1:3050/favicon.ico", host: "mastodon.jimchen.me", referrer: "https://mastodon.jimchen.me/"
2024/08/03 12:59:39 [error] 605546#605546: *14222 connect() failed (111: Connection refused) while connecting to upstream, client: 175.159.120.173, server: mastodon.jimchen.me, request: "GET / HTTP/1.1", upstream: "http://127.0.0.1:3050/", host: "mastodon.jimchen.me"
2024/08/03 12:59:40 [error] 605546#605546: *14222 connect() failed (111: Connection refused) while connecting to upstream, client: 175.159.120.173, server: mastodon.jimchen.me, request: "GET /sw.js HTTP/1.1", upstream: "http://127.0.0.1:3050/sw.js", host: "mastodon.jimchen.me"
root@ip-172-31-25-211:~/mastodon#
```

### Solution

Configure Nginx

### This page is not correctly, "We're sorry, but something went wrong on our end."

```
root@ip-172-31-25-211:~/mastodon# docker logs 5dbc74221680|grep -i err
[28f2ff45-d4a6-423f-ba94-14af0e3b700b] ActionDispatch::RemoteIp::IpSpoofAttackError (IP spoofing attack?! client 172.25.0.1 is not a trusted proxy HTTP_CLIENT_IP=nil HTTP_X_FORWARDED_FOR="175.159.120.173"):
[19e08cac-7ecc-48c2-9a92-6db16dd60aa2] ActionDispatch::RemoteIp::IpSpoofAttackError (IP spoofing attack?! client 172.25.0.1 is not a trusted proxy HTTP_CLIENT_IP=nil HTTP_X_FORWARDED_FOR="175.159.120.173"):
[8abd4644-fdd4-42bd-a336-112163684a42] ActionDispatch::RemoteIp::IpSpoofAttackError (IP spoofing attack?! client 172.25.0.1 is not a trusted proxy HTTP_CLIENT_IP=nil HTTP_X_FORWARDED_FOR="175.159.120.173"):
```

### Solution

Remove these env variables

```
TRUSTED_PROXY_IP=
ALLOWED_PRIVATE_ADDRESSES=
```

in `.env.production`, the default configuration will work

### No Admin Account

### Solution

```
docker exec -it mastodon-web-1 bash -c "RAILS_ENV=production bin/tootctl accounts create jimchen --email jimchen4214@gmail.com --confirmed --role Owner"
```

### Your application is pending review by our staff. This may take some time. You will receive an e-mail if your application is approved.

### Solution

```
docker exec -it mastodon-web-1 bash -c "RAILS_ENV=production bin/tootctl accounts approve jimchen"
```

### Can't Upload Attachments

```
XHRPOST
https://mastodon.jimchen.me/api/v2/media
[HTTP/2 500  1644ms]
```

and

```
175.159.120.173 - - [03/Aug/2024:13:34:47 +0000] "POST /api/v2/media HTTP/2.0" 500 894 "https://mastodon.jimchen.me/publish" "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0" "-"
```

### Solution

Basically I found the bug

```
root@ip-172-31-25-211:~/mastodon# docker logs 2c08760f4abf|grep -i err
[893e166d-5198-46e3-8496-4bff97c1b501] Aws::S3::Errors::AccessControlListNotSupported (The bucket does not allow ACLs):
```

### No "Administered by"

### Solution

Go to `/admin/settings/branding` and set contact username(@admin) and email

### Cannot open images

Wrong Hostname

### Solution

Use `S3_ALIAS_HOST` instead of S3 hostname in `.env.production`


### Migration: 

After modifying the Postgres host

```

To resolve this issue:

- Did you create the database for this app, or delete it? You may need to create your database.
- Has the database name changed? Check your database.yml config has the correct database name.


2024-08-16T12:39:23.581Z pid=7 tid=5en WARN: ActiveRecord::NoDatabaseError: We could not find your database: mastodon. Which can be found in the database configuration file located at config/database.yml.
```

### Solution

So basically like there is a permission issue. In PostgreSQL, being the owner of a database doesn't automatically grant you all permissions on that database when you're connecting as a non-root user. (This is really really confusing) 

Please grant nonroot user all permissions and make sure psql logged in as nonroot user can see everything.