```
user@fedora ~> rclone lsd s3:
          -1 2024-06-02 13:18:21        -1 jimchen4214-archive
          -1 2024-06-02 13:18:23        -1 jimchen4214-blog
          -1 2024-07-17 18:35:16        -1 jimchen4214-git
          -1 2024-07-19 00:33:25        -1 jimchen4214-mail
          -1 2024-08-03 04:44:01        -1 jimchen4214-mastodon
          -1 2024-07-17 12:24:32        -1 jimchen4214-mongo
          -1 2024-07-19 03:50:24        -1 jimchen4214-photo
          -1 2024-08-04 05:49:58        -1 jimchen4214-tube
```

## Each Bucket's Purpose

## Public Buckets

- **jimchen4214-blog**: Personal Blog photo and media storage, no delete.
- **jimchen4214-mastodon**: Mastodon storage.
- **jimchen4214-tube**: Peertube Storage.

## Private Buckets

- **jimchen4214-archive**: Archive for any files, no delete.
- **jimchen4214-git**: Github backup every week, see Lambda function.
- **jimchen4214-mail**: Mail Storage, from receiving in SES.
- **jimchen4214-mongo**: MongoDB database backup of Blogs, every 30 minutes, see Lambda function.
- **jimchen4214-photo**: Photo backup from Android by FolderSync.
