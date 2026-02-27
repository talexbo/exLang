#include<iostream>
#include<stack>

int main(){
    std::string paranteze;
    std::stack<char> stiva;
    std::cout <<"sir de paranteze = ";
    std::cin >> paranteze;
    int ok=1;
    for (int i = 0; i<paranteze.size(); i++) {
        if(paranteze[i] == '('){
            stiva.push('(');
        }
        else{
            if (paranteze[i] == ')'){
                if(!stiva.empty()){
                    stiva.pop();
                }
                else{
                    ok=0;
                    break;
                }
            }
        }
    } 
    if(ok && stiva.empty()){
        std::cout << "((((((((e bun șirul))))))))";
    }
    else{
        std::cout << "nu e bun șirul, codul tău în Lisp e stricat.";
    }
    return 0;
};