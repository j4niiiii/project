# project

Hola, estoy trabajando en un proyecto escolar donde debo hacer una página web con un dashboard. Para esto estoy usando django.
En mi base.html tengo dos filtros, uno es un calendario y otro es un dropdown, donde me muestra los usuarios con id rol (llamados agentes).
Se supone que para extraer los datos y mostrarlos en kpis o graficas debo usar una api, esta se conecta a mi base de datos.

Entonces, actualmente lo que hago es generar un ednpoint, de ventas_totales_views (que esta en analytics),
ya probe el endpoint en postman, y si le doy las fecha y los agentes, me arroja el resultado, el problema es
en el kpi, que no me actualiza los datos, porque en un inicio esta estatico con 0, pero, despues de seleccionar 
los datos en los filtros no me actualiza nada, y ese es mi problema.

Tambien debo aclarar que uso dashboard.html para ahí mostrar todo lo relacionado a el dashboard, kpis o graficas
(ahorita solo un kpi porque es de prueba).
