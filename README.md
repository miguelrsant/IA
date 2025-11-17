# TAYLOR — Business Super Intelligence Platform

**TAYLOR** é uma plataforma avançada de automação operacional e análise inteligente, projetada para transformar dados brutos em decisões estratégicas. Seu objetivo é permitir que qualquer empresa — independentemente do setor — aproveite o poder da IA para automatizar rotinas, gerar relatórios, visualizar dashboards e acompanhar o desempenho do negócio de forma flexível e personalizada.

---

## 🚀 Visão Geral

TAYLOR é um sistema completo composto por três pilares principais:

1. **Automação por Upload de Arquivos**
   Usuários podem enviar planilhas (Excel/CSV) contendo informações operacionais — pedidos, estoque, inventário, fornecedores — que serão automaticamente processadas, padronizadas e integradas aos modelos internos da plataforma.

2. **Chat Inteligente (NLP + Análises Operacionais)**
   Um assistente conversacional onde o usuário pede insights em linguagem natural:
   *"Me mostre o OTIF deste mês"*, *"Quais itens estão parados há mais de 60 dias?"*, *"Quais fornecedores mais atrasam?"*.
   As requisições são convertidas dinamicamente em consultas estruturadas, gerando análises, tabelas e gráficos.

3. **BSI — Business Super Intelligence**
   Um painel adaptável que apresenta visão macro do negócio, indicadores essenciais, narrativas inteligentes e alertas automáticos sobre riscos e oportunidades.

---

## 🎯 Objetivos do Projeto

* Criar uma plataforma robusta e escalável para análises automatizadas.
* Possibilitar que qualquer usuário obtenha relatórios avançados sem conhecimento técnico.
* Oferecer dashboards dinâmicos, configuráveis e inteligentes.
* Reduzir tempo operacional, melhorar eficiência e aumentar a qualidade das decisões.
* Adaptar o sistema a diferentes segmentos, lojas e modelos de operação.

---

## 🧠 Principais Funcionalidades

### 🔹 Upload e Processamento de Planilhas

* Suporte a CSV e XLSX.
* Pré-visualização e validação dos dados enviados.
* Mapeamento flexível de colunas para entidades internas.
* ETL automatizado com normalização e estruturação dos dados.

### 🔹 Chat Inteligente

* Consulta de métricas e relatórios via linguagem natural.
* Suporte a perguntas sobre fornecedores, estoque, pedidos, desempenho e muito mais.
* Respostas com tabelas, KPIs e gráficos gerados dinamicamente.

### 🔹 BSI — Business Super Intelligence

* Painel com visão macro do negócio.
* Cartões de desempenho, alertas e insights explicados por IA.
* KPIs essenciais como OTIF, aging de pedidos, estoque parado, giro de produto.
* Recomendações automáticas com base nos padrões detectados.

### 🔹 Autenticação e Gestão de Usuários

* Registro, login e controle de acesso.
* Suporte a múltiplas organizações (multi-tenant).

### 🔹 Exportações e Relatórios

* Exportação de relatórios em CSV e PDF.
* Geração automática de arquivos com indicadores críticos.

---

## 🏗️ Arquitetura da Solução

A plataforma segue uma arquitetura moderna orientada a serviços, totalmente conteinerizada.

### **Frontend (Next.js)**

* Interface responsiva e profissional.
* Autenticação, uploads, dashboards e chat.
* Comunicação com backend via REST.

### **Backend (Python + FastAPI)**

* Processamento de arquivos e ETL.
* API para métricas, relatórios e dashboards.
* Motor de NL → SQL para consultas no chat.
* Integração com modelo de IA.

### **Banco de Dados (PostgreSQL)**

* Estrutura relacional para dados normalizados.
* Suporte a múltiplas organizações.

### **Containerização (Docker)**

* Facilita desenvolvimento e deploy.
* Ambiente replicável para todos os serviços.

---

## 🛠️ Tecnologias Utilizadas

### **Frontend**

* Next.js
* React

### **Backend**

* Python
* FastAPI
* Pydantic

### **Data & Infra**

* PostgreSQL
* Redis (filas de processamento)
* Celery ou RQ (workers)
* Docker + Docker Compose

### **IA e Análises**

* Modelos de Linguagem (LLMs)
* Conversão dinâmica NL → SQL
* Geração automática de insights e narrativas

---

## 📊 Principais Indicadores (KPIs)

* **OTIF (On Time In Full)** por fornecedor e loja
* **Aging de pedidos** por faixa (0-7d, 8-30d, >30d)
* **Itens parados** (30/60/90 dias)
* **Giro de estoque**
* **Lead time médio por fornecedor**
* **Ruptura e cobertura de estoque**

---

## 🧩 Estrutura do Repositório

```
taylor/
├── backend/         # FastAPI + lógica de negócios
├── frontend/        # Next.js + UI
└── README.md        # Este arquivo
```

---

## 📌 Diferenciais da TAYLOR

* Adaptável a qualquer segmento: varejo, logística, indústria.
* Configuração flexível baseada no mapeamento das planilhas do cliente.
* IA integrada ao processo, não apenas como “chat”, mas como **motor analítico**.
* Dashboard que conta histórias, identifica padrões e faz recomendações.
* Plataforma moderna, escalável e preparada para crescimento.



**TAYLOR — Automatize. Analise. Evolua.**
