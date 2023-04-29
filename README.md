flask-pybrcode
==============

This is a small flask server using pybrcode library. The server provides a Pix QRCode in SVG string when accessed via a URL like:
```
http://127.0.0.1:5000/brcode/<value>/<key>/<name>

example:

http://127.0.0.1:5000/brcode/3.56/406c5d72-e8e1-40dd-87a9-f7846d08f9e1/Vin%C3%ADcius%20Fonseca%20Maciel
```

For this example a SVG string containing a R$3,56 pix QRCode for "Vinícius Fonseca Maciel" which key is "406c5d72-e8e1-40dd-87a9-f7846d08f9e1" is generated.

Visit the [pybrcode repository](https://github.com/ViniciusFM/pybrcode) for more information.