import java.util.Scanner;

// Este programa deve receber o nome do usuário e exibir uma mensagem de boas vindas.
public class ProgramaNome {

	public static void main(String[] args) {
		// A linha abaixo cria um leitor para lermos o teclado do usuário.
		Scanner leitor = new Scanner(System.in);
		
		//A linha abaixo pega o texto digitado pelo usuário e guarda na variável nome
		String nome;
		
		System.out.println("Por favor, digite seu nome:");
		//A linha abaixo pega o texto digitado pelo usuário e guarda na variável "nome"
		nome = leitor.next();
		
		//Para lermos texto com espaço, podemos usar o nextLine:
		//nome = leitor.nextLine(); 
		
		//Este código lê um texto do teclado do usuário
		System.out.println("Que legal que seu nome é " + nome);
		
		System.out.println(nome + ", fico feliz que você esteja usando meu programa");
		
		//Após terminarmos de usar o leitor, precisamos fechar
		leitor.close();
	
	}

}
