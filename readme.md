# Firewall Zero

Firewall Zero é um jogo interativo desenvolvido em Django, onde os jogadores enfrentam desafios de hacking e tomam decisões que afetam o desenrolar da história. O jogo inclui vários mini-jogos de hacking, cada um com suas próprias mecânicas e desafios.

## Funcionalidades

- **Capítulos e Telas**: O jogo é dividido em capítulos, cada um com várias telas. Cada capítulo pode ter uma trilha sonora específica.
- **Mini-jogos de Hacking**: Inclui vários mini-jogos de hacking, como invasão, padrão, furtividade, complexo, clicker, entre outros.
- **Controle de Volume**: Os jogadores podem ajustar o volume da trilha sonora durante o jogo.
- **Persistência de Progresso**: O progresso do jogador é salvo e pode ser continuado posteriormente.

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/firewall-zero.git
    cd firewall-zero
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Aplique as migrações do banco de dados:
    ```sh
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:
    ```sh
    python manage.py runserver
    ```

6. Acesse o jogo no navegador:
    ```
    http://127.0.0.1:8000/
    ```

## Estrutura de Arquivos

- `firewall_zero/`: Diretório do projeto Django contendo configurações e URLs principais.
- `game/`: Diretório do aplicativo Django contendo modelos, visualizações, templates, arquivos estáticos e URLs específicas do jogo.
- `media/`: Diretório para armazenar arquivos de mídia, como imagens e trilhas sonoras.
- `static/`: Diretório para arquivos estáticos, como CSS e JavaScript.
- `templates/`: Diretório para templates HTML.

## Personalização

### Adicionar um Novo Capítulo

1. Crie um novo capítulo no Django Admin.
2. Adicione telas ao capítulo.
3. Configure a trilha sonora do capítulo, se necessário.

### Adicionar um Novo Mini-jogo de Hacking

1. Crie um novo tipo de mini-jogo no modelo `HackingMiniGame`.
2. Crie um template HTML para o mini-jogo.
3. Adicione a lógica do mini-jogo na view `hacking_mini_game_view`.

## Contribuição

1. Faça um fork do repositório.
2. Crie uma nova branch para sua feature ou correção de bug:
    ```sh
    git checkout -b feature/nova-feature
    ```
3. Commit suas mudanças:
    ```sh
    git commit -am 'Adiciona nova feature'
    ```
4. Faça push para a branch:
    ```sh
    git push origin feature/nova-feature
    ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Créditos

- Adonai Santos Fernandes: Historiador, Game Designer
- Alisson Andrade Nunes: Historiador, Game Developer
- Isaac Castro Silva: Historiador, Game Designer, Sound Effects
- Jairo Williams Guedes Lopes Neto: Game Designer, Game Developer
- João Victor Melo Fontes Linhares: Game Designer, Game Developer
- Josiely Alves Santos Prado: Historiador, Game Designer
- Leonardo dos Santos Feitoza: Historiador, Game Designer
- Raphael Moraes Goettenauer de Oliveira: Designer, Character Maker

Versão do jogo: 1.0.0