site = input("Digite a URL de um site: ")

if site.startswith("https:/"):
    print("Site confiável.")
else:
    print("Possível Risco.")