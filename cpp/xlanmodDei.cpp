// 2. Divide et Impera (2 pct)
// Se dau trei numere întregi x, n și M. 
// Să se calculeze eficient valoarea expresiei x^n % M folosind 
// metoda Divide et Impera. Algoritmul trebuie să aibă o complexitate 
// de O(log n). Atenție la gestionarea overflow-ului în timpul înmulțirilor.
// Exemplu:
// • Input: x = 2, n = 10, M = 1000
// • Output: 1024 (mod 1000) = 24
// • Input: x = 4, n = 13, M = 497
// • Output: 67108864 (mod 497) = 445

#include<iostream>

int putereMoo(int b, int e, int M){
    int rezultat = 1;
    b = b-(b/M)*M; //b = b%M
    while (e > 0 && M!=0){ 
        if (e % 2 == 1){ 
            int aux1 = rezultat*b; 
            rezultat = aux1-(aux1/M)*M;
        }
        e = e/2; 
        int aux2 = b*b;
        b = aux2-(aux2/M)*M; 
    }
    return rezultat;
}

int putere(int b, int e){
    if (e == 0) {
        return 1;
    }
    else if (e == 1) {
        return b;
    }
    else if (e % 2 == 0) {
        return putere(b, e/2) * putere(b, e/2);
    }
    else return putere(b,e/2+1) * putere(b,e/2);
    // complexitate O(n) pentru ca apeleaza functia de doua ori per nivel, si functia 
    // imparte e in 2 dar fiind apelata de doua ori e de fapt 2 la puterea log in baza
    // 2 din n, deci O(n).
}  

int putereMod(int x, int n, int M){
    return putere(x,n) % M; // O(1)
}


int main(){
    int x,n,M;
    std::cin >> x;
    std::cin >> n;
    std::cin >> M;
    int rezultat;
    rezultat = putereMod(x, n, M);
    std::cout << rezultat << std::endl;
    rezultat = putereMoo(x,n,M);
    std::cout << rezultat << std::endl;
    return 0;
}
