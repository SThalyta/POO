package meuprojeto.pagamento;

public class PagamentoEmDinheiro extends Pagamento{
    public PagamentoEmDinheiro(double valor){
        super(valor);
    }
    @Override
    public void processarPagamento(){
        System.out.println("Obrigada pela compra no valor de " + valor);
    }

    
}
