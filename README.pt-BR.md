# Automação de Retenção de Câmeras Meraki

Este projeto automatiza a coleta de informações de retenção de vídeo das câmeras Meraki em múltiplas organizações, utilizando a API Meraki e automação web com Selenium. O objetivo é facilitar auditorias e o gerenciamento de políticas de retenção de vídeo, centralizando os dados em um arquivo CSV.

## Caso de Uso

Automatiza o processo de login, coleta de inventário de câmeras e extração dos dias de retenção configurados em cada dispositivo Meraki MV. Ideal para equipes de TI que precisam monitorar e documentar a política de retenção de vídeo em ambientes corporativos.

## Stack Tecnológico

- Python 3.8+
- Selenium WebDriver
- Meraki Python SDK
- python-dotenv
- Google Chrome + ChromeDriver

## Status

Beta – Funcional, mas pode exigir ajustes para diferentes fluxos de autenticação ou mudanças no dashboard Meraki.

## Instalação

1. Clone o repositório:

   ```bash
   git clone <seu-repo-url>
   cd <seu-repo>
   ```

2. Instale as dependências usando o arquivo requirements.txt:

   ```bash
   pip install -r requirements.txt
   ```

3. Certifique-se de ter o Google Chrome instalado e o ChromeDriver compatível no PATH.

## Configuração

Crie um arquivo `.env` na raiz do projeto com as variáveis:

```env
MERAKI_API_KEY=SEU_API_KEY
MERAKI_USERNAME=seu@email.com
MERAKI_PASSWORD=sua_senha
```

## Uso

Execute o script principal:

```bash
python rpa.py
```

Durante a execução, siga as instruções no terminal para autenticação (incluindo 2FA, se necessário).

Os resultados serão salvos em `camera_retention.csv` com as colunas: organização, nome da câmera, serial e dias de retenção.

## Problemas Conhecidos

- O fluxo de login pode mudar conforme atualizações do dashboard Meraki.
- O script requer intervenção manual para autenticação 2FA.

## Ajuda

Abra uma issue neste repositório para dúvidas ou problemas.

## Contribuição

Contribuições são bem-vindas! Veja o arquivo [CONTRIBUTING.md](./CONTRIBUTING.md) para detalhes.

## Licença

Este código está licenciado sob a BSD 3-Clause License. Veja [LICENSE.txt](./LICENSE.txt) para detalhes.
