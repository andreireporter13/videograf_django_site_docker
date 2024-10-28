# ssl certificates
docker-compose run --rm certbot certonly --webroot -w /var/www/certbot -d razvanvideo.ro -d www.razvanvideo.ro

#
docker-compose down

docker-compose up --build

docker-compose up -d

# linux
sudo systemctl start docker.service
sudo systemctl stop docker.service
sudo systemctl enable docker.service


####################################################################################################
# Ghid pentru gestionarea aplicației Docker

## 1. Când să faci `docker-compose build`
- **Făcând modificări la Dockerfile**: Dacă ai modificat Dockerfile-ul (de exemplu, ai adăugat sau eliminat pași de instalare).
- **Actualizând `requirements.txt`**: Dacă ai adăugat sau schimbat pachete în `requirements.txt`.

## 2. După ce ai făcut build-ul
- **Pentru a rula aplicația**: După ce ai construit imaginile cu `docker-compose build`, poți porni aplicația cu:
  ```bash
  docker-compose up -d
  ```
  Aceasta va lansa containerele în fundal (`-d` pentru "detached mode").

## 3. Când să folosești doar `docker-compose up -d`
- **După ce ai modificat codul sursă**: Dacă ai modificat fișierele aplicației (ex. `.py`, `.html`, `.css`) dar nu ai modificat Dockerfile-ul sau `requirements.txt`, poți folosi direct:
  ```bash
  docker-compose up -d
  ```

## Scurt exemplu de flux de lucru
1. **Modificări la aplicație** (ex. modifici `views.py`):
   - **Rularea aplicației**:
     ```bash
     docker-compose up -d
     ```

2. **Modificări la `Dockerfile` sau `requirements.txt`**:
   - **Construcția imaginilor**:
     ```bash
     docker-compose build
     ```
   - **Rularea aplicației**:
     ```bash
     docker-compose up -d
     ```

## Oprirea aplicației
- **Pentru a opri aplicația**:
  ```bash
  docker-compose down
  ```

## Recapitulare
1. **`docker-compose build`**: Folosit pentru modificările care necesită reconstruirea imaginilor.
2. **`docker-compose up -d`**: Folosit pentru a porni containerele (în fundal) după construirea imaginilor sau după modificarea codului sursă.
