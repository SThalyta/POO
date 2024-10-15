import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        EstoqueProduto produto = new EstoqueProduto();

        int opcao;

        do {
            System.out.println("Escolha uma opcao:");
            System.out.println("1 - Cadastrar produto");
            System.out.println("2 - Excluir quantidade do estoque");
            System.out.println("3 - Exibir produto");
            System.out.println("0 - Sair");
            opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao) {
                case 1:
                    System.out.println("Digite a descricao do produto:");
                    String descricao = scanner.nextLine();
                    
                    System.out.println("Digite a quantidade:");
                    int quantidade = scanner.nextInt();

                    System.out.println("Digite o valor do produto:");
                    double valor = scanner.nextDouble();

                    produto.cadastrar(descricao, quantidade, valor);
                    System.out.println("Produto cadastrado com sucesso!");
                    break;

                case 2:
                    System.out.println("Digite a quantidade a ser removida do estoque:");
                    int qtdRemover = scanner.nextInt();
                    produto.removerQuantidade(qtdRemover);
                    break;

                case 3:
                    produto.exibirEstoque();
                    break;

                case 0:
                    System.out.println("Obrigada, tchau!");
                    break;

                default:
                    System.out.println("Escolha uma opcao valida!");
                    break;
            }

            System.out.println();

        } while (opcao != 0);

        scanner.close();
    }
}
