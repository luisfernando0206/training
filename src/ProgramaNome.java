import java.util.Scanner;

// Este programa deve receber o nome do usu�rio e exibir uma mensagem de boas vindas.
public class ProgramaNome {

	public static void main(String[] args) {
		// A linha abaixo cria um leitor para lermos o teclado do usu�rio.
		Scanner leitor = new Scanner(System.in);
		
		//A linha abaixo pega o texto digitado pelo usu�rio e guarda na vari�vel nome
		String nome;
		
		System.out.println("Por favor, digite seu nome:");
		//A linha abaixo pega o texto digitado pelo usu�rio e guarda na vari�vel "nome"
		nome = leitor.next();
		
		//Para lermos texto com espa�o, podemos usar o nextLine:
		//nome = leitor.nextLine(); 
		
		//Este c�digo l� um texto do teclado do usu�rio
		System.out.println("Que legal que seu nome � " + nome);
		
		System.out.println(nome + ", fico feliz que voc� esteja usando meu programa");
		
		//Ap�s terminarmos de usar o leitor, precisamos fechar
		leitor.close();
	
	}

}
