import sys
import dns.resolver
#importando as livrarias

resolver = dns.resolver.Resolver()
#criando a função

try:
	alvo = sys.argv[1]
	wordlist = sys.argv[2]
except:
	print("usage: python3 dnsbrute.py dominio  wordlist.txt")
	sys.exit()
#aqui estamos dizendo para o usuario colocar 2 argumentos, alvo e wordlist, e caso tenha erro, ele volta o print mostrando um exemplo de uso
	
try:
	with open(wordlist,"r") as arq:
		subdominios = arq.read().splitlines()
except:
	print("Erro ao abrir arquivo")
	sys.exit()
#aqui pedimos para abrir o arquivo wordlist, e definimos o subdominio como 
	
for subdominio in subdominios:
	try:
		sub_alvo = "{}.{}".format(subdominio, alvo)
		resultados = resolver.resolve(sub_alvo,"A")
		for resultado  in resultados:
			print("{} -> {}".format(sub_alvo, resultado))
	except:
		pass
