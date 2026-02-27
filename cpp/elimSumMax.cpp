// 3. Metoda Greedy (2 pct)
// Se dau trei vectori v1, v2 și v3, fiecare conținând numere întregi pozitive, 
// din care se pot elimina elemente doar de la începutul fiecărui vector 
// (primul element curent).
// Să se găsească suma maximă posibilă care poate fi obținută astfel încât suma
// elementelor rămase în fiecare dintre cei trei vectori să fie egală.
// Exemplu:
// v1: {3, 2, 1, 1, 1} (Suma totală: 8)
// v2: {4, 3, 2} (Suma totală: 9)
// v3: {1, 1, 4, 1} (Suma totală: 7)

// Output: Suma maximă egală este 5.
// (Explicație: Din v1 eliminăm 3; din v2 eliminăm 4; din v3 eliminăm 1 și 1.
// Toți vectorii rămân cu suma 5.)

#include<iostream>
#include<vector>

void eliminaFata(std::vector<int>& v) {
    if (v.empty()) 
        return;
    std::vector<int> aux;
    for (int i = 1; i < v.size(); i++) {
        aux.push_back(v[i]);
    }
    v = aux;
}

int sumaVector(std::vector<int> v){
    int suma = 0;
    for (int i = 0; i<v.size(); i++) {
        suma += v[i]; 
    }
    return suma;
}

void scriereVector(std::vector<int>& v){
    int n;
    std::cout << "lungime vector: ";
    std::cin >> n;
    std::cout << "scrie vector: ";
    for (int i = 0; i < n; i++) {
        int el;
        std::cin >> el;
        v.push_back(el);
    }
}

void afisareVector(std::vector<int>& v){
    for (int i = 0; i < v.size(); i++) {
        std::cout << v[i] << " ";
    }
}

int lungimeMaximaDinTrei(std::vector<int>& v1, std::vector<int>& v2, std::vector<int>& v3){
    if(v1.size() > v2.size() && v1.size() > v3.size())
        return v1.size();
    else if (v2.size() > v1.size() && v2.size() > v3.size())
        return v2.size();
    else if (v3.size() > v1.size() && v3.size() > v2.size())
        return v3.size();
    else
        return v1.size(); //sunt egali in lungime
}

int gasesteCmmElComIntreRanduri(int**& mat, int& n) {
    int CmmC = -1; 
    for (int i = 0; i<n; i++) {
        int suma = mat[0][i];
        bool gasitRandDoi = false;
        bool gasitRandTrei = false;
        for (int j = 0; j<n; j++) {
            if (mat[1][j] == suma) {
                gasitRandDoi = true;
                break; 
            }
        }
        for (int k = 0; k <n; k++) {
            if (mat[2][k] == suma) {
                gasitRandTrei = true;
                break;
            }
        }
        if (gasitRandDoi && gasitRandTrei) {
            if (suma > CmmC) { 
                CmmC = suma;
            }
        }
    }
    return CmmC;
}

int main(){
    std::vector<int> v1;
    std::vector<int> v2;
    std::vector<int> v3;
    scriereVector(v1);
    scriereVector(v2);
    scriereVector(v3);
    int n = lungimeMaximaDinTrei(v1, v2, v3); 
    int** mat = new int*[3];
    for (int i = 0; i < 3; i++) {
        mat[i] = new int[n];
        for (int j = 0; j < n; j++) {
            mat[i][j] = 0;
        }
    }
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < n; j++) {
            if (i==0 && j<v1.size()) {
                mat[i][j] = v1[j];
            }
            if (i==1 && j<v2.size()) {
                mat[i][j] = v2[j];
            }        
            if (i==2 && j<v3.size()) {
                mat[i][j] = v3[j];
            }        
        }
    }

    for (int i = 0; i < 3; i++) {
        int suma = 0;
        for (int j = n-1; j >= 0; j--) {
            suma=suma+mat[i][j]; 
            mat[i][j] = suma;
        }
    }

    int sumaGreedy = gasesteCmmElComIntreRanduri(mat, n);

    if (sumaGreedy > 0) {
        std::cout << "Cea mai mare suma este: " << sumaGreedy << std::endl;
        std::cout << "Uita-te în matrice de cate ori ar trebui" << std::endl;
        std::cout << "sa ruleze funcția cu care elimin primul" << std::endl;
        std::cout << "element al fiecărui vector." << std::endl;
    }
    else {
        std::cout << "Nu există val sumă comună" << std::endl;
    }
    for (int i = 0; i < 3; i++) {
        for(int j = 0; j < n; j++){
            std::cout << mat[i][j] << " ";
        }
        std::cout << std::endl;
    }

    for (int i = 0; i < 3; i++) {
        delete[] mat[i];
    }
    delete[] mat;

    return 0;
}
