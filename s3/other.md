## I don't need glacier storage on AWS because I have too few total storage size

## Change storage class

```
aws s3 cp s3://jimchen4214-photo s3://jimchen4214-photo --recursive --storage-class STANDARD_IA
```



## Restore Glacier Objects

1. Get objects and classes in json from a bucket
2. Start restoring job for each Glacier Object
3. Restore like normal objects
