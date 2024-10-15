public class Empregado {

    private String nome;
    private double salario;
    private double imposto;

    public Empregado(String nome, double salario, double imposto){
        this.nome = nome;
        this.salario = salario;
        this.imposto = imposto;
    }

    public double netSalary(){
        return salario - imposto;
    }
    public void increaseSalary(double porcentagem){
        double salarioLiquido = netSalary();
        this.salario = ((porcentagem/100) * salario) + salarioLiquido;
    }
    
    public String getNome(){
        return nome;
    }

    public double getSalario(){
        return salario;
    }

    public double getImposto(){
        return imposto;
    }

}
