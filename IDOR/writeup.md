## IDOR

We will test feature Update Account Details

`http://localhost:3000/page-account`

![img.png](img.png)

We detect id in body 

![img_1.png](img_1.png)

id=2,3,4,5???

We submit, and change account to another account => Check IDOR

account with id = `3`

![img_2.png](img_2.png)
