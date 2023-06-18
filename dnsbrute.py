import sys
import dns.resolver

resolver = dns.resolver.Resolver()

try:
    alvo = sys.argv[1]
    wordlist = sys.argv[2]
except IndexError:
    print("usage: python3 dnsbrute.py dominio wordlist.txt")
    sys.exit()

try:
    with open(wordlist, "r") as arq:
        subdominios = arq.read().splitlines()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
    sys.exit()
except IOError:
    print("Erro: Falha ao ler o arquivo")
    sys.exit()

total_subdominios = len(subdominios)
print(f"Total de subdomínios a serem testados: {total_subdominios}")

subdominios_encontrados = []

for index, subdominio in enumerate(subdominios, 1):
    try:
        sub_alvo = f"{subdominio}.{alvo}"
        resultados = resolver.resolve(sub_alvo, "A")
        for resultado in resultados:
            subdominios_encontrados.append(sub_alvo)
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.NoAnswer:
        pass
    except dns.exception.DNSException:
        pass

    print(f"Progresso: {index}/{total_subdominios}")

print("Subdomínios encontrados:")
if subdominios_encontrados:
    for subdominio_encontrado in subdominios_encontrados:
        print(subdominio_encontrado)
else:
    print("Nenhum subdomínio encontrado.")

print("Conclusão da execução do script.")
