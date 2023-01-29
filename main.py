PLACEHOLDER = "[nome]"


with open("D:\Kaell\Programação\ProvasDlunos\Discentes\pessoas.txt") as nomes:
    nomes_lista = nomes.readlines()
    print(nomes_lista)


with open ("D:\Kaell\Programação\ProvasDlunos\Provas\prova.txt") as provas:
    prova_conteudo = provas.read()
    for alunos in nomes_lista:
        stripped_aluno = alunos.strip()
        nova_prova = prova_conteudo.replace(PLACEHOLDER, stripped_aluno)
        print(nova_prova)
        with open(f"D:\Kaell\Programação\ProvasDlunos\ProvasAtu\{stripped_aluno}prova.txt", "w") as final_prova:
            final_prova.write(nova_prova)

