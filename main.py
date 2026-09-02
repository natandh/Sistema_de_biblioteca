'''Uma biblioteca deseja controlar empréstimos de livros. O sistema apresenta: 1 - Emprestar livro 2 
Devolver livro 3 - Consultar quantidade disponível 0 - Sair A biblioteca possui inicialmente 50 livros
disponíveis. Quando um livro é emprestado, a quantidade disponível diminui em 1. Quando um livro é
devolvido, a quantidade disponível aumenta em 1. O sistema não pode permitir empréstimo quando
não houver livros disponíveis. Também não deve permitir devolução quando não houver livros
emprestados. Responda: Quais variáveis são necessárias? Quais condições devem ser verificadas?
Qual estrutura mantém o menu funcionando? Como controlar a quantidade de livros emprestados'''

def menu_principal():
    quantidade = 50
    while True:
        print("="*30)
        print("Sistema da biblioteca")
        print("="*30)
        print("1 - Emprestar livro")
        print("2 - Devolver livro")
        print("3 - Consultar quantidade disponível")
        print("0 - Sair")

        opcao = (input("Informe a opção desejada: "))
        print("="*30)

        if opcao == "1":
            if quantidade > 0:
                quantidade -=1
            else:
                print("Não ha livros disponível!")
        
        elif opcao == "2":
            if quantidade < 50:
                quantidade +=1
            else:
                print("Não ha livros emprestados!")
        
        elif opcao == "3":
            print("quantidade de livros disponível: ", quantidade)
        
        elif opcao == "0":
            print("Obrigado por usar nosso sistema!")
            return False
        else:
            print("Opção invalida, tente novamente.")

menu_principal()