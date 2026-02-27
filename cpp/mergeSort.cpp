// 1. Alocare Dinamică și Sortare (2 pct)
// Să se citească de la tastatură un număr natural n și un vector de n elemente întregi,
// alocat dinamic. Să se implementeze un algoritm de sortare eficient (QuickSort sau
// MergeSort) pentru a ordona crescător elementele vectorului. La final, se va afișa
// vectorul sortat și se va elibera memoria. Memoria se va aloca și dealoca manual,
// fără a se utiliza STL.

#include<iostream>

int* faceVector(int& n){
    std::cin >> n;
    int* vec = new int[n];
    for (int i = 0; i < n; i++){
        std::cin >> vec[i];
    }
    return vec;
}

void afisareVector(int* vec, int n){
    for (int i = 0; i < n; i++) {
        std::cout << vec[i] << " "; 
    }
    std::cout<<std::endl;
}

void interclasare (int* vec, int st, int dr){
    int i = st;
    int mij = (st + dr)/2;
    int j = mij + 1;
    int k = 0;
    int n = dr-st+1;
    int* aux = new int[n];
    while (i <= mij && j <= dr){
        if (vec[i] < vec[j]) {
            aux[k]=vec[i];
            k++;
            i++;
        }
        else {
            aux[k]=vec[j];
            k++;
            j++;
        }
    }
    for (; i <= mij; i++) {
        aux[k]=vec[i];
        k++;
    }
    for (; j<=dr; j++) {
        aux[k]=vec[j];
        k++;
    }
    for (int f = 0; f < n; f++) {
        vec[st+f]=aux[f];
    }
    delete[] aux;
}

void mergeSort(int* vec, int st, int dr){
    if(st >= dr){
        return;
    }
    else{
        int mij = (st+dr)/2;
        mergeSort(vec,st, mij);
        mergeSort(vec,mij+1, dr);
        interclasare(vec, st,dr);
    }
}

int main(){

    int n;
    int* vector;
    vector = faceVector(n);
    afisareVector(vector, n);
    mergeSort(vector, 0, n-1);
    afisareVector(vector, n);
    delete[] vector;
    return 0;
}