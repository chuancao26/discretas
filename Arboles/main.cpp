#include <iostream>
#include <fstream>
using namespace std;

int main()
{

    char valor;
    int contador = 0;
    ifstream entrada;
    entrada.open("E:/UNSA 2022 CC/semestre par/CC/discretas_2/Arboles/text.txt");
    entrada >> valor;
    while (valor != ){

        entrada >> valor;
        cout << valor;
        contador ++;
        //if (valor == 'x')
          //  break;
    }
}
