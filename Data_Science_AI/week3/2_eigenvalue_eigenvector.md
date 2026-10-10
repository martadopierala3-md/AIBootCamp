# Wartości własne i wektory własne

## 1. Co to jest?

**Wartość własna** (*eigenvalue*) i **wektor własny** (*eigenvector*) opisują
szczególne działanie macierzy na wektor.

Większość wektorów po pomnożeniu przez macierz zmienia zarówno długość, jak
i kierunek. Wektor własny jest wyjątkiem: macierz zmienia jego długość lub
zwrot, ale nie zmienia jego kierunku.

Podstawowe równanie ma postać:

```text
A · v = λ · v
```

gdzie:

- `A` — macierz,
- `v` — wektor własny,
- `λ` (lambda) — wartość własna.

Jeżeli `λ > 1`, wektor zostaje wydłużony.  
Jeżeli `0 < λ < 1`, zostaje skrócony.  
Jeżeli `λ < 0`, zmienia również zwrot.

## 2. Jak obliczyć wartości własne?

Wartości własne znajdujemy, rozwiązując równanie charakterystyczne:

```text
det(A - λI) = 0
```

`I` oznacza macierz jednostkową o takim samym wymiarze jak `A`.
Rozwiązania tego równania to wartości własne macierzy.

## 3. Jak obliczyć wektory własne?

Dla każdej wartości własnej `λ` rozwiązujemy układ:

```text
(A - λI) · v = 0
```

Nietrywialne rozwiązanie `v` jest wektorem własnym odpowiadającym wartości
`λ`.

## 4. Przykład

Rozważmy macierz:

```text
       [ 2  3 ]
A  =   [ 1  4 ]
```

Jej wartości własne to:

```text
λ₁ = 5
λ₂ = 1
```

Odpowiadające wektory własne można zapisać jako:

```text
dla λ₁ = 5:  v₁ = [ 1,  1]
dla λ₂ = 1:  v₂ = [-3,  1]
```

Sprawdzenie:

```text
A · [1, 1]  = [5, 5]  = 5 · [1, 1]
A · [-3, 1] = [-3, 1] = 1 · [-3, 1]
```

NumPy może wypisać te same wektory w innej skali, na przykład
`[0.707, 0.707]`. Nadal wskazują one ten sam kierunek.

## 5. Własności pomocne w sprawdzaniu wyniku

Dla macierzy kwadratowej:

```text
suma wartości własnych = ślad macierzy
iloczyn wartości własnych = wyznacznik macierzy
```

W naszym przykładzie:

```text
5 + 1 = 6 = 2 + 4
5 · 1 = 5 = det(A)
```

## 6. Obliczenia w Pythonie

```python
import numpy as np

A = np.array([[2, 3],
              [1, 4]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Wartości własne:")
print(eigenvalues)

print("Wektory własne (kolumny):")
print(eigenvectors)
```

Kolejność wartości własnych może zależeć od wersji NumPy. Przykładowy wynik
może mieć przybliżoną postać:

```text
Wartości własne:
[1. 5.]

Wektory własne (kolumny):
[[-0.9486833  -0.70710678]
 [ 0.31622777 -0.70710678]]
```

Każda kolumna macierzy `eigenvectors` odpowiada wartości własnej na tej samej
pozycji w tablicy `eigenvalues`.
