# 🌐 Sub-Hunter - Subdomain Discovery Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)

Ferramenta de reconhecimento (Recon) focada em **descoberta de subdomínios**. O script utiliza uma wordlist otimizada com os termos mais utilizados por desenvolvedores e infraestrutura (ex: `dev`, `stage`, `admin`, `vpn`) para encontrar "portas dos fundos" em servidores alvo.

## 🚀 Funcionalidades

* **[+] Wordlist Inteligente:** Mais de 100 payloads focados em ambientes reais corporativos.
* **[+] Detecção de Status:** Identifica não apenas o que está aberto (200), mas também o que é restrito (403) ou requer senha (401).
* **[+] User-Agent Spoofing:** Simula um acesso via navegador para evitar bloqueios simples.
* **[+] Multi-Thread Speed:** (Em breve na V3.0)

## 🛠️ Instalação

```bash
# 1. Clone o repositório
git clone [https://github.com/brunopark852/sub-hunter.git](https://github.com/brunopark852/sub-hunter.git)

# 2. Entre na pasta
cd sub-hunter

# 3. Instale as dependências
💻 Como Usar
Bash

python3 sub-hunter.py

Insira o domínio alvo (sem http/https), exemplo: tesla.com

Exemplo de Saída:
Plaintext

[*] Alvo: tesla.com
[*] Carregando wordlist Hacker...

[!] RESTRITO:   [http://shop.tesla.com](http://shop.tesla.com) (403 Forbidden)
[+] ABERTO:     [http://sso.tesla.com](http://sso.tesla.com) (200 OK)
[!] REQUER SENHA: [http://vpn.tesla.com](http://vpn.tesla.com) (401 Unauthorized)

⚠️ Disclaimer

Ferramenta desenvolvida para fins educacionais e testes autorizados (Bug Bounty). O autor não se responsabiliza pelo uso indevido.

Dev: Bruno Rodrigo 💀
pip install requests
