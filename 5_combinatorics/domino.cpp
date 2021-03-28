#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int mod(int num) {
    if (num < 0) return -num;
    return num;
} 

int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int n;
    fin >> n;
//////////////////
    vector<int> h(n);

    // for (int i = 0; i < n; i++) {
    //     fin >> h[i];
    // }

    int result = 0;

    for (int i = 0; i <= n; i++) {
      for (int j = i; j <= n; j++) {
          result += (i + j);
      }
    }
////////////////////
    // fout << min_energy[n - 1];
    fout << result;

    fin.close();
    fout.close();

    return 0;
}
