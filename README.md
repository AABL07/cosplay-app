# 🎭 Cosplay Scoring App

Aplicativo Android para pontuação de concursos de cosplay, desenvolvido com Python + Kivy e compilado com Buildozer.

## 📱 Funcionalidades

- Cadastro de participantes com nome
- Avaliação por 3 juízes em 3 critérios:
  - 🎨 Fidelidade
  - 🔧 Complexidade
  - ✨ Acabamento
- Cálculo automático de média
- Ranking em tempo real
- Exclusão individual ou total de participantes

## 🏗️ Arquitetura

O projeto segue o padrão **MVP (Model - View - Presenter)**:
```
cosplay_app/
├── main.py # Ponto de entrada do app
├── buildozer.spec # Configuração de build Android
├── views/
│ └── cosplay_view.py # Interface gráfica (View)
├── presenter/
│ └── cosplay_presenter.py # Lógica de negócio (Presenter)
├── repository/
│ └── participante_repo.py # Acesso ao banco de dados (Model)
```

## 🛠️ Tecnologias
```
| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.x | Linguagem principal |
| Kivy | 2.x | Interface gráfica |
| SQLite | — | Banco de dados local |
| Buildozer | — | Compilação para Android |

## ⚙️ Como compilar

### Pré-requisitos

- WSL (Ubuntu) ou Linux
- Python 3.x
- Buildozer instalado
```
### Instalação do Buildozer

```bash
pip install buildozer
sudo apt install -y git zip unzip openjdk-17-jdk
```

Build
```bash
git clone https://github.com/seu-usuario/cosplay_app.git
cd cosplay_app
buildozer android debug
```
**O APK será gerado em bin/.**

Instalar no celular via ADB
```bash
# Listar dispositivos
adb devices

# Instalar
adb install bin/*.apk
```

📋 Pré-requisitos Android

- Android 8.0 (API 26) ou superior

- Habilitar "Fontes desconhecidas" para instalar o APK

🖥️ Desenvolvimento

Para editar o projeto, recomenda-se usar o VS Code com a extensão Remote - WSL:

1. Instale a extensão Remote - WSL

2. Conecte ao WSL: clique no ícone >< no canto inferior esquerdo

3. Abra a pasta: File → Open Folder → ~/cosplay_app

🚀 Roadmap

- Tela de Login

- Exportar ranking em PDF/TXT

- Tema visual personalizado

- Número de juízes configurável

- Tela de configurações do evento

📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.


Desenvolvido para a comunidade de cosplay 🎭
