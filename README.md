# 📡 GitHub Activity CLI

**Una herramienta de línea de comandos para visualizar la actividad pública reciente de un usuario en GitHub.**

---

## 🚀 Características

- Consulta rápida desde terminal con: `github-activity <usuario>`
- Muestra los últimos eventos públicos (commits, stars, forks, issues, pull requests, etc.)
- Sin dependencias externas (usa solo bibliotecas estándar de Python)
- Manejo de errores ante usuarios inválidos o problemas de red
- Fácil instalación y uso en cualquier sistema con Python ≥ 3.6

---

## 🛠️ Instalación

### 🔧 Instalación local (modo editable para desarrollo)

```bash
git clone https://github.com/tuusuario/github-activity-cli.git
cd github-activity-cli
pip install -e .
````

Esto instalará el comando `github-activity` en tu sistema.

---

## 💻 Uso

```bash
github-activity <nombre_de_usuario>
```

### Ejemplo:

```bash
github-activity torvalds
```

### Salida esperada:

```
- 🔁 Pushed 2 commits to torvalds/linux
- ⭐ Starred octocat/Hello-World
- 🔃 Opened a pull request in linux/kernel
```

---

## 🧪 Desarrollo y pruebas

Este proyecto no usa dependencias externas ni frameworks, por lo que puedes probar directamente ejecutando el script:

```bash
python github_activity/cli.py <usuario>
```

---

## 🧱 Estructura del Proyecto

```
github_activity/
├── github_activity/
│   └── cli.py
├── setup.py
└── README.md
```

---

## 📝 Licencia

MIT © Andejecruher

---

## 🌐 Créditos

Este proyecto utiliza la [GitHub REST API](https://docs.github.com/en/rest) para obtener los datos públicos de usuario.

