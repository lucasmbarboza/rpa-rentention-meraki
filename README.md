# Meraki Camera Retention RPA

Este projeto é um RPA (Robotic Process Automation) em Python para automatizar a coleta de informações de retenção de vídeo de câmeras Meraki em múltiplas organizações, utilizando a API Meraki e automação web com Selenium.

## Funcionalidades
- Autenticação automática no dashboard web da Meraki (com suporte a 2FA manual).
- Coleta de todas as organizações e câmeras do dashboard via API.
- Abertura automática das páginas de configuração de retenção de cada câmera.
- Extração e registro dos dias de retenção de vídeo de cada câmera.
- Armazenamento dos dados em um arquivo CSV (`camera_retention.csv`).
- Logging detalhado de todas as etapas e erros.

## Requisitos
- Python 3.8+
- Google Chrome instalado
- ChromeDriver compatível com sua versão do Chrome

### Bibliotecas Python
- selenium
- meraki
- python-dotenv

Instale as dependências com:
```bash
pip install selenium meraki python-dotenv
```

## Configuração
1. Crie um arquivo `.env` na raiz do projeto com as variáveis:
   ```env
   MERAKI_API_KEY=SEU_API_KEY
   MERAKI_USERNAME=seu@email.com
   MERAKI_PASSWORD=sua_senha
   ```
2. Certifique-se de que o `chromedriver` está no PATH ou na mesma pasta do script.

## Uso
Execute o script principal:
```bash
python rpa.py
```

Durante a execução, se houver autenticação em duas etapas (2FA), siga as instruções no terminal.

Os resultados serão salvos em `camera_retention.csv` com as colunas: organização, nome da câmera, serial e dias de retenção.

## Observações
- O script foi projetado para uso interno e pode precisar de ajustes para diferentes ambientes ou versões do dashboard Meraki.
- O login web pode exigir adaptações caso o fluxo de autenticação da Meraki mude.

## Licença
Este projeto é fornecido sem garantia e para fins educacionais/demonstrativos.
