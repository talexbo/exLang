#include <iostream>
#include <fstream>
#include <string>

struct nodInCoada {
    int x, y;
};

struct coadaCirculara {
    nodInCoada* coada;
    int fata;
    int spate;
    int marime;
    
    coadaCirculara(int m) {
        marime = m;
        coada = new nodInCoada[marime];
        fata = -1;
        spate = -1;
    }
    
    void adauga(int x, int y) {
        if (fata == -1) {
            fata = 0;
        }
        spate = (spate + 1) % marime;
        coada[spate].x = x;
        coada[spate].y = y;
    }
    
    nodInCoada scoate() {
        nodInCoada value = coada[fata];
        if (fata == spate) {
            fata = -1;
            spate = -1;
        } else {
            fata = (fata + 1) % marime;
        }
        return value;
    }
    
    bool eGol() {
        return fata == -1;
    }
};

void citesteLabirint(std::string numeLabirint,
                            int**& labirint, int& n, int& m) {
    std::ifstream fisier(numeLabirint);
    fisier >> n >> m;
    labirint = new int*[n];
    for (int i = 0; i < n; i++) {
        labirint[i] = new int[m];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            fisier >> labirint[i][j];
        }
    }
}

bool** creazaIstoric(int n, int m) {
    bool** aFost = new bool*[n];
    for (int i = 0; i < n; i++) {
        aFost[i] = new bool[m];
        for (int j = 0; j < m; j++) {
            aFost[i][j] = false;
        }
    }
    return aFost;
}
//scrie o matrice cu FALSE pentru a tine minte unde
//a mai fost soarecele

void stergeIstoric(bool** istoric, int n) {
    for (int i = 0; i < n; i++) {
        delete[] istoric[i];
    }
    delete[] istoric;
}
//dealoca memorie matrice bool

void stergeMatriceInt(int** matrice, int n) {
    for (int i = 0; i < n; i++) {
        delete[] matrice[i];
    }
    delete[] matrice;
}
//dealoca memorie matrice int

void laBFSirint(int** labirint, int xPlecare, int yPlecare, 
                                int xBranza, int yBranza,
                                int n, int m) {
    coadaCirculara q(n * m);
    bool** trecut = creazaIstoric(n, m);
    
    int** xAnterior = new int*[n];
    int** yAnterior = new int*[n];
    for (int i = 0; i < n; i++) {
        xAnterior[i] = new int[m];
        yAnterior[i] = new int[m];
        for (int j = 0; j < m; j++) {
            xAnterior[i][j] = -1;
            yAnterior[i][j] = -1;
        }
    }

    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};
    //direcții de mișcare sus, jos, stânga, dreapta în 2 vectori.

    //Algoritm de cautare in latime.
    q.adauga(xPlecare, yPlecare);
    trecut[xPlecare][yPlecare] = true;

    while (!q.eGol()) {
        nodInCoada curent = q.scoate();
        int x = curent.x;
        int y = curent.y;

        if (x == xBranza && y == yBranza) {
            std::cout << "Soarecu a pus gheara pe branza!\n";
            std::cout << "Inainte sa ajunga la branza el a fost prin: ";
            int xCurent = xBranza, yCurent = yBranza;
            while (xCurent != -1 && yCurent != -1) {
                std::cout << "(" << xCurent << "," << yCurent << ") ";
                int xParinte = xAnterior[xCurent][yCurent];
                int yParinte = yAnterior[xCurent][yCurent];
                xCurent = xParinte;
                yCurent = yParinte;
            }
            std::cout << "\n";
            return;
        } //Soarecu se opreste cand da de branza

        //Daca nu a gasit branza cauta in pozitiile vecine
        for (int i = 0; i < 4; i++) {
            int xVecin = x + dx[i];
            int yVecin = y + dy[i];
            
            if (xVecin >= 0 && xVecin < n && yVecin >= 0 && yVecin < m &&
                !trecut[xVecin][yVecin] && labirint[xVecin][yVecin] != -1) {
                
                q.adauga(xVecin, yVecin);
                trecut[xVecin][yVecin] = true;
                xAnterior[xVecin][yVecin] = x;
                yAnterior[xVecin][yVecin] = y;
            }
        }
    }
    
    std::cout << "Branza este o minciuna! Soarecele este inchis :( \n";

    //Goleste memorie!
    stergeIstoric(trecut, n);
    for (int i = 0; i < n; i++) {
        delete[] xAnterior[i];
        delete[] yAnterior[i];
    }
    delete[] xAnterior;
    delete[] yAnterior;
    delete[] q.coada;
}

int main() {
    int** labirint;
    int n, m;
    std::string harta;
    std::cout << "Selectați labirintul (scrie numele fisierului): ";
    getline(std::cin, harta);
    citesteLabirint(harta, labirint, n, m);
    laBFSirint(labirint, 0, 0, n-1, m-1, n, m);
    //am ales conltul diametral opus punctului de plecare,
    //dar ambele pot fi arbitrare
    stergeMatriceInt(labirint, n);
    return 0;
}
