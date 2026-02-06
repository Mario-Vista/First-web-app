# Login Page – Full Stack Project

Questo progetto è una **pagina di login full stack** che mostra l’integrazione tra frontend, backend e database utilizzando **Docker**, **FastAPI**, **PostgreSQL** e **React**.

L’architettura è composta da:

* **Database PostgreSQL** in un container Docker
* **Backend Python** con **FastAPI** in un container Docker
* **Frontend React (JavaScript)** eseguito in locale

Il backend e il database sono orchestrati tramite **Docker Compose**.

---

## 🧱 Struttura del progetto

```text
.
├── backend/        # Backend FastAPI (Python)
├── frontend/       # Frontend React (JavaScript)
├── docker/         # Dockerfile, docker-compose e file .env
└── README.md
```

---

## ⚙️ Tecnologie utilizzate

### Backend

* Python
* FastAPI
* PostgreSQL
* Docker

### Frontend

* React
* JavaScript

### DevOps

* Docker
* Docker Compose
* File `.env` per la gestione delle variabili d’ambiente

---

## 🔐 Variabili d’ambiente

Le variabili d’ambiente sono definite in un file **`.env`** (presente nella cartella `docker/`) e vengono utilizzate da **Docker Compose** per configurare backend e database.

Esempio di variabili:

```env
POSTGRES_DB=login_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DATABASE_URL=postgresql://postgres:postgres@db:5432/login_db
```

> ⚠️ Il file `.env` **non dovrebbe essere committato** su GitHub.
> Assicurati di aggiungerlo al `.gitignore`.

---

## 🚀 Avvio del progetto

### Prerequisiti

Assicurati di avere installato:

* Docker
* Docker Compose
* Node.js e npm (o yarn)

---

### 1️⃣ Avvio Backend + Database

Dalla cartella `docker/`:

```bash
docker-compose up --build
```

Questo comando avvierà:

* il container PostgreSQL
* il container del backend FastAPI

L’API sarà disponibile (di default) su:

```
http://localhost:8000
```

Documentazione Swagger:

```
http://localhost:8000/docs
```

---

### 2️⃣ Avvio del Frontend

Dalla cartella `frontend/`:

```bash
npm install
npm run dev
```

Il frontend React sarà disponibile su:

```
http://localhost:5173
```

---

## 🔁 Comunicazione tra i servizi

* Il **backend** comunica con PostgreSQL tramite la rete Docker
* Il **frontend** comunica con il backend tramite API REST
* Le configurazioni sensibili sono gestite tramite file `.env`

---

## 📦 Docker

Nella cartella `docker/` sono presenti:

* `Dockerfile` del backend
* `docker-compose.yml`
* file `.env` per la configurazione dei servizi

Il frontend **non è containerizzato** e viene eseguito in locale.

---

## 📌 Note

* Progetto pensato per scopi didattici / di sviluppo
* Non include configurazioni di produzione (HTTPS, reverse proxy, CI/CD)
* Le credenziali sono gestite esclusivamente tramite variabili d’ambiente

---

## 🛠️ Possibili miglioramenti futuri

* Containerizzazione del frontend
* Autenticazione JWT
* Hashing avanzato delle password
* Test automatici
* Deployment in produzione


