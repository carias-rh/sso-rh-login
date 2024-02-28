# OTP token generator for SSO Red Hat Login
This application runs a very simple command to generate the OTP token, but I wanted to have it isolated, so that several applications could use it as a service, so that I could "spend" only one token slot in the token.redhat.com site, which allows a maximum of 4 different tokens.

`$ oathtool --hotp $SECRET -c $COUNTER`

### Set up your token
Generate a random alphanumeric string of 40 characters in length, this will be our `SECRET`.
```
$ dd if=/dev/random bs=1M count=1 status=none | shasum | cut -b 1-40
243a0396359cb8ebe4fc3448c88dc48c113fdc24
```

Go to `token.redhat.com` with the VPN activated to create the new token with the secret. Uncheck the ☑️ `Generate OTP Key on the Server` box, paste your secret, and choose a PIN.

![image](https://user-images.githubusercontent.com/80515069/177427661-7a1d9c81-ad96-485c-a31a-376e7dc3c1e5.png)

Make sure that the `./counter` file always matches the `Count` value of the token, **initially set to 1**. It will increase the value each time you login.

![hotp](https://user-images.githubusercontent.com/80515069/212667043-69dd2e9e-c81e-4b75-a5ac-41e1b52b8f27.png)

### Run the container
`$ docker run --name sso-rh-login -d --restart always -p 5000:5000 -v "$(pwd)"/counter:/app/counter -e SECRET='243a0396359cb8ebe4fc3448c88dc48c113fdc24' sso-rh-login:latest`

### Known issues
It's possible that if you click many times the Generate OTP button, the counter passes the available range allowed and you will need to resync with the token, that's why the `counter` file is mounted as a volume in the container, so you can edit it anytime needed.
If used for automated processes this is improbable to happen.
