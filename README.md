# DevOps – Hello World webalkalmazas Flask (PY) hasznalataval

Ez a projekt egy szimpla "Hello World" Flask webalkalmazast futtat, amelyen keresztul bemutatom az elvart alap DevOps lepeseket:

- program forraskod
- verziokezeles (trunk alapu)  
- buildeles
- kontenerizalas (Docker-rel)  
- CI pipeline + Docker Hub registrybe pusholas  

---

## 1. Alkalmazas

Az alkalmazás egy minimalis Flask webszolgaltatas, ami HTTP-n keresztul erheto el es egy egyszeru szoveget jelenit meg.

- **Elerhetosegi cime a kovetkezo:** http://localhost:8080  
- **Tovabbi vegpontok:** /info -> Verzio metaadat lekeres; /egeszseg -> Teljesitmeny metrika

- **Forraskod az "alkalmazashoz":** `app.py`

---

##  2. Buildeles es futtatas lokalisan

### 2.1 virtualis kornyezet letrehozasa

Windows eseteben:
```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS eseteben:
```bash
python -m venv venv
source venv/bin/activate
```

---

### 2.2 Dependenciak telepitese
```bash
pip install -r requirements.txt
```

---

### 2.3 Alkalmazas futtatasa
```bash
python app.py
```

---

## 3. Docker hasznalata
A projekt tartalmaz egy `Dockerfile`-t, amellyel az alkalmazas kontenerbe csomagolhato.

---

### 3.1 Docker img buildelese
```bash
docker build -t hello-devops:v1 .
```

---

### 3.2 Docker kontener futtatasa (8080-as port)
```bash
docker run -p 8080:8080 hello-devops:v1
```

---

## 4. Git - Trunk-alapu fejlesztes
**A projekt GitHub repojanak elerhetosege:** https://github.com/attila-somogyvari/devops-beadando

**A "program" letrehozasa trunk-alapu modell szerint tortent:**

- `main` -> stabil branch

- A fejlesztes -> rovid elettartamu feature brancheken keresztul

- Azt kovetoen vissza mergelunk a trunkra (main)

---

Peldafolyamat:

```bash
#modositasokat az app.py-ben

git checkout -b feature/update-message
git add app.py
git commit -m "Uzenet frissitese"
git checkout main
git merge feature/update-message
git push
```

---

## 5. CI - GitHub Actions es Docker Hub integracio

A projekt tartalmaz egy automatizalt CI pipelinet:
`.github/workflows/ci.yml`

A pipeline automatikusan lefut:

- minden push eseten a main branchre

- minden pull request eseten a main-re

---

**A pipeline fobb lepesei:**
1. Repo checkout
2. Python kornyezet beallitasa
3. Dependenciak telepitese
4. Docker Hub login (GitHub Secrets atiranyitassal)
5. Docker img build majd push a Docker Hubra

**Publikus Docker Hub img linkje:**
```bash
xoserino/hello-devops:latest
```

**Img lehuzasa es futtatasa:**
```bash
docker pull xoserino/hello-devops:latest
docker run -p 8080:8080 xoserino/hello-devops:latest
```

---

## 6. Projekt strukturaja
```bash
devops-beadando/
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```
		
---

## 7. Egyeb megjegyzesek

- A Flask fejlesztoi szerver nem produkcios hasznalatra keszult. (Erre vonatkozoan figyelmezteto uzenetet is dob a Flask.)

- Kontenerben futtatva a Flask szerver automatikusan indul.

- A CI pipeline minden push eseten uj Docker image-et general.

- A Docker Hub-on tarolt image teljes mertekben reprodukalhato.

- A trunk-based fejlesztes atlathato es konnyen kovetheto.

Az alkalmazas vegpontjai:

- `/` – alapveto "Hello World" szeru uzenet
- `/info` – egyszeru metaadat az alkalmazasrol
---