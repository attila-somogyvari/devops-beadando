# DevOps beadando feladat – Hello World alkalmazas Flask (PY) hasznalataval

Ez a projekt egy szimpla "Hello World" Flask alkalmazast futtat, amelyen keresztul bemutatom az elvart alap DevOps lepeseket:

- program forraskod
- verziokezeles (trunk alapu)  
- buildeles
- kontenerizalas (Docker-rel)  
- CI pipeline + Docker Hub registrybe pusholas  

---

## 1. Alkalmazas

Az alkalmazás egy minimalis Flask webszolgaltatas, ami HTTP-n keresztul erheto el es egy egyszeru szoveget jelenit meg.

- **Elerhetosegi cime a kovetkezo:** http://localhost:8080  
- **Forraskod az "alkalmazashoz":** `app.py`

---

##  2. Buildeles es futtatas lokalisan

Windows eseteben:

```bash
python -m venv venv
venv\Scripts\activate
