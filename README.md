Trabajo Final Django - Clara I. Tortora

Alumna - Clara Inés Tortora

Comisión - 40445

Video explicando mi página: https://youtu.be/wQcnVEiSKrk


Idea del trabajo

<div align="center">

## Mi idea fue crear una página para la compra y venta de celulares, en la que las personas al ingresar no verán los productos hasta que se registren y logueen. Al ingresar a la página puede verse un inicio con algunas secciones y un navbar. Una vez logueados, se pueden ver los productos, detalles de la categoría de productos y las ofertas. 
Como admin (superuser) podes ver todo eso también, pero además hacer un CRUD de cada apartado anterior (producto, categoría de productos y ofertas) que ofrece la página. Existe también el logout.
Hay un apartado llamado 'sobre mi' que cuenta brevemente quien soy y que me gusta hacer.
</div>
Dato importante: cualquier persona puede loguearse, no solamente el admin puede hacer el registro. Mi idea era que, si registrabas personas siendo admin, estabas registrando vendedores, y registrandote desde la parte de login, fueran clientes.

Roadmap de la página 

/inicio - con 3 secciones con detalles, la última es un 'sobre mi'. Al principio este 'sober mi' tenía url y accedías a otra página. Luego decidí hacerlo onepage porque me gustaba como quedaba.

/navbar - que cuenta con inicio, iniciar sesión y sobre mi

/login - dentro de este apartado se encuentra también el 'registrarse'

/register - que funciona tanto como para nuevos clientes como para vendedores/trabajadores de la página

/admin - que también puede registrar y ver el panel de administración y puede loguearse en login también, sin necesidad de buscar /admin en la url

/producto - navbar (una vez logueado) - pueden verse los productos y categoría de productos (como cliente solo pueden ver detalles)

/ofertas - navbar (una vez logueado) - pueden ver las ofertas (como cliente solo pueden ver detalles)

/logout

/CRUD - que solo puede acceder el superuser o alguien del staff





Apps y CRUD

Tiene 2 apps; Home y Producto. Cuenta con 3 CRUD, ya que en producto está también 'Producto Categoría', y luego la app oferta.




Paquetes instaladas para que funcione todo

-Django
-Pillow (para las imágenes)


[![Screenshot-1.png](https://i.postimg.cc/k5n0JZ8m/Screenshot-1.png)](https://postimg.cc/18jCMvJC)
---
[![Screenshot-2.png](https://i.postimg.cc/fT1XhnGV/Screenshot-2.png)](https://postimg.cc/ykXWF5YK)
---
[![Screenshot-3.png](https://i.postimg.cc/6QXvyV5w/Screenshot-3.png)](https://postimg.cc/Hr6xNyyP)
---
[![Screenshot-4.png](https://i.postimg.cc/fybvSms2/Screenshot-4.png)](https://postimg.cc/hzHmHJfT)
---
[![Screenshot-8.png](https://i.postimg.cc/W1Vw0Bsq/Screenshot-8.png)](https://postimg.cc/nCdmJwjn)
---
[![Screenshot-20.png](https://i.postimg.cc/LsXCZcVB/Screenshot-20.png)](https://postimg.cc/rDBCBY3K)
---
[![Screenshot-19.png](https://i.postimg.cc/44z5n4gR/Screenshot-19.png)](https://postimg.cc/MXpRFSH9)
---
[![Screenshot-21.png](https://i.postimg.cc/cJwKTHTs/Screenshot-21.png)](https://postimg.cc/GB3hmbZN)
---
[![Screenshot-10.png](https://i.postimg.cc/KzQ8sgTy/Screenshot-10.png)](https://postimg.cc/tZZbsJDr)
---
[![Screenshot-11.png](https://i.postimg.cc/7Y5ZmhYp/Screenshot-11.png)](https://postimg.cc/RNzm0MtR)
---
[![Screenshot-12.png](https://i.postimg.cc/J0fVT1pL/Screenshot-12.png)](https://postimg.cc/zHFcv1mt)
---
[![Screenshot-13.png](https://i.postimg.cc/14h2GvzR/Screenshot-13.png)](https://postimg.cc/2LG0mFvg)
---
[![Screenshot-14.png](https://i.postimg.cc/DwBFhKZq/Screenshot-14.png)](https://postimg.cc/bZD40W1J)
---
[![Screenshot-15.png](https://i.postimg.cc/8C78VJxS/Screenshot-15.png)](https://postimg.cc/Z9zs8RT7)
---
[![Screenshot-16.png](https://i.postimg.cc/28rPSXgT/Screenshot-16.png)](https://postimg.cc/fkqHH5z0)
---
[![Screenshot-17.png](https://i.postimg.cc/N09nnhrG/Screenshot-17.png)](https://postimg.cc/KKbQKHNC)
---
[![Screenshot-18.png](https://i.postimg.cc/4yLbZdrD/Screenshot-18.png)](https://postimg.cc/64ZGf96c)


