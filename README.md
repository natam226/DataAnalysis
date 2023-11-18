# DataAnalysis
En este repositorio se encuentra toda la información del primer proyecto de nuestra clase de Programación orientada a DataScience.

A continuación, encontrarás una descripción del contenido del repositorio.

---
## dataset

El directorio `dataset` contiene un archivo en formato xlsx que sirve como conjunto de datos para la aplicación. A continuación se detallan los encabezados de las columnas presentes en el conjunto de datos:

- **NOMBRE**
- **CONVENIO**
- **MONTO**
- **ASESOR**
- **ESTADO**
- **ENTIDAD**

Estos encabezados representan las diferentes categorías de información almacenada en el conjunto de datos. La aplicación web utiliza estos datos para proporcionar una interfaz de usuario interactiva y almacenar la información ingresada en la base de datos.

### Uso del Dataset

Si deseas utilizar un conjunto de datos diferente o actualizar el existente, asegúrate de que los encabezados coincidan con la estructura mencionada anteriormente para garantizar un funcionamiento correcto de la aplicación.

Recuerda que este conjunto de datos es esencial para el correcto funcionamiento y la consistencia de la información manejada por la aplicación.

---

## Scripts

El directorio `scripts` contiene varios archivos Python que realizan análisis y visualizaciones de datos utilizando diferentes bibliotecas. Aquí se describen brevemente cada uno de ellos:

### 1. `codigo_analisis_corte_2.py`

Este script utiliza las bibliotecas `numpy`, `pandas`, `matplotlib`, y `seaborn` para realizar análisis y visualizaciones de datos. Algunas de las visualizaciones incluyen gráficos de barras para el rendimiento de asesores, el rendimiento de convenios, y el estado de los créditos. También hay un gráfico de barras que muestra el rendimiento de los asesores por monto prestado, y un gráfico de pastel que representa el estado de los créditos.

### 2. `codigo_analisis_corte_3.py`

Este script utiliza las bibliotecas `pandas`, `plotly`, y `dash` para crear un dashboard interactivo de rendimiento. El dashboard incluye gráficos de barras para el rendimiento de asesores, el rendimiento de convenios, el rendimiento de asesores por monto prestado, un gráfico de dispersión que muestra la relación entre el monto y el estado, y un gráfico de pastel que representa el estado de los créditos.

### 3. `interfaz_proyecto.py`

Este script utiliza las bibliotecas `tkinter`, `pandas`, `plotly`, y `PIL` para crear una interfaz gráfica. La interfaz permite cargar y mostrar gráficas de rendimiento de asesores, rendimiento de convenios, rendimiento de asesores por monto prestado, estado de los créditos y la relación entre el monto y el estado.

---

Estos scripts son herramientas valiosas para analizar y visualizar los datos del conjunto de datos proporcionado en el directorio `dataset`. Puedes ejecutarlos para obtener una comprensión más profunda de los patrones y rendimientos dentro de los datos de Zaga Company.

---

## Gráficas

El directorio `Gráficas` contiene las salidas generadas por los scripts de análisis presentes en el directorio `scripts`. Cada archivo de imagen corresponde a una visualización específica generada por los scripts. Aquí se proporciona una breve descripción de cada gráfica:

1. **`Gráfica rendimiento de los asesores.png`**
   - Visualización del rendimiento de los asesores en forma de gráfico de barras.

2. **`Gráfica rendimiento del convenio.png`**
   - Gráfico de barras que representa el rendimiento del convenio.

3. **`Gráfica rendimiento asesores por monto prestado.png`**
   - Gráfico de barras que muestra el rendimiento de los asesores por el monto prestado.

4. **`Gráfica estado de los créditos.png`**
   - Gráfico de pastel que ilustra el estado de los créditos.

5. **`Relacion entre monto y el estado.png`**
   - Gráfico de dispersión que representa la relación entre el monto y el estado.

Estas imágenes son generadas por los scripts de análisis y se utilizan en la interfaz gráfica proporcionada por el script `interfaz_proyecto.py` para visualizar de manera interactiva los resultados del análisis de datos.

---

Este directorio es crucial para mantener un registro visual de los resultados obtenidos durante el análisis de datos y puede ser utilizado para comunicar eficazmente los hallazgos a otras partes interesadas.

---

## appweb: Unificación del Registro de Datos de Zaga Company

Este proyecto se centra en la creación de una aplicación web para unificar el registro de datos de clientes de Zaga Company. Proporciona un formulario intuitivo para ingresar información esencial y almacenarla en una base de datos.

### Contenido del directorio:

#### 1. Carpeta `appweb`

Contiene los archivos esenciales para la aplicación web.

##### 1.1 `index.html`

El archivo HTML que define la estructura del formulario y la interfaz de usuario.

##### 1.2 `LogoZaga.png`

El logo de Zaga Company utilizado en la interfaz de usuario.

##### 1.3 `styles.css`

Archivo de estilo que define el aspecto visual de la aplicación web.

##### 1.4 `zagadata.php`

Script PHP para procesar y almacenar los datos del formulario en la base de datos.

### Instrucciones de Uso

1. Clona el repositorio a tu máquina local.
2. Configura un servidor web local para ejecutar la aplicación.
3. Abre el archivo `index.html` en tu navegador.
4. Completa el formulario con la información del cliente.
5. Haz clic en "Agregar" para enviar los datos al servidor.

### Configuración de la Base de Datos

Asegúrate de configurar la conexión a la base de datos en el archivo `zagadata.php` con los detalles correctos del servidor MySQL.

```php
$host = "localhost";
$user = "root";
$pass = "";
$db = "basedatoszaga";

---