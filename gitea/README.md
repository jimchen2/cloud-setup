## Create Admin

```
docker exec -it 003b0addcc49 sh
```

Then change to user `git`
```
gitea admin user create --username youradminname --password yoursecurepassword --email youremail@example.com --admin
```