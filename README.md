# Chatbot RAG - asystent studenta PW – Instrukcja uruchomienia

Poniżej znajdziesz opis kroków, jak uruchomić aplikację Chatbot RAG lokalnie za pomocą **Streamlit** oraz w kontenerze **Docker**.

---

## 1. Przygotowanie środowiska

1. **Pobierz repozytorium** z kodem (np. poprzez klonowanie lub ściągnięcie paczki `.zip`).  
2. **Zainstaluj Pythona** (w wersji 3.8+).

---

## 2. Uruchomienie lokalne (Streamlit)

### 2.1. Instalacja zależności

W katalogu głównym projektu uruchom:

```bash
pip install -r requirements.txt
```

> Uwaga: Możesz użyć wirtualnego środowiska (np. `venv`) lub conda – wedle preferencji.

### 2.2. Plik `.env`

W katalogu głównym projektu (obok pliku `app.py`) stwórz plik **`.env`**, w którym umieścisz klucz do OpenAI:

```makefile
OPENAI_API_KEY=sk-xxxxx
```

### 2.3. Uruchomienie aplikacji

W terminalu:

```bash
streamlit run app.py
```

Po chwili w konsoli zobaczysz adres (zwykle `http://localhost:8501`). Otwórz go w przeglądarce. Powinieneś zobaczyć interfejs Chatbota RAG.  

---

## 3. Uruchomienie w kontenerze Docker

### 3.1. Plik `.env` i `.dockerignore`

Jeśli chcesz, aby kontener korzystał z Twojego klucza OpenAI, najlepiej **nie kopiować** go bezpośrednio do obrazu. Możesz użyć opcji `--env-file` lub `docker-compose`. 

1. Upewnij się, że masz plik `.env` w katalogu głównym (jak w kroku 2.2).  
2. Dodaj do pliku `.dockerignore` następujące wpisy (jeśli chcesz ukryć `.env` przed kopiowaniem do obrazu):
   ```
   .env
   __pycache__/
   *.pyc
   ```

### 3.2. Budowa obrazu i uruchomienie kontenera

W głównym katalogu projektu uruchom:

```bash
docker-compose up --build
```

Po chwili aplikacja będzie dostępna pod adresem:

```
http://localhost:8501
```
Po zbudowaniu obrazu każde kolejne uruchomienie kontenera możesz wywołać np. komendą:

```bash
docker-compose up
```

## 4. Testowanie

### 4.1. Testy jednostkowe

W głównym katalogu projektu uruchom:

```bash
python -m pytest tests
```

Upewnij się, że wcześniej masz zainstalowaną bibliotekę pytest.