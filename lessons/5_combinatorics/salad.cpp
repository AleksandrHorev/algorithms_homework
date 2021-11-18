// https://acmp.ru/index.asp?main=task&id_task=513
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>

using namespace std;

map<int, unsigned long long> factorials;

unsigned long long fact(int number) {
  if (factorials[number]) return factorials[number]; 

  unsigned long long result = fact(number - 1) * number;
  factorials.insert(number, result);
  return factorials[number];
}

int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int  n;
    fin >> n;
//////////////////
    unsigned long long result = 0;
    factorials.insert(0, 1);
    for (int k = 1; k <= n; k++) {
      result += fact(n) / (fact(k) * fact(n-k));
    }

////////////////////
    fout << result;

    fin.close();
    fout.close();

     return 0;
}
