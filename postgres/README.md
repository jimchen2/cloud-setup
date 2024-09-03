```
postgres=# \du
                             List of roles
 Role name |                         Attributes                     
    
-----------+--------------------------------------------------------
----
 gitea     | 
 mastodon  | 
 matrix    | Create DB
 metabase  | 
 miniflux  | 
 peertube  | 
 postgres  | Superuser, Create role, Create DB, Replication, Bypass 
RLS

postgres=# ALTER ROLE matrix NOCREATEDB;
ALTER ROLE
postgres=# 
postgres=# \du
                             List of roles
 Role name |                         Attributes                     
    
-----------+--------------------------------------------------------
----
 gitea     | 
 mastodon  | 
 matrix    | 
 metabase  | 
 miniflux  | 
 peertube  | 
 postgres  | Superuser, Create role, Create DB, Replication, Bypass 
RLS

postgres=# \l
                                                           List of d
atabases
        Name         |  Owner   | Encoding | Locale Provider |  Coll
ate   |   Ctype    | ICU Locale | ICU Rules |   Access privileges   
---------------------+----------+----------+-----------------+------
------+------------+------------+-----------+-----------------------
 gitea_production    | gitea    | UTF8     | libc            | en_US
.utf8 | en_US.utf8 |            |           | 
 mastodon_production | mastodon | UTF8     | libc            | en_US
.utf8 | en_US.utf8 |            |           | 
 matrix_production   | matrix   | UTF8     | libc            | en_US
.utf8 | en_US.utf8 |            |           | =Tc/matrix           +
                     |          |          |                 |      
      |            |            |           | matrix=CTc/matrix
 metabase_production | metabase | UTF8     | libc            | en_US
.utf8 | en_US.utf8 |            |           | 
 miniflux            | miniflux | UTF8     | libc            | en_US
.utf8 | en_US.utf8 |            |           | =Tc/miniflux         +
                     |          |          |                 |      
      |            |            |           | miniflux=CTc/miniflux
 peertube_production | peertube | UTF8     | libc            | en_US
.utf8 | en_US.utf8 |            |           | 
 postgres            | postgres | UTF8     | libc            | en_US
.utf8 | en_US.utf8 |            |           | 
 template0           | postgres | UTF8     | libc            | en_US
.utf8 | en_US.utf8 |            |           | =c/postgres          +
                     |          |          |                 |      
      |            |            |           | postgres=CTc/postgres
 template1           | postgres | UTF8     | libc            | en_US
.utf8 | en_US.utf8 |            |           | =c/postgres          +
                     |          |          |                 |      
      |            |            |           | postgres=CTc/postgres
(9 rows)

```