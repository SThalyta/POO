public class EstoqueProduto {
    
    private String descricao;
    private int quantidade;
    private double valor;

    public void cadastrar(String descricao, int quantidade, double valor){
        this.descricao = descricao;
        this.quantidade = quantidade;
        this.valor = valor;
    }

        public String getDescricao() {
            return descricao;
        }
    
        public void setDescricao(String descricao) {
            this.descricao = descricao;
        }
    
        public int getQuantidade() {
            return quantidade;
        }
    
        public void setQuantidade(int quantidade) {
            this.quantidade = quantidade;
        }
    
        public double getValor() {
            return valor;
        }
    
        public void setValor(double valor) {
            this.valor = valor;
        }

        public void removerQuantidade(int quantidade) {
            if (quantidade <= this.quantidade) {
                this.quantidade -= quantidade;
            } else {
                System.out.println("Quantidade insuficiente em estoque.");
            }
        }

        public void exibirEstoque() {
            System.out.println("Descricao: " + descricao);
            System.out.println("Quantidade: " + quantidade);
            System.out.println("Valor: " + valor);
        }


}
