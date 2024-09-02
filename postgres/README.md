```
postgres-# \l
                                                           List of databases
        Name         |  Owner   | Encoding | Locale Provider |  Collate   |   Ctype    | ICU Locale | ICU Rules |   Access privileges   
---------------------+----------+----------+-----------------+------------+------------+------------+-----------+-----------------------
 freshrss_production | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =Tc/postgres         +
                     |          |          |                 |            |            |            |           | postgres=CTc/postgres+
                     |          |          |                 |            |            |            |           | freshrss=CTc/postgres
 gitea_production    | gitea    | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 mastodon_production | mastodon | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 matrix_production   | matrix   | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =Tc/matrix           +
                     |          |          |                 |            |            |            |           | matrix=CTc/matrix
 metabase_production | metabase | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 peertube_production | peertube | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 postgres            | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 template0           | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/postgres          +
                     |          |          |                 |            |            |            |           | postgres=CTc/postgres
 template1           | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/postgres          +
                     |          |          |                 |            |            |            |           | postgres=CTc/postgres
(9 rows)

postgres-# \du
                             List of roles
 Role name |                         Attributes                         
-----------+------------------------------------------------------------
 freshrss  | 
 gitea     | 
 mastodon  | 
 matrix    | Create DB
 metabase  | 
 peertube  | 
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS
 ```