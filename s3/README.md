## I don't need glacier storage on AWS because I have too few total storage size

## Change storage class

```
aws s3 cp s3://jimchen4214-photo s3://jimchen4214-photo --recursive --storage-class STANDARD_IA
```
