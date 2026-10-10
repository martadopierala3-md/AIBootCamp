# Pochodne w uczeniu maszynowym

W uczeniu maszynowym pochodne są fundamentalnym narzędziem matematycznym używanym do trenowania modeli, a dokładniej do optymalizacji ich parametrów (wag), aby model popełniał jak najmniejsze błędy.

Oto proste wyjaśnienie, jak działają i do czego służą.

## Do czego służą pochodne w ML?

Głównym celem w uczeniu maszynowym jest zminimalizowanie tzw. funkcji straty (*Loss Function*), która mierzy, jak bardzo przewidywania modelu różnią się od rzeczywistych danych.

- **Wskaźnik kierunku**: pochodna mówi nam, jak zmiana danej wagi (parametru) wpłynie na błąd modelu.
- **Gradient**: w sieciach neuronowych oblicza się pochodne cząstkowe dla wielu wag jednocześnie — tworzą one wektor zwany gradientem.
- **Optymalizacja**: dzięki pochodnym algorytm wie, czy powinien zwiększyć, czy zmniejszyć daną wagę, aby zmniejszyć błąd.

## Jak to działa w praktyce? (algorytm Gradient Descent)

Wyobraź sobie, że stoisz na szczycie góry we mgle i chcesz zejść na sam dół (gdzie błąd wynosi zero). Nie widzisz drogi, ale pod stopami czujesz nachylenie terenu.

1. **Pochodna to właśnie to nachylenie**. Pokazuje, w którą stronę teren opada najszybciej.
2. **Krok w dół**: algorytm wykonuje mały krok w kierunku przeciwnym do pochodnej, czyli w stronę spadku.
3. **Propagacja wsteczna (*Backpropagation*)**: w sieciach neuronowych pochodne są przekazywane od końca sieci do jej początku, aby zaktualizować każdą pojedynczą wagę. Proces ten powtarza się tysiące razy, aż model „nauczy się” poprawnych wzorców.

## Jak oblicza się pochodne w algorytmie *Backpropagation*?

Podstawą jest **reguła łańcuchowa**: jeśli jedna wartość wpływa na drugą, a ta na funkcję straty, mnożymy pochodne kolejnych zależności. Najpierw wykonujemy przejście w przód, aby obliczyć przewidywanie i stratę, a następnie przejście wstecz, aby wyznaczyć wpływ wag i biasów na tę stratę.

### Przykład: pojedynczy neuron

Rozważmy neuron z funkcją aktywacji sigmoid:

```text
z = w · x + b
a = σ(z) = 1 / (1 + e⁻ᶻ)
L = 1/2 · (a - y)²
```

Gdzie `x` to wejście, `w` — waga, `b` — bias, `a` — przewidywanie, `y` — oczekiwana wartość, a `L` — funkcja straty.

Z reguły łańcuchowej:

```text
∂L/∂w = ∂L/∂a · ∂a/∂z · ∂z/∂w
```

Poszczególne pochodne wynoszą:

```text
∂L/∂a = a - y
∂a/∂z = a · (1 - a)       (pochodna funkcji sigmoid)
∂z/∂w = x
∂z/∂b = 1
```

Stąd:

```text
∂L/∂w = (a - y) · a · (1 - a) · x
∂L/∂b = (a - y) · a · (1 - a)
```

#### Obliczenie na liczbach

Przyjmijmy `x = 2`, `w = 0,5`, `b = 0` i `y = 1`.

1. **Przejście w przód**:

   ```text
   z = 0,5 · 2 + 0 = 1
   a = σ(1) ≈ 0,7311
   L = 1/2 · (0,7311 - 1)² ≈ 0,0362
   ```

2. **Przejście wstecz — obliczenie gradientów**:

   ```text
   ∂L/∂w ≈ (0,7311 - 1) · 0,7311 · (1 - 0,7311) · 2 ≈ -0,1058
   ∂L/∂b ≈ (0,7311 - 1) · 0,7311 · (1 - 0,7311) ≈ -0,0529
   ```

3. **Aktualizacja parametrów**: dla współczynnika uczenia `η = 0,1` wykonujemy krok gradient descent:

   ```text
   w_nowe = w - η · ∂L/∂w ≈ 0,5106
   b_nowe = b - η · ∂L/∂b ≈ 0,0053
   ```

Ujemne gradienty oznaczają w tym przykładzie, że zwiększenie wagi i biasu zmniejszy stratę. W praktyce gradienty oblicza się dla wszystkich parametrów modelu, a aktualizacje często wykonuje optymalizator, np. SGD lub Adam.

### Rozszerzenie na wiele warstw

Dla warstwy `l` oznaczmy jej wejście jako `a⁽ˡ⁻¹⁾`, wagi jako `W⁽ˡ⁾`, bias jako `b⁽ˡ⁾`, sumę ważoną jako `z⁽ˡ⁾`, a aktywacje jako `a⁽ˡ⁾`:

```text
z⁽ˡ⁾ = W⁽ˡ⁾ · a⁽ˡ⁻¹⁾ + b⁽ˡ⁾
a⁽ˡ⁾ = f(z⁽ˡ⁾)
```

Zaczynamy od warstwy wyjściowej i obliczamy jej błąd `δ`. Następnie przekazujemy go wstecz przez kolejne warstwy:

```text
δ⁽L⁾ = ∂L/∂a⁽L⁾ ⊙ f'(z⁽L⁾)
δ⁽ˡ⁾ = (W⁽ˡ⁺¹⁾)ᵀ · δ⁽ˡ⁺¹⁾ ⊙ f'(z⁽ˡ⁾)
∂L/∂W⁽ˡ⁾ = δ⁽ˡ⁾ · (a⁽ˡ⁻¹⁾)ᵀ
∂L/∂b⁽ˡ⁾ = δ⁽ˡ⁾
```

Symbol `⊙` oznacza mnożenie element po elemencie, a `L` w indeksie górnym oznacza ostatnią warstwę sieci. Gdy gradienty są już obliczone, optymalizator używa ich do aktualizacji parametrów. **Backpropagation oblicza gradienty; sam krok aktualizacji wykonuje algorytm optymalizacji.**

## Podsumowanie

Bez pochodnych współczesne uczenie maszynowe i sztuczna inteligencja — w tym głębokie sieci neuronowe, LLM i inne modele — nie mogłyby efektywnie się uczyć, ponieważ nie wiedziałyby, jak poprawiać swoje błędy.
