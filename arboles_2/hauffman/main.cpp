#include <iostream>
#include <fstream>
using namespace std;
void mostrar(char v[], int n){
    for (int i = 0; i < n; i++){
        cout << v[i] << " ";
    }
}
int frecuencia(char x){
    char letra;
    int contador = 0;

    ifstream entrada;
    entrada.open("E:/UNSA 2022 CC/semestre par/CC/discretas_2/Arboles/Arboles/arboles_2/string.txt");
    entrada >> letra;
    while( letra != 'x'){
        //cout << letra;
        if (letra == x)
            contador++;
        entrada >> letra;
    }
    return contador;
}

int main()
{
    //Algoritmo para obtener la cantidad de letras unicas:
    char letra;
    char v[10];
    int repeticiones = 0;
    int indice = 1;
    ifstream entrada;
    entrada.open("E:/UNSA 2022 CC/semestre par/CC/discretas_2/Arboles/arboles_2/hauffman/string.txt");
    entrada >> letra;

    v[0] = letra;


    while (letra != 'x'){

        for (int i = 0; i < indice; i++){

            if (letra == v[i])
                repeticiones += 1;
        }
        if (repeticiones == 0){
            v[indice] = letra;
            indice ++;
        }
        entrada >> letra;
        repeticiones = 0;
    }
    mostrar(v, 40);
    cout << indice;
    //cout << frecuencia('b');

}
