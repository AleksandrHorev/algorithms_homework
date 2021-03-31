// https://acmp.ru/index.asp?main=task&id_task=291
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int n;
    fin >> n;

    vector<string> words(n);
    for (int i = 0; i < n; i++) {
        fin >> words[i];
    }

    string dictonary;
    fin >> dictonary;

//////////////////
    int result = 0;
    std::map<char, int> hashDictionary;
    for (int i = 0; i <= dictonary.length(); i++) {
      if (hashDictionary.find(dictonary[i]) != hashDictionary.end()) {
        hashDictionary[dictonary[i]] += 1;
      } else {
        hashDictionary[dictonary[i]] = 1;
      }
    }

    for (int i = 0; i < n; i++) {
      int len = words[i].length();
      bool isMissedLetter = false;
      std::map<char, int> tempHashDictionary;
      tempHashDictionary.insert(hashDictionary.begin(), hashDictionary.end());
      std::map<char, int>::iterator end = tempHashDictionary.end();

      for (int j = 0; j < len; j++) {
        char symbol = words[i][j];
        if ((tempHashDictionary.find(symbol) != end) && (tempHashDictionary[symbol] > 0)) {
          tempHashDictionary[symbol] -= 1;
        }
        else {
          isMissedLetter = true;
          break;
        }
      }

      if (!isMissedLetter) {
        result++;
      }
    }

////////////////////
    fout << result;

    fin.close();
    fout.close();

     return 0;
}
