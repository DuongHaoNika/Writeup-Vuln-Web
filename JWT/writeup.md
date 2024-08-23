## JWT 

### None Alg

First, we access to `None Alg` level.

![img.png](img.png)

After we have successfully logged in, it will be granted a token.

![img_1.png](img_1.png)

And when we decode it with JWT Editor or `https://token.dev/`, it will look like this:

![img_3.png](img_3.png)

Set `alg` is `none` and add `.` to end of token

![img_4.png](img_4.png)

![img_5.png](img_5.png)

DONE!

### Weak Key

Get jwt -> use tool: `hashcat`

`hashcat -a 0 -m 16500 eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsImlhdCI6MTcyNDQyOTExNH0.WAYwnF9enco3vKphiVXpaKox49TO6nvll82lNsGkxjI jwt_secrets/jwt_secrets_uniq.txt
hashcat `

-> secret-key

### Alg Confusion

Let's see the decode token.

![img_6.png](img_6.png)

See the difference ⇒ and I see the token is signed by asymmetric algorithm as RS256

That algorithm uses one key pair follow: public key and private key, private key is used to signed token and public key is used to verify.

Exploit:

Obtain the server's public key.
Convert the public key to a suitable format.
Create a malicious JWT with a modified payload and the alg header set to HS256.
Sign the token with HS256, using the public key as the secret.
Obtain the server's public key `/.well-known/jwks.json`.

```
{

    "keys": [

        {

            "kty": "RSA",

            "e": "AQAB",

            "kid": "6f597b7-fd81-44c7-956f-6937ea94cdf6",

            "n": "08q7VZbBa0y8MxwfrCvb2rq0jlUcDzzi3xoR38VRuoDjqlWXiQFjqounAIOcqHdCxwQxaKrF0wEScS0tkkyc8sfuYf06_5cYB-jqbifQbHNBeRRmsYzD6lmgbdfwXO5ugYNG-pasLEQxIklyjRi-lV_DdyBYL7f8vQJsIUu7Iga1w4BwbbAKYCRcuYk32xuX7BWxtpXpLEoHseb1q0B_mT6QixYqHiNstFBo-EBFbNnlpobBSXTGjYrAgfTMAqKv6GoNLEePJ9bY_rbSQV-gbO1FQ5MADm4ZT4S_Qcp7j5z_6DF1oUHHTn5ky5gMYFvbALGNiQiivY7gfSRib-WN7w"

        }

    ]

}
```

Although the server may expose their public key in JWK format, when verifying the signature of a token, it will use its own copy of the key from its local filesystem or database. This may be stored in a different format.

In order for the attack to work, the version of the key that you use to sign the JWT must be identical to the server's local copy.

Or you can just use it as it’s,but base-64 decoded.

Let's create a new RSA key by use the expose key.

![img_7.png](img_7.png)

![img_8.png](img_8.png)

Back to JSON Web Token, change alg from RS256 to HS256 and modify the payload.

The last, sign the token with Symmetric that we have just created.

![img_9.png](img_9.png)

DONE!!!
