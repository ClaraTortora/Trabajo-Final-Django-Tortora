Trabajo Final Django - Clara I. Tortora

Alumna - Clara Inés Tortora
Comisión - 40445

Idea del trabajo

video : https://youtu.be/wQcnVEiSKrk



Mi idea fue crear una página para la compra y venta de celulares, en la que las personas al ingresar no verán los productos hasta que se registren y logueen. Al ingresar a la página puede verse un inicio con algunas secciones y un navbar. Una vez logueados, se pueden ver los productos, detalles de la categoría de productos y las ofertas. 
Como admin (superuser) podes ver todo eso también, pero además hacer un CRUD de cada apartado anterior (producto, categoría de productos y ofertas) que ofrece la página. Existe también el logout.
Hay un apartado llamado 'sobre mi' que cuenta brevemente quien soy y que me gusta hacer.

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



