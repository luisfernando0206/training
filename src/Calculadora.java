import java.util.Scanner;

public class Calculadora {

	public static void main(String[] args) {
		Scanner leitor = new Scanner(System.in);
		//Criando uma variável capaz de armazenar valores numéricos com casas decimais
		double valor1;
		double valor2;
		double soma;
		
		System.out.println("Por favor, digite o primeiro valor");
		valor1 = leitor.nextDouble();
		
		System.out.println("Por favor, digite o segundo valor");
		valor2 = leitor.nextDouble();
		
		soma = valor1 + valor2;
		
		System.out.println("A soma entre dois valores informados é " + soma);
		
		leitor.close();
		
	}

}
