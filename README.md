# Desafio Codeforces — Mentoria Codificadas | Além do Código
 
## Sobre este repositório
 
Este repositório contém minha resolução para o desafio de programação proposto na mentoria, utilizando problemas da plataforma [Codeforces](https://codeforces.com/) com auxílio de Inteligência Artificial.
 
---
 
## Problemas escolhidos
 
| # | Nome do problema | Link | Dificuldade |
|---|-----------------|------|-------------|
| 2231F | Quadratic Jumps | [Ver no Codeforces](https://codeforces.com/contest/2231/problem/F) | 2600 |
| 236A | Boy or Girl | [Ver no Codeforces](https://codeforces.com/contest/236/problem/A) | 800 |
| 4A | Watermelon | [Ver no Codeforces](https://codeforces.com/contest/4/problem/A) | 800 |

 
## Problema 1 — [ Quadratic Jumps]
 
### O que o problema pede?
Resolução de casas númeriicas com distancias de quadrados perfeitos e com o menor número de pulos para chegar ao distino sem usar BFS. 
 
 
### Como eu resolvi?
Entendendo cada vértice e tranformando os graficos em problemas numéricos, separando a distancia entre as duas vértices e pensando somente em qual o menor número que eu presico somar ou subtrair para obter a diferença. Usei o Teorema de Lagrange onde o número inteiro pode ser escrito como soma no máximo 4 quadrados e analisando que a distância entre duas vértices dependem apenas da diferença entre elas.
 
### Código
```python
import sys

MAX_VAL = 200000
dist = [4] * (MAX_VAL + 1)
dist[0] = 0
squares = [i*i for i in range(1, int(MAX_VAL**0.5) + 1)]

def precompute_distances():
  for s in squares: dist[s] = 1
  for a in squares:
    for b in squares:
      if a+b <= MAX_VAL: dist[a+b] = min(dist[a+b], 2)
      if abs(a-b) <= MAX_VAL: dist[abs(a-b)] = min(dist[abs(a-b)], 2)
  for i in range(MAX_VAL + 1):
    if dist[i] <= 2:
      for s in squares:
        if i+s <= MAX_VAL: dist[i+s] = min(dist[i+s], 3)
        if abs(i-s) <= MAX_VAL: dist[abs(i-s)] = min(dist[abs(i-s)], 3)

precompute_distances()

 #Leitura da entrada: quantidade de casos t
line = sys.stdin.readline()
if line:
  t = int(line.strip())
  for _ in range(t):
    n, q = map(int, sys.stdin.readline().split())
    for _ in range(q):
      a, b = map(int, sys.stdin.readline().split())
      print(dist[abs(a - b)])
```
---
 
## Problema 2 — [Boy or Girl ]
 
### O que o problema pede?
Se o nome do usuare tiver uma quantidade ímpar deve imprimi: "IGNORE HIM!" e se tiver uma quantidade par deve imprimir: "chat with her!".
 
### Como eu resolvi?
Ultilisando o set() para remover os  caracteres repetidos juntamente com o len() para obter a quantidade de letras, depois verificando a paridade com % 2 == 0 e por fim usando if e else para imprimir a saida correspondente.
 
### Código
```python
namo = input()

caracteres_distintos = len(set(namo))

if caracteres_distintos % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
```
---

## Problema 3 — [Watermelon]
 
### O que o problema pede?
 Pedro e Billy querem dividir sua melancia em duas partes sem deixar uma das partes sem melancia, encontrando assim uma resolução que imprima "YES" ou "NO" dependendo do kg da melancia.
 
### Como eu resolvi?
 Indentificando primeiro o peso da melancia como impar ou par pois se a melancia tivesse o número impar não poderia ser divida em duas partes iguais então useia a operação % 2 == 0 e por fim usando if e else para imprimir a saida correspondente.
 
### Código
```python
peso = int(input())

resto = peso % 2

if resto == 0:
    print("YES")
else:
    print("NO")
```
---
 
## IA utilizada
 
**Qual IA você usou?**
ClaudGPT
 
**Como a IA te ajudou?**
Ultilisei para analisar minhas soluções e indentificar erros de emtrada ou saida dos meus problemas exigindo uma explicação clara e objetiva.

## Reflexão
 
### Dificuldades encontradas
Tive mas dificuldade para entender oque realmente era a problematica para encontrar a solução.
 
 
### O que aprendi
Aprendi que a formas mas rapidas para resolução problemas em Python tanto em questão de tempo de resposta e também na quantidade de linhas.
 
 
### Como foi a experiência?
Eu gostei dos disafios e de ter a oportunidade esta tendo a experiencia poder navegar pelo sistema da Codeforces.
