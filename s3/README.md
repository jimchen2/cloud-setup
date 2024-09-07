```
user@fedora ~> rclone lsd s3:
          -1 2024-06-02 13:18:21        -1 jimchen4214-archive
          -1 2024-06-02 13:18:23        -1 jimchen4214-blog
          -1 2024-07-17 18:35:16        -1 jimchen4214-git
          -1 2024-07-19 00:33:25        -1 jimchen4214-mail
          -1 2024-08-03 04:44:01        -1 jimchen4214-mastodon
          -1 2024-07-17 12:24:32        -1 jimchen4214-mongo
          -1 2024-07-19 03:50:24        -1 jimchen4214-photo
          -1 2024-05-29 17:07:49        -1 jimchen4214-public
          -1 2024-07-19 14:41:20        -1 jimchen4214-status
          -1 2024-08-04 05:49:58        -1 jimchen4214-tube
```

## I don't need glacier storage on AWS because I have too few total storage size

## Change storage class

```
aws s3 cp s3://jimchen4214-photo s3://jimchen4214-photo --recursive --storage-class STANDARD_IA
```



## Restore Glacier Objects

1. Get objects and classes in json from a bucket
2. Start restoring job for each Glacier Object
3. Restore like normal objects

