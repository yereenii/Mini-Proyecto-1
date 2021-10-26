import java.util.Scanner;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

//Clase principal
public class Programa1 {

	public static void main(String[] args){
		Scanner teclado = new Scanner(System.in);
	
		System.out.println("Inserte la ruta del archivo a leer:");
		String ruta = teclado.nextLine();
		
		Programa1 p1 =new Programa1();
		Programa1.Encabezados enc1 = p1.new Encabezados();

		enc1.comprobarEncabezado(ruta);
		
				
	}

	//Clase para el manejo de archivos
	public class Archivos {
	
		public int tamanioArchivo(String rutaArchivo) throws FileNotFoundException, IOException {
			String cadena;
			FileReader fr = new FileReader(rutaArchivo);
			BufferedReader br = new BufferedReader(fr);
			int contador = 0;
			while((cadena = br.readLine())!=null) {
            			contador++;
        		}
			br.close();	
			return contador;	
		}

		public String[] lecturaArchivos(String rutaArchivo) throws FileNotFoundException, IOException {
			String cadena;
			FileReader fr = new FileReader(rutaArchivo);
			BufferedReader br = new BufferedReader(fr);
			int total = tamanioArchivo(rutaArchivo);
			String[] cadenas = new String[total];
			int contador = 0;

			while((cadena = br.readLine())!=null) {
				cadenas[contador] = cadena;
            			contador++;
        		}
       			br.close();
			return cadenas;		
		}


	}


	//Clase para el manejo de encabezados
	public class Encabezados {

		public boolean verificarCadena(String cadena){

			String[] datos =  cadena.split(":");
			int cont = 0;

			for (int j=1; j < datos.length; j++){
				String cad = datos[j];
	
				for (int i = 0; i<cad.length();i++){
					if (Character.isDigit(cad.charAt(i)) || Character.isLetter(cad.charAt(i))) {
						cont++;
					}
				}
			}
			if (cont > 0) {
				return true;
			} else {
				return false;
			}
		}

		public void comprobarEncabezado(String rutaArchivo) {
			Programa1 p2 =new Programa1();
			Programa1.Archivos arc1 = p2.new Archivos();

			try {
  				String encabezado[] = arc1.lecturaArchivos(rutaArchivo);

				System.out.println("\nDiagnostico: \n");

				if (verificarCadena(encabezado[1])){
					System.out.println("Program name: Complete \n");
				} else {
					System.out.println("Program name: Incomplete \n");
				}

				if (verificarCadena(encabezado[2])){
					System.out.println("Name: Complete \n");
				} else {
					System.out.println("Name: Incomplete \n");
				}
				if (verificarCadena(encabezado[3])){
					System.out.println("Date: Complete \n");
				} else {
					System.out.println("Date: Incomplete \n");
				}
				if (verificarCadena(encabezado[4])){
				System.out.println("Description: Complete \n");
				} else {
					System.out.println("Description: Incomplete \n");
				}

			}
			catch(FileNotFoundException fnfe) {
  				System.out.println("No se encontró el archivo \n");
			}
			catch(IOException ioe) {
  				System.out.println("Error de entrada / salida \n");
			}
	
		}

	}

}






