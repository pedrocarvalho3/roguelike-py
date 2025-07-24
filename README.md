# 🐍 Roguelike em Python

Um pequeno projeto de **Roguelike em Python**, feito com o objetivo de revisar os conhecimentos fundamentais de programação e, claro, me divertir enquanto programo!

---

## 🎯 Objetivos

- Revisar fundamentos da programação:
  - Estruturas de dados (listas, dicionários, filas, pilhas)
  - Orientação a objetos (OOP)
  - Modularização e organização de código
  - Controle de fluxo e estruturas condicionais
  - Entrada/saída e manipulação de arquivos (opcional)
- Praticar boas práticas de desenvolvimento
- Criar um jogo jogável e expandível
- Explorar mecânicas clássicas de roguelike
- Aprender se divertindo!

---

## 🧱 Funcionalidades (planejadas)

- [x] Geração de mapa simples (grade de salas ou labirinto)
- [x] Movimentação do jogador com teclado
- [ ] Combate básico (jogador vs inimigos)
- [ ] Sistema de turnos
- [ ] Inventário e coleta de itens
- [ ] HUD básica com status do jogador
- [ ] Salvar e carregar jogo (extra)
- [ ] Interface com biblioteca gráfica (ex: `curses`, `pygame` ou `tcod`) – opcional

---

## 🛠️ Tecnologias

- **Python 3**
- [tcod (libtcod)](https://python-tcod.readthedocs.io/en/latest/) (para gráficos estilo terminal – opcional)
- Modo texto puro para início simples

---

## 📁 Estrutura do Projeto

```bash
roguelike/
├── main.py               # Loop principal do jogo
├── map.py                # Geração e renderização do mapa
├── player.py             # Classe do jogador
├── enemy.py              # Classe base para inimigos
├── engine.py             # Lógica de jogo (movimento, turnos)
├── ui.py                 # Interface e renderização no terminal
└── README.md             # Este arquivo
```
