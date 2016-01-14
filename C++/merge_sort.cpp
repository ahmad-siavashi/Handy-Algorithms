// In his exalted name
// Algorithm: Merge Sort
// Author: Ahmad Siavashi (ahmad.siavashi@gmail.com)
// Date: 11/2/2014

#include <vector>
#include <iostream>
#include <cmath>
#include <random>
#include <ctime>

using namespace std;

int n;

void merge(vector<int>&, int,int,int);

void print(vector<int>& A){
	for(int i = 0 ; i < A.size() ; i++)
		cout << A[i] << ", ";
	cout << endl;
}

void mergeSort(vector<int>& A, int p, int r){
	if(p < r){
		int q = (r+p)/2;
		mergeSort(A,p,q);
		mergeSort(A,q+1,r);
		merge(A,p,q,r);
	}
}

void merge(vector<int>& A, int p, int q, int r){
		int n1 = q - p + 1;
		int n2 = r - q;
		vector<int> L,R;
		for(int i = 0 ; i < n1 ; i++){
			L.push_back(A[p + i]);
		}
		for(int j = 0 ; j < n2 ; j++){
			R.push_back(A[q+j+1]);
		}
		L.push_back(n+1); // to represent infinity.
		R.push_back(n+1);
//		print(A);
//		print(L);
//		print(R);
        int i = 0, j = 0;
        for(int k = p ; k <= r ; k++){
            if(L[i] <= R[j]){
				A[k] = L[i];
				i += 1;
            }else{
				A[k] = R[j];
				j += 1;
            }
        }
//		print(A);
}

int main()
{
    cin >> n;
    default_random_engine generator;
    uniform_int_distribution<int> distribution(1,n);
    vector<int> A;
    for(int i = 0 ; i < n ; i++){
        A.push_back(distribution(generator));
    }
//    print(A);
    float t = clock();
    mergeSort(A,0,A.size() - 1);
    cout << "Elapsed time = " << (clock()-t)/CLOCKS_PER_SEC << endl;
//    print(A);
    return 0;
}
