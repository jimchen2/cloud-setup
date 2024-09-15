R2: Media hoarding and backup of S3.

Specifically, the public bucket is for media hoarding, other buckets are all backups of S3.

Because of the egregious and nefarious outbound egress fees of AWS, backups should occur less frequently. The backup should occur Next February.


```
user@fedora ~> rclone lsd r2:
          -1 2024-08-15 06:46:29        -1 jimchen4214-archive
          -1 2024-08-15 06:47:37        -1 jimchen4214-blog
          -1 2024-08-15 06:47:45        -1 jimchen4214-git
          -1 2024-08-15 06:51:46        -1 jimchen4214-mail
          -1 2024-08-15 07:03:47        -1 jimchen4214-mastodon
          -1 2024-08-15 06:51:48        -1 jimchen4214-mongo
          -1 2024-08-15 06:51:56        -1 jimchen4214-photo
          -1 2024-09-05 02:40:34        -1 jimchen4214-public
          -1 2024-08-15 07:03:45        -1 jimchen4214-tube
```
