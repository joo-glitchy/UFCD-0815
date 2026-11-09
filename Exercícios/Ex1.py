

alunos=[]

while True:
    print("1 - Inserir")
    print("2 - Listar")
    print("0 - Sair")

    op=input("Escolha uma opção: ")

    if op == "1":
        print("-----------------")
        nome = input("Nome: ")
        idade = input("Idade: ")
        curso = input("Curso: ")

        
        aluno = {
            "nome": nome,
            "idade":idade,
            "curso":curso
        }
        alunos.append(aluno)
        print("INSERIDO")

    elif op == "2":
        if not alunos:
            print("nenhum aluno registado inda")
        else:
            print("\nlista de alunos")
            
            for aluno in  alunos:
                print(f"nome: {aluno["nome"]}")
                print(f"idade: {aluno["idade"]}")
                print(f"curso: {aluno["curso"]}")
                print("-"*15)  
    elif op == "0":
        print("terminou")
        break
    else:
        print("op invalida")

