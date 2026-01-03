import requests
import sys
import time

# --- CORES ---
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
AZUL = "\033[96m"
RESET = "\033[0m"

# --- WORDLIST "TOP 90% DOS PROGRAMADORES" ---
# Esta lista contém os nomes mais usados em empresas reais.
wordlist = [
    # > Ambientes (Onde o ouro está escondido)
    "dev", "development", "stage", "staging", "homolog", "homologacao", 
    "prod", "production", "test", "testing", "beta", "sandbox", "demo", 
    "lab", "experiment", "new", "old", "bkp", "backup", "temp",
    
    # > Administrativo & Painéis
    "admin", "administrator", "adm", "painel", "panel", "dashboard", 
    "portal", "gestao", "manager", "management", "root", "suporte",
    "help", "helpdesk", "login", "auth", "signin", "register",
    
    # > Serviços & Tecnologia (APIs, Bancos)
    "api", "api-dev", "v1", "v2", "app", "apps", "mobile", "db", "sql", 
    "mysql", "database", "oracle", "elastic", "search", "graphql", 
    "cdn", "assets", "static", "images", "img", "files", "download",
    
    # > Infraestrutura & Redes
    "vpn", "remote", "access", "secure", "security", "firewall", 
    "proxy", "router", "gateway", "ns1", "ns2", "dns", "host",
    "cloud", "aws", "azure", "s3", "storage", "bucket", "docker",
    "jenkins", "gitlab", "git", "ci", "cd", "monitor", "status",
    
    # > Comuns Gerais
    "www", "www2", "web", "site", "blog", "shop", "loja", "store",
    "mail", "webmail", "email", "smtp", "imap", "pop", "exchange",
    "corp", "corporate", "intranet", "interno", "private", "public",
    "partner", "client", "cliente", "docs", "documentos"
]

def descobrir_subdominios(dominio):
    print(f"\n{AZUL}--- SUB-HUNTER V2.0 ---{RESET}")
    print(f"{AMARELO}[*] Alvo: {dominio}{RESET}")
    print(f"{AMARELO}[*] Carregando wordlist Hacker com {len(wordlist)} payloads...{RESET}\n")
    
    encontrados = 0
    
    # Headers para não parecer um robô simples
    headers_fake = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        for sub in wordlist:
            url_teste = f"http://{sub}.{dominio}"
            
            # Imprime o que está testando na mesma linha (efeito visual legal)
            sys.stdout.write(f"\r{AZUL}[*] Testando: {sub:<20}{RESET}")
            sys.stdout.flush()
            
            try:
                # Timeout curto (1s) para varrer rápido
                resposta = requests.get(url_teste, headers=headers_fake, timeout=1)
                
                if resposta.status_code == 200:
                    print(f"\r{VERDE}[+] ABERTO:     {url_teste} (200 OK)          {RESET}")
                    encontrados += 1
                elif resposta.status_code == 403:
                    print(f"\r{VERMELHO}[!] RESTRITO:   {url_teste} (403 Forbidden)   {RESET}")
                    encontrados += 1
                elif resposta.status_code == 401:
                    print(f"\r{AMARELO}[!] REQUER SENHA: {url_teste} (401 Unauthorized){RESET}")
                    encontrados += 1
                elif resposta.status_code in [301, 302]:
                    print(f"\r{AZUL}[~] REDIRECIONA: {url_teste} ({resposta.status_code})      {RESET}")
                    encontrados += 1
                    
            except requests.ConnectionError:
                pass
            except requests.Timeout:
                pass

    except KeyboardInterrupt:
        print(f"\n\n{VERMELHO}[!] Varredura interrompida.{RESET}")
        sys.exit()

    print(f"\n\n{AMARELO}--- FIM DA VARREDURA ---{RESET}")
    print(f"Total de subdomínios encontrados: {encontrados}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        alvo = sys.argv[1]
    else:
        alvo = input("Digite o domínio (ex: tesla.com): ")
    
    # Limpeza básica do input
    alvo = alvo.replace("http://", "").replace("https://", "").replace("/", "").strip()
    
    descobrir_subdominios(alvo)
