# Sistema de Control de Acceso

Este proyecto es un sistema de control de acceso diseñado para gestionar la autenticación de usuarios y permisos basados en roles. Implementado en Python y utilizando SQLite como base de datos, este sistema proporciona un entorno seguro y flexible para la gestión de accesos.

![Python](https://img.shields.io/badge/Python-3.8-blue.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg)

## Funciones Principales

- **Autenticación Segura**: Utiliza contraseñas para la verificación de identidad.
- **Control de Acceso Basado en Roles (RBAC)**: Define permisos según el rol del usuario.
- **Gestión de Recursos**: Administración de accesos a diferentes recursos dentro del sistema.
- **Código Modular y Extensible**: Fácil de modificar y mejorar.
- **Base de Datos Ligera**: Uso de SQLite para almacenamiento eficiente.

## Requerimientos

Para ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.8+
- SQLite (incluido en la biblioteca estándar de Python)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Draxn0919/Access_Control.git
   cd Access_Control
   ```
2. Ejecuta la aplicación:
   ```bash
   python face_access.py
   ```

## Explicación Técnica

Este sistema de control de acceso se basa en la autenticación de usuarios y la asignación de roles. Utiliza una base de datos SQLite para almacenar credenciales y permisos, permitiendo consultas rápidas y eficientes.

### Modelo de Base de Datos

La base de datos está estructurada en las siguientes tablas:

- **Usuarios**: Almacena la información de los usuarios, incluyendo credenciales encriptadas.
- **Roles**: Define diferentes niveles de acceso dentro del sistema.
- **Permisos**: Especifica qué acciones pueden realizar los usuarios según su rol.

## Mejoras Futuras

- Implementación de autenticación multifactorial.
- Integración con JWT y OAuth.
- Soporte para bases de datos adicionales como PostgreSQL o MySQL.
- Desarrollo de una interfaz gráfica para administración.

## Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

- Haz un fork del repositorio.
- Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
- Realiza tus cambios y haz un commit (`git commit -m 'Añadir nueva funcionalidad'`).
- Envía tus cambios (`git push origin feature/nueva-funcionalidad`).
- Abre un Pull Request para revisión.

## Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Consulta el archivo [LICENSE](./LICENSE) para más detalles.

## Autores

- GitHub: [@Draxn0919](https://github.com/Draxn0919)
- Email: danrivera505@gmail.com
- LinkedIn: [Daniel Rivera](https://www.linkedin.com/in/danrivera9/)

