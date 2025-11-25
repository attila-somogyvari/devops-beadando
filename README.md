# DevOps Beadando – Hello World alkalmazas Flask (PY) hasznalataval

Ez a projekt egy egyszeru "Hello World" Flask alkalmazast futtat, amelyen keresztul bemutatom az alap Devops lepeseket:

- kodiras
- verziokezeles (trunk-based)  
- buildeles
- kontenerizalas (Docker-rel)  
- CI pipeline + Docker Hub registrybe pusholas  

---

## 1. Alkalmazas

Az alkalmazás egy minimalis Flask webszolgaltatas, ami HTTP-n keresztul erheto el es egy egyszeru szoveget jelenit meg.

- **Elerhetosegi cime:** http://localhost:8080  
- **Forraskod az "alkalmazashoz":** `app.py`

---

##  2. Buildeles es futtatas (lokalisan)

### 2.1 (Opcionalis) virtualis kornyezet letrehozasa

Windows eseteben:

```bash
python -m venv venv
venv\Scripts\activate
