# Linear Regression from Scratch (with Visualization) 📉

Prosta implementacja **Regresji Liniowej** w Pythonie napisana "od zera" (bez użycia `scikit-learn`). Projekt służy do edukacyjnej wizualizacji algorytmu **Gradient Descent** (Metoda Najszybszego Spadku).

Skrypt wyświetla animowany wykres, pokazując w czasie rzeczywistym, jak model matematyczny "uczy się" dopasowywać linię do danych (Salary Data).

## ✨ Funkcjonalności

* 🧠 **Czysta matematyka:** Ręczna implementacja obliczania gradientów (pochodnych cząstkowych) oraz funkcji błędu (MSE).
* 🎬 **Wizualizacja na żywo:** Wykres aktualizujący się co 10 epok, pokazujący proces uczenia "na żywo".
* 📊 **Monitoring:** Wyświetlanie numeru epoki i aktualnego błędu średniokwadratowego (MSE) bezpośrednio na wykresie.

## 🛠️ Wymagania

* **uv** (Python Package Manager)
* Biblioteki: `pandas`, `numpy`, `matplotlib`

## 🚀 Jak uruchomić (używając uv)

1. Upewnij się, że w folderze z projektem znajduje się plik z danymi `Salary_Data.csv`.

2. Zainstaluj wymagane zależności w projekcie:
   ```bash
   uv add pandas numpy matplotlib