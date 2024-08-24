## SSRF

### Preparation 

Go to settings and set `SSRF` is `Yes`

I will check SSRF vul in Add Product `http://localhost:3000/product/add`

![img.png](img.png)

![img_1.png](img_1.png)

We will test feature Preview Image

![img_2.png](img_2.png)

Server get URL image, send request to show image for us

What if we inject: `http://localhost:3000/admin`

![img_3.png](img_3.png)

We get source here 
![img_4.png](img_4.png)

Use base64 decode

![img_5.png](img_5.png)