# open SSL

### Generating public / privte key pair
#### Generating Your Private Key

```console
openssl genrsa -out aatmaj.key 2048
notepad aatmaj.key
openssl rsa -text -in aatmaj.key -noout
```

Private key will open like this and show the information about the key
![image](https://github.com/Aatmaj-Zephyr/information-security/assets/83284294/531001ca-c35b-43be-9419-f7da53e6ce53)

#### Generating Your Public Key

```console
openssl rsa -in aatmaj.key -pubout -out aatmaj_public.key
notepad aatmaj_public.key
```

![image](https://github.com/Aatmaj-Zephyr/information-security/assets/83284294/4ddbb03d-e061-40f3-b3b2-5d439697d84e)


### Encrypt the file

Encrypting a text file using RSA using the above public key

```console

openssl pkeyutl -encrypt -in plaintest.txt -inkey aatmaj_public.key -pubin -out encrypted.txt
notepad plaintest.txt
notepad encrypted.txt

```


Plaintext -> hippopotamus
CipherText -> –¬»)Ì»Q%U7DãËÎM_ôœ\Li!¨ºžCæÀØ^0Veˆ¼/ëHÄ/zW~˜§ËúWóATÛó“¯Mšh÷
©éSé_4†ùa¯®/|üúX€^íÈvºHøÖUXö^eíFé˜„±¢t”>\Ã˜,¼•àI¤LÐµlq’-öãÀÉfJcØzÇTe£üQÕô¹Ï(fWa³ìÕêw%¢]!£Sá{¯ðíñßÚ¦úøJ¾7¯Šø0.CqÛõ*,™eñ œ3¤5Ø”u®…hjŒIÅJd&Y@ørH¹ÜKðÿúÐ-fB+^öx±e


![image](https://github.com/Aatmaj-Zephyr/information-security/assets/83284294/e3d69d3a-16e6-4baa-8a92-a9a062d970c8)



### Hash a file

Lets hash a file using SHA 256

```console
openssl dgst -sha256 plaintest.txt
```

![image](https://github.com/Aatmaj-Zephyr/information-security/assets/83284294/c90c05a0-1f35-41ca-b512-680bb6c898cc)


### Generate a certificate

Generate a password secured certificate key.
Then generate certificate using the key

```console
openssl genrsa -des3 -out aatmaj_cert.key 2048
..Enter PEM pass phrase:
..Verifying - Enter PEM pass phrase:
notepad aatmaj_cert.key
openssl req -key aatmaj_cert.key -new -out domain.csr
openssl x509 -text -noout -in domain.crt
```

![image](https://github.com/Aatmaj-Zephyr/information-security/assets/83284294/737857ce-aa6e-48d2-ae49-dee6da4ff079)

![image](https://github.com/Aatmaj-Zephyr/information-security/assets/83284294/d16c8f98-1aaf-4588-ad48-b04d5cc89966)


### Generate a key for the certificate

```console
penssl genrsa -aes128 -passout pass:aatmaj -out private.pem 4096
openssl rsa -in private.pem -passin pass:aatmaj -pubout -out public.pem
notepad private.pem
notepad public.pem
```
![image](https://github.com/Aatmaj-Zephyr/information-security/assets/83284294/0d2d8a01-181c-477c-8019-4e8225f64bfe)



### Create signature for text file

 
 ```
openssl dgst -sha256 -sign private.pem -out sign.sha256 plaintest.txt
..Enter pass phrase for private.pem:
openssl base64 -in sign.sha256 -out sign.bin
openssl base64 -d -in sign.bin -out sign.sha256
openssl dgst -sha256 -verify public.pem -signature sign.sha256 plaintest.txt
..Verified OK
```

![image](https://github.com/Aatmaj-Zephyr/information-security/assets/83284294/2db9cdc1-0408-4d9b-9d20-140c075c0053)
