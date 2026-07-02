# 📍 Floripa Smart Tour - Roteiro Turístico Inteligente

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/SENAC-Jovem%20Programador-orange?style=for-the-badge" alt="SENAC">
  <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge" alt="Status">
</p>

<blockquote>
  <strong>"A Ilha da Magia na palma da sua mão, planejada de forma inteligente."</strong>
</blockquote>

---

## 📌 Sobre o Projeto

O **Floripa Smart Tour** é um sistema de recomendação de turismo desenvolvido como projeto prático para o programa **Jovem Programador (SENAC)**. 

O software foi idealizado para mitigar um problema real enfrentado por milhões de turistas que visitam Florianópolis anualmente: a dificuldade de consolidar informações espalhadas em blogs e redes sociais, o que gera perda de tempo precioso e frustração ao tentar conciliar rotas, interesses específicos, orçamento e acessibilidade.

---

## ⚡ O Desafio vs. Nossa Solução

### O Desafio
* ❌ Informações turísticas pulverizadas e descentralizadas.
* ❌ Alto tempo gasto pesquisando e comparando opções de lazer.
* ❌ Dificuldade de encontrar atrações perfeitamente compatíveis com o perfil (ex: locais pet friendly ou com acessibilidade motora).
* ❌ Desperdício de experiências devido à falta de planejamento logístico/geográfico eficaz.

### Nossa Solução
O sistema coleta as preferências exatas do usuário e gera de forma dinâmica um roteiro estruturado por ordem lógica de visitação. O usuário informa:
1. **Região(ões) da cidade** que deseja explorar (com suporte a seleção múltipla).
2. **Tipo de passeio** de preferência (Praia, História, Gastronomia, Natureza, Compras).
3. **Subtipo gastronômico** específico se aplicável (Churrascaria, Lanche, Oriental, Cafeteria/Padaria, Frutos do Mar).
4. **Filtros de inclusão**: Necessidade de acessibilidade motora e/ou se viaja acompanhado de um animal de estimação (Pet Friendly).

---

## 🚀 Funcionalidades e Diferenciais

* **Filtros Combinados Dinâmicos:** Cruzamento inteligente de dados para evitar sugestões incompatíveis.
* **Seleção Multi-Região:** Liberdade para escolher uma ou mais áreas da cidade de uma só vez (Centro, Norte, Sul, Leste, Lagoa e Continente).
* **Otimização de Rota:** O roteiro final é exibido e ordenado logicamente pelo atributo de proximidade geográfica (`ordem_visita`).
* **Interatividade (Check-in):** Simulação em console de um guia passo a passo, permitindo avançar as paradas do dia conforme o passeio acontece.

---

## 🛠️ Tecnologias Utilizadas

O projeto passou por uma evolução arquitetural, migrando de uma estrutura baseada em vetores paralelos em pseudocódigo (Portugol) para uma implementação em **Python**, utilizando estruturas de dados otimizadas (Dicionários e Listas):

* **Linguagem:** Python 3
* **Estruturas:** Mapeamento por chave-valor (Dicionários), List Comprehension e estruturas condicionais avançadas.
* **Biblioteca Nativa:** `os` (para manipulação e limpeza do terminal).

---

## 🚀 Como Executar o Projeto

Certifique-se de ter o Python instalado em sua máquina.

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/floripa-smart-tour.git](https://github.com/SEU-USUARIO/floripa-smart-tour.git)
   
2. **Navegue até a pasta do projeto:**
    ```bash
   cd floripa-smart-tour

4. **Execute o arquivo principal:**
    ```bash
    python nome_do_seu_arquivo.py

**Visão de Futuro (Potencial de Mercado)**
Este algoritmo serve como o núcleo de lógica para uma aplicação escalável de mercado. Os próximos passos mapeados para o projeto incluem:

🗺️ Integração com APIs de Mapas (Google Maps/Mapbox) para traçar rotas em tempo real.

📱 Desenvolvimento de uma interface de usuário mobile.

📅 Módulos para reservas online e avaliação de estabelecimentos.

🤝 Parcerias estratégicas com restaurantes, beach clubs e atrativos locais.

**Equipe de Desenvolvimento**
Malu Dalsasso
Nahyara Miranda
Raphaela Barreto

Desenvolvido para o ecossistema de tecnologia e turismo de Florianópolis.
