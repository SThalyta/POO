import meuprojeto.pagamento.Pagamento;
import meuprojeto.pagamento.PagamentoCartao;
import meuprojeto.pagamento.PagamentoEmDinheiro;
import meuprojeto.pagamento.PagamentoEmPix;

public class Main {
    public static void main(String[] args) {
        Pagamento pagamentocartao = new PagamentoCartao("123-456-789", 220);
        pagamentocartao.processarPagamento();

        Pagamento pagamentoemdinheiro = new PagamentoEmDinheiro(360);
        pagamentoemdinheiro.processarPagamento();

        Pagamento pagamentoempix = new PagamentoEmPix("13022004", 180);
        pagamentoempix.processarPagamento();
    }
}