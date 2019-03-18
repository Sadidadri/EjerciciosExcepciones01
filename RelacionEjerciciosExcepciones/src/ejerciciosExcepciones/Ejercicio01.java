package ejerciciosExcepciones;

import java.util.Scanner;

/**
 * Realiza un programa que pida 6 n�meros por teclado y nos diga cu�l es el
 * m�ximo. Si el usuario introduce un dato err�neo (algo que no sea un n�mero
 * entero) el programa debe indicarlo y debe pedir de nuevo el n�mero.
 * @author d18momoa
 *
 */
public class Ejercicio01 {

	public static void main(String[] args) {
		//Declaracion del scanner que leera los valores del usuario
		Scanner entrada = new Scanner(System.in);
		//Variable que ira recogiendo el valor maximo
		int maximo = Integer.MIN_VALUE;
		//Variable que el usuario ira introduciendo en cada pasada
		int numeroPedido;
		//Booleano que comprueba si el valor introducido es verdadero o falso
		boolean valido;
		System.out.println("Introduzca 6 numeros y veremos cual es el mayor.");
		for(int i = 0;i<6;i++) {
			do {
				try {
					System.out.println("Introduzca el numero "+(i+1));
					numeroPedido = entrada.nextInt();
					valido = true;
					if (maximo < numeroPedido) {
						maximo = numeroPedido;
					}
				}catch(Exception e){
					entrada.nextLine();
					System.err.println("Error, has introducido un valor incorrecto");
					valido = false;
				}
			}while(!valido);
		}	
		System.out.println("El valor maximo es "+maximo);
		
	}
}
