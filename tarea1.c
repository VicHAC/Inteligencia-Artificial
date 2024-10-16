#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ConcatenarCadenas(char *cadena1, char *cadena2, char *cadenaResultante);
void ObtenerPrefijos(char *cadenaResultante);
void ObtenerSufijos(char *cadenaResultante);
void ObtenerSubcadena(char *cadena, int inicio, int final);

int main() {
    char cadena1[100], cadena2[100], *cadenaResultante;
    int opcion, inicio, fin, potencia;
    cadenaResultante = (char *) malloc(200 * sizeof(char)); // tamaño grande para pruebas

    if (cadenaResultante == NULL) {
        printf("Error al asignar memoria\n");
        return 1;
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
void ObtenerSubsecuencia() {
    
}

// funcion para invertir cadena
void InvertirCadena() {
    
}

// funcion para la potencia de cadena
void PotenciarCadena() {
    
}