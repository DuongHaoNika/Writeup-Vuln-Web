## XXE

We check feature `Add To Cart` 
Example in: `http://localhost:3000/product?id=Small-Steel-Bacon-ae7c02f2-221b-4f24-bc9c-0843cee3bdc3`

![img.png](img.png)

Open in Burp Suite, we detect xml in body

![img_1.png](img_1.png)

We inject 

![img_2.png](img_2.png)

and send!!!