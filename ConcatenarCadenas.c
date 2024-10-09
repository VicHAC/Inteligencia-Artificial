#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ConcatenarCadenas(char *cadena1, char *cadena2, char *cadenaResultante);
void ObtenerPrefijos(char *cadenaResultante);
void ObtenerSufijos(char *cadenaResultante);
void ObtenerSubcadena(char *cadena, int inicio, int final);
void ObtenerSubsecuencia(char *cadena);
void InvertirCadena(char *cadena);
void PotenciaCadena(char *cadena, int n);

int main() {
    char cadena1[100], cadena2[100], *cadenaResultante;
    int opcion, inicio, fin, potencia;
    cadenaResultante = (char *) malloc(200 * sizeof(char)); // tamaño grande para pruebas

    if (cadenaResultante == NULL) {
        printf("Error al asignar memoria\n");
        return 1;
    }

    while (1) {
        printf("\n--- Menu de Operaciones con Cadenas ---\n");
        printf("1. Concatenar dos cadenas\n");
        printf("2. Obtener prefijos de la cadena\n");
        printf("3. Obtener sufijos de la cadena\n");
        printf("4. Obtener subcadena\n");
        printf("5. Obtener subsecuencia\n");
        printf("6. Invertir cadena\n");
        printf("7. Potencia de la cadena\n");
        printf("8. Salir\n");
        printf("Seleccione una opcion: ");
        scanf("%d", &opcion);

        switch (opcion) {
            case 1:
                printf("Ingrese la primera cadena: ");
                scanf("%s", cadena1);
                printf("Ingrese la segunda cadena: ");
                scanf("%s", cadena2);
                ConcatenarCadenas(cadena1, cadena2, cadenaResultante);
                break;

            case 2:
                printf("Ingrese la cadena: ");
                scanf("%s", cadenaResultante);
                ObtenerPrefijos(cadenaResultante);
                break;

            case 3:
                printf("Ingrese la cadena: ");
                scanf("%s", cadenaResultante);
                ObtenerSufijos(cadenaResultante);
                break;

            case 4:
                printf("Ingrese la cadena: ");
                scanf("%s", cadenaResultante);
                printf("Ingrese el índice de inicio: ");
                scanf("%d", &inicio);
                printf("Ingrese el índice de fin: ");
                scanf("%d", &fin);
                ObtenerSubcadena(cadenaResultante, inicio, fin);
                break;

            case 5:
                printf("Ingrese la cadena: ");
                scanf("%s", cadenaResultante);
                ObtenerSubsecuencia(cadenaResultante);
                break;

            case 6:
                printf("Ingrese la cadena: ");
                scanf("%s", cadenaResultante);
                printf("Cadena invertida: ");
                InvertirCadena(cadenaResultante);
                break;

            case 7:
                printf("Ingrese la cadena: ");
                scanf("%s", cadenaResultante);
                printf("Ingrese la potencia (positivo para repetir, 0 para vacía, negativo para invertir): ");
                scanf("%d", &potencia);
                PotenciaCadena(cadenaResultante, potencia);
                break;

            case 8:
                free(cadenaResultante);
                printf("Saliendo...\n");
                return 0;

            default:
                printf("Opción inválida. Intente nuevamente.\n");
                break;
        }
    }

    return 0;
}

// funcion para concatenar cadenas
void ConcatenarCadenas(char *cadena1, char *cadena2, char *cadenaResultante) {
    int i, j;
    for (i = 0; i < strlen(cadena1); i++) {
        cadenaResultante[i] = cadena1[i];
    }
    for (j = 0; j < strlen(cadena2); j++) {
        cadenaResultante[i + j] = cadena2[j];
    }
    cadenaResultante[i + j] = '\0'; // Asegurarse de que termine en null
    printf("Cadena Concatenada: %s\n", cadenaResultante);
}

// funcion para obtener los prefijos
void ObtenerPrefijos(char *cadena){
    int i, j;
    for(i = 0; i < strlen(cadena); i++){
        for(j = 0; j <= i; j++){
            printf("%c", cadena[j]);
        }
        printf("\n");
    }
}

// funcion para obtener los sufijos
void ObtenerSufijos(char *cadena){
    int i, j;
    for(i = strlen(cadena) - 1; i >= 0; i--){
        for(j = i; j < strlen(cadena); j++){
            printf("%c", cadena[j]);
        }
        printf("\n");
    }
}

// funcion para obtener una subcadena
void ObtenerSubcadena(char *cadena, int inicio, int final){
    int i = 0;
    printf("\nSubcadena: ");
    for(i = inicio; i <= final; i++){
        printf("%c", cadena[i]);
    }
    printf("\n");
}

// funcion para obtener una subsecuencia
void ObtenerSubsecuencia(char *cadena) {
    int n = strlen(cadena);
    printf("\nSubsecuencia: ");
    for (int i = 0; i < n; i += 2) {  // Aquí obtendremos una subsecuencia tomando caracteres alternos
        printf("%c", cadena[i]);
    }
    printf("\n");
}

// funcion para invertir cadena
void InvertirCadena(char *cadena) {
    int n = strlen(cadena);
    for (int i = n - 1; i >= 0; i--) {
        printf("%c", cadena[i]);
    }
    printf("\n");
}

// funcion para la potencia de cadena
void PotenciaCadena(char *cadena, int n) {
    if (n == 0) {
        printf(""); // cadena vacía
    } else if (n > 0) {
        for (int i = 0; i < n; i++) {
            printf("%s", cadena);
        }
    } else { // n es negativo, se invierte la cadena
        InvertirCadena(cadena);
    }
    printf("\n");
}