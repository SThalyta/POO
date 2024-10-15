import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite seu nome: ");
        String nome = sc.nextLine();
        System.out.println("Digite seu salario: ");
        double salario = sc.nextDouble();
        System.out.println("Digite o imposto: ");
        double imposto = sc.nextDouble();

        Empregado empregado = new Empregado(nome, salario, imposto);

        System.out.println("Nome:" +empregado.getNome());
        System.out.println("Salário Bruto:" +empregado.getSalario());
        System.out.println("Imposto:" +empregado.getImposto());

        System.out.println("Nome: " +empregado.getNome() +", " +empregado.netSalary());

        System.out.println("Qual a porcentagem de aumento?:");
        double porcentagem = sc.nextDouble();
        empregado.increaseSalary(porcentagem);
        System.out.println("Update data:" +empregado.getNome() +", " +empregado.getSalario());

        sc.close();

    }
}
