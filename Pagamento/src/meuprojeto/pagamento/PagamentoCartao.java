package meuprojeto.pagamento;

public class PagamentoCartao extends Pagamento {
    private String numero;

    public PagamentoCartao(String numero, double valor){
        super(valor);
        this.numero = numero;
    }
    @Override
    public void processarPagamento(){
        System.out.println("Efetuado o pagamento de " + valor +"no cartão de numero " + numero);
    }
    
}
