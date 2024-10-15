package meuprojeto.pagamento;

public class PagamentoEmPix extends Pagamento {
    private String chave;

    public PagamentoEmPix(String chave, double valor) {
        super(valor);
        this.chave = chave;
    }

    @Override
    public void processarPagamento() {
        System.out.println("Efetuado o pagamento de " + valor + " na chave pix " + chave);
    }
}

