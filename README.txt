
W celu uruchomienia programu nale�y poda� funkcje w �ci�le okre�lowj kolejno�ci i formacie jaki przedstawiono poni�ej:

Przyk�ad 1:

max 60x1 +30x2 +20x3
8x1 +6x2 +x3 <= 960
8x1 +4x2 +3x3 <= 800
4x1 +3x2 +x3 <= 320
stop

W celu wygenerowania wykresu przedstawiaj�cego obszar poszukiwa� nale�y poda� funkcje zawiej�ce 2 zmienna, tak jak przedstawiono poni�ej:

Przyk�ad 2: (wykres zostanie zapisany do pliku SimplexChart.png)

max 8x1 + 5x2 
6x1 +10x2 <= 45 
9x1 +5x2 <= 45
stop

// -------------------------------------------
 
Kompilator:
python-3.5.2

Install matplotlib:
python -m pip install -U pip setuptools

Install plotly:
pip install --upgrade plotly