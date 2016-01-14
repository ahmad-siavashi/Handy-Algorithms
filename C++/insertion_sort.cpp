// In his exalted name
// Algorithm: Insertion Sort
// Author: Ahmad Siavashi (ahmad.siavashi@gmail.com)
// Date: 11/2/2014

#include <iostream>
#include <vector>
#include <random>
#include <ctime>

using namespace std;

int insertionSort(vector<int>& A){
    for(int j = 1; j < A.size() ; j++){
        int key = A[j];
        int i = j - 1;
        while (i >= 0 && A[i] > key){
            A[i+1] = A[i];
            i--;
        }
        A[i+1] = key;
    }
}

int main()
{
    int n;
    cin >> n;
    default_random_engine generator;
    uniform_int_distribution<int> distribution(1,n);
    vector<int> A;
    for(int i = 0 ; i < n ; i++){
        A.push_back(distribution(generator));
    }
    float t = clock();
    insertionSort(A);
    cout << "Elapsed time = " << (clock()-t)/CLOCKS_PER_SEC << endl;
    /*
    for(int val : A){
        cout << val << endl;
    }
    /**/
    return 0;
}
