rclone copy s3:jimchen4214-archive azure:jimchen4214-archive --progress --azureblob-access-tier archive
rclone copy s3:jimchen4214-blog azure:jimchen4214-blog --progress --azureblob-access-tier archive
rclone copy s3:jimchen4214-git azure:jimchen4214-git --progress --azureblob-access-tier archive
rclone copy s3:jimchen4214-mail azure:jimchen4214-mail --progress --azureblob-access-tier archive
rclone copy s3:jimchen4214-mongo azure:jimchen4214-mongo --progress --azureblob-access-tier archive
rclone copy s3:jimchen4214-photo azure:jimchen4214-photo --progress --azureblob-access-tier archive
rclone copy s3:jimchen4214-private azure:jimchen4214-private --progress --azureblob-access-tier archive
rclone copy s3:jimchen4214-public azure:jimchen4214-public --progress --azureblob-access-tier archive
rclone copy s3:jimchen4214-status azure:jimchen4214-status --progress --azureblob-access-tier archive

# configure azure
# [azure]
# type = azureblob
# account = [account name]
# key = [any of the 2 azure keys]
