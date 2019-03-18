package ejerciciosExcepciones;
/**
 * 	Modifica la clase Gato vista anteriormente añadiendo el método apareaCon.
 * Este método debe comprobar que los gatos son de distinto sexo, tras lo
 * cual, genera un nuevo gato. Por ejemplo, sería válido algo como Gato cria
 * = garfield.apareaCon(lisa). En caso de que los gatos sean del mismo sexo,
 * el método debe generar la excepción ExcepcionApareamientoImposible. Crea un
 * programa desde el que se pruebe el método.
 * @author d18momoa
 *
 */
public class Ejercicio02 {
	public static void main(String[] args) {
		GatoSimple garfield = new GatoSimple("macho");
		GatoSimple lisa = new GatoSimple("hembra");
		GatoSimple tom = new GatoSimple("macho");
		
		try {
			garfield.apareaCon(lisa);
			//garfield.apareaCon(tom);
		}catch(Exception e){
			System.err.println(e.getMessage());
		}
	}
}
