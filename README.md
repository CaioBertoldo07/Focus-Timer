# ⏱️ Focus Timer — Aplicativo Anti-Distração

## 📌 Visão Geral

O **Focus Timer** é um aplicativo desktop desenvolvido em Python com interface gráfica, criado para ajudar usuários a manterem o foco durante estudos ou trabalho. Ele utiliza sessões cronometradas de foco e pausa, registrando automaticamente o progresso diário.

O projeto segue uma proposta **minimalista**, evitando excesso de funcionalidades e distrações visuais, priorizando simplicidade, clareza e uso prático no dia a dia.

---

## 🎯 Objetivo do Projeto

* Reduzir distrações digitais durante períodos de foco
* Incentivar constância através de sessões cronometradas
* Registrar automaticamente sessões concluídas
* Servir como projeto prático para aprendizado de:

  * Interface gráfica com Python
  * Gerenciamento de estado
  * Persistência de dados
  * Organização e evolução de projetos

---

## 👤 Público-alvo

* Estudantes
* Pessoas que estudam ou trabalham em home office
* Usuários que desejam melhorar foco e disciplina
* Desenvolvedores iniciantes/intermediários em Python

---

## 🧱 Funcionalidades (Versão 1 — MVP)

### ⏱️ Timer de Foco

* Sessões padrão de **25 minutos**
* Exibição do tempo restante em formato **MM:SS**
* Atualização em tempo real sem travar a interface

### ☕ Modo Pausa

* Pausa curta de **5 minutos**
* Iniciada manualmente pelo usuário
* Timer independente da sessão de foco

### ▶️ Controle do Timer

* Botão **Iniciar / Pausar**
* Controle interno do estado do timer
* Retomada do tempo exatamente de onde foi pausado

### 📊 Contador de Sessões Diárias

* Registro automático de cada sessão concluída
* Exibição do número de sessões realizadas no dia atual
* Atualização imediata após o término de cada sessão

### 💾 Persistência de Dados

* Armazenamento local em arquivo `.json`
* Cada sessão registrada contém:

  * Data
  * Horário
  * Tipo de sessão
* Histórico preservado entre execuções do aplicativo

---

## 🖥️ Interface Gráfica

A interface é desenvolvida com **Tkinter**, mantendo um layout simples e funcional.

### Elementos da Interface

* Timer central em destaque
* Botão de controle de foco
* Botão de pausa
* Indicador de sessões realizadas no dia

### Princípios de Design

* Poucos elementos na tela
* Fonte grande para facilitar leitura
* Ausência de distrações visuais
* Foco total na função principal do aplicativo

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Tkinter** — Interface gráfica
* **JSON** — Persistência de dados
* **datetime** — Controle de datas e horários
* **Event Loop (`after`)** — Atualização do timer sem bloqueio

---

## 🗂️ Estrutura do Projeto

```
focus_timer/
 ├─ app.py           # Código principal do aplicativo
 ├─ sessions.json    # Histórico de sessões
 └─ README.md        # Documentação do projeto
```

---

## 🔄 Fluxo de Funcionamento

1. O usuário inicia o aplicativo
2. O sistema carrega o histórico de sessões do dia atual
3. O usuário inicia uma sessão de foco
4. O timer inicia a contagem regressiva
5. Ao zerar o tempo:

   * A sessão é registrada automaticamente
   * O contador diário é atualizado
   * O timer retorna ao estado inicial
6. O usuário pode iniciar uma nova sessão, fazer uma pausa ou encerrar o aplicativo

---

## 🚀 Evoluções Planejadas

### Versão 2

* Tema escuro
* Alerta sonoro ao finalizar sessões
* Estatísticas semanais
* Personalização do tempo de foco

### Versão 3

* Bloqueio de sites ou aplicativos durante o foco
* Exportação de relatórios
* Modo “hard focus”
* Geração de executável (.exe)

---

## 🧩 Diferenciais do Projeto

* Simples o suficiente para uso diário
* Funcional e aplicável à vida real
* Fácil de evoluir conforme novos aprendizados
* Une produtividade pessoal e prática de programação

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado
2. Clone ou baixe este repositório
3. No diretório do projeto, execute:

```bash
python app.py
```

---

## 📄 Licença

Projeto de uso educacional e pessoal. Livre para modificações e melhorias.


