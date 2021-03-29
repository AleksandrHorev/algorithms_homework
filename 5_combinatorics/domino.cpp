// https://acmp.ru/index.asp?main=task&id_task=328
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    long long  n;
    fin >> n;
//////////////////
    long long result = 0;

    // for (int i = 0; i <= n; i++) {
    //   for (int j = i; j <= n; j++) {
    //       result += (i + j);
    //   }
    // }
    result = n * (((n + 1) + 1)*(n + 1)/2);

////////////////////
    fout << result;

    fin.close();
    fout.close();

     return 0;
}
