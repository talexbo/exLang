#include <iostream>

// Programare Dinamică (2 pct)
// Să se genereze primele n rânduri ale Triunghiului lui Pascal. 
// Într-un Triunghi Pascal, fiecare număr este suma celor două 
// numere aflate direct deasupra lui. Soluția trebuie să fie
//  de complexitate de timp O(n2).
// Exemplu pentru n = 4:
// 1
// 1 1
// 1 2 1
// 1 3 3 1
//==============================================================================

void scoatePascal(int n) {
    int** pascalT = new int*[n];
    for (int i = 0; i < n; i++) {
        pascalT[i] = new int[i];
    }

    for (int i = 0; i < n; i++) {
        pascalT[i][0] = 1;
        pascalT[i][i] = 1;
        for (int j = 1; j < i; j++) {
            pascalT[i][j] = pascalT[i-1][j-1] + pascalT[i-1][j];
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            std::cout << pascalT[i][j] << " ";
        }
        std::cout << std::endl;
    }

    for (int i = 0; i < 3; i++) {
        delete pascalT[i];
    }
    delete[] pascalT;
}

int main() {
    int n;
    std::cout << "Introduceți numărul de rânduri: ";
    std::cin >> n;
    if (n > 0 && n <35) {
        scoatePascal(n);
    } else {
        std::cout << "Numărul de rânduri trebuie să pozitiv sau mai mic decat 35."<< std::endl;
    }
    return 0;
}
