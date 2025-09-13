# Extrator de Vídeo para Boot Animation Android (com Chroma Key)

Um script Python para automatizar a criação de sequências de frames para boot animations do Android a partir de vídeos com fundo verde (green screen).

## Sobre o Projeto

Criar uma animação de boot (boot animation) para Android geralmente é um processo manual e tedioso que envolve editar um vídeo, exportar cada frame como uma imagem individual e renomeá-los sequencialmente. Este projeto nasceu da necessidade de automatizar completamente esse fluxo de trabalho.

Este script pega um vídeo com um objeto ou animação em um fundo verde, processa um intervalo de tempo específico, remove o fundo, redimensiona os frames para a resolução desejada e os salva como uma sequência de arquivos PNG com transparência, prontos para serem empacotados em um `bootanimation.zip`.

## Funcionalidades

- **Extração de Frames:** Extrai frames de arquivos de vídeo comuns (MP4, MKV, etc.).
- **Remoção de Fundo Verde (Chroma Key):** Isola e remove o fundo verde, gerando imagens com canal alfa (transparência).
- **Seleção de Intervalo de Tempo:** Permite definir o segundo exato de início e fim para a extração dos frames.
- **Redimensionamento Automático:** Redimensiona cada frame para uma resolução de destino específica, ideal para a tela do seu dispositivo.
- **Nomeação Padrão para Boot Animation:** Salva os arquivos com nomes sequenciais e preenchimento de zeros (ex: `frame_0000.png`), garantindo a ordem correta de reprodução.

## Pré-requisitos

Para executar este script, você precisará ter o Python 3 instalado, juntamente com as seguintes bibliotecas:

- OpenCV
- NumPy

Você pode instalá-las facilmente via `pip`:
```bash
pip install opencv-python numpy
```

## Como Usar

1. **Clone o repositório (ou baixe o script):**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio
   ```

2. **Coloque seu vídeo:**
   Adicione seu arquivo de vídeo (ex: `meu_video.mkv`) na pasta do projeto.

3. **Configure os parâmetros:**
   Abra o arquivo `processar_video.py` em um editor de texto e ajuste as variáveis na seção de configurações no topo do arquivo:

   ```python
   # --- CONFIGURAÇÕES ---
   VIDEO_PATH = 'seu_video.mkv'      # Caminho para o seu vídeo de entrada
   OUTPUT_DIR = 'part0'              # Pasta onde os frames serão salvos (padrão para boot animations)
   START_TIME_SEC = 1.0              # Tempo de início (em segundos)
   END_TIME_SEC = 2.0                # Tempo de fim (em segundos)

   # --- CONFIGURAÇÕES DE RESOLUÇÃO ---
   TARGET_WIDTH = 1440
   TARGET_HEIGHT = 2960

   # --- AJUSTE FINO DO CHROMA KEY ---
   # Altere estes valores para corresponder exatamente ao tom de verde do seu vídeo
   LOWER_GREEN = np.array([35, 100, 100])
   UPPER_GREEN = np.array([85, 255, 255])
   ```

4. **Execute o script:**
   Abra um terminal na pasta do projeto e execute:
   ```bash
   python processar_video.py
   ```

Ao final, uma pasta chamada `part0` será criada (ou preenchida) com todos os frames processados.

## Próximos Passos: Criando o `bootanimation.zip`

Após executar o script e obter a pasta `part0`, você precisa finalizar o pacote:

1. **Crie o arquivo `desc.txt`** ao lado da pasta `part0` com o conteúdo (ajuste o FPS se necessário):
   ```
   1440 2960 30
   p 0 0 part0
   ```

2. **Crie o arquivo ZIP (sem compressão):**
   No terminal, na pasta que contém `desc.txt` e `part0`, execute:
   ```bash
   zip -0qry bootanimation.zip desc.txt part0
   ```
O arquivo `bootanimation.zip` estará pronto para ser instalado em um dispositivo Android com acesso root.

## Como Contribuir

Contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

1. Faça um Fork do Projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## Autor

**Seu Nome** - [@seu-github](https://github.com/seu-github)

Link do Projeto: [https://github.com/seu-usuario/seu-repositorio](https://github.com/seu-usuario/seu-repositorio)
