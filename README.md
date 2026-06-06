# OBSERVER

## Sobre o Projeto

Este projeto consiste em um script de automação inteligente e reativo focado no monitoramento e gerenciamento dinâmico de arquivos do sistema operacional. Desenvolvido em Python, o script `watchdogs.py` atua em segundo plano vigiando uma pasta de entrada específica (geralmente a pasta de Downloads) e organiza automaticamente qualquer arquivo novo que seja adicionado a ela.

Diferente de scripts de execução manual, esta aplicação implementa um padrão de observador (Observer) contínuo. Assim que um novo download é concluído e o arquivo é detectado no diretório monitorado, o programa identifica sua extensão e o transfere de forma imediata e assíncrona para uma pasta de destino devidamente estruturada e organizada por categoria.

---

## Funcionalidades

* Monitoramento contínuo em tempo real de um diretório alvo (como a pasta de Downloads).
* Detecção instantânea de eventos de criação ou modificação de novos arquivos.
* Triagem automatizada que lê e classifica o tipo de dado com base em sua extensão de arquivo.
* Transferência e realocação imediata de arquivos para subpastas dedicadas, mantendo o ambiente limpo sem necessidade de intervenção manual.

---

## Tecnologias Utilizadas

* **Python 3**
* Biblioteca externa principal: `watchdog` (indicada pelo nome clássico do arquivo de controle `watchdogs.py`)
* Bibliotecas nativas auxiliares: `os`, `shutil`, `time`

---

## Objetivo

O principal objetivo deste projeto é criar um fluxo de trabalho automatizado de "Zero Cliques" para a limpeza de diretórios altamente rotativos. O foco técnico está no aprendizado de programação orientada a eventos no sistema operacional, utilizando loops de escuta ativos e manipuladores de eventos (*event handlers*) para reagir a alterações de I/O em tempo real.

---

## Aprendizados

Durante o desenvolvimento deste projeto, foram aplicados conceitos como:

* Utilização da biblioteca `watchdog` para instanciar um observador (`Observer`) e associar um manipulador de eventos de sistema de arquivos (`FileSystemEventHandler`).
* Captura e tratamento do evento específico `on_created` para disparar ações automáticas no momento exato em que um download é finalizado.
* Implementação de rotinas de atraso temporário ou tratamento de exceções para evitar a manipulação de arquivos que ainda estão sendo gravados no disco pelo navegador.
* Integração com funções avançadas dos módulos nativos `os` e `shutil` para renomear, mover e validar a integridade dos caminhos de destino.

---

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca necessária via terminal:
```bash
pip install watchdog
```

3. Acesse a pasta do projeto:

```bash
cd OBSERVER
```

4. Execute o script para iniciar o monitoramento em segundo plano:

```bash
python watchdogs.py
```

---

## Estrutura do Projeto
```text
OBSERVER/
│
├── watchdogs.py
└── README.md
```

---

## Licença
Este projeto foi desenvolvido exclusivamente para fins educacionais e de aprendizado.

Desenvolvido como prática avançada de automação de infraestrutura local e manipulação de eventos de sistema com Python, criando uma rotina inteligente de triagem automática para pastas de download.
