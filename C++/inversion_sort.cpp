// In his exalted name
// Algorithm: Inversion Sort
// Author: Ahmad Siavashi (ahmad.siavashi@gmail.com)
// Date: 13/5/2014

#include <vector>
#include <iostream>
#include <cmath>
#include <random>
#include <ctime>

using namespace std;

int n;

int merge(vector<int>&, int,int,int);

void print(vector<int>& A){
	for(int i = 0 ; i < A.size() ; i++)
		cout << A[i] << ", ";
	cout << endl;
}

int mergeSort(vector<int>& A, int p, int r){
	if(p < r){
		int q = (r+p)/2;
		int x = mergeSort(A,p,q);
		int y = mergeSort(A,q+1,r);
		int z = merge(A,p,q,r);
		return x + y + z;
	}else{
		return 0;
	}
}

int merge(vector<int>& A, int p, int q, int r){
		int n1 = q - p + 1;
		int n2 = r - q;
		int c = 0;
		vector<int> L,R;
		for(int i = 0 ; i < n1 ; i++){
			L.push_back(A[p + i]);
		}
		for(int j = 0 ; j < n2 ; j++){
			R.push_back(A[q+j+1]);
		}
		//L.push_back(n+1); // to represent infinity.
		//R.push_back(n+1);
//		print(A);
//		print(L);
//		print(R);
        int i = 0, j = 0;
        for(int k = p ; k <= r ; k++){
            if(i < n1 && L[i] < R[j]){
				A[k] = L[i];
				i += 1;
            }else{
				A[k] = R[j];
				j += 1;
				c += n1 - i;
            }
        }
        return c;
//		print(A);
}
int main()
{
    //cin >> n;
    default_random_engine generator;
    uniform_int_distribution<int> distribution(1,n);
    vector<int> A;
    /*
    for(int i = 0 ; i < n ; i++){
        A.push_back(distribution(generator));
    }
    */
    A.push_back(1);
    A.push_back(3);
    A.push_back(5);
    A.push_back(2);
    A.push_back(4);
    A.push_back(6);
    print(A);
    float t = clock();
    cout << mergeSort(A,0,A.size() - 1) << endl;
    cout << "Elapsed time = " << (clock()-t)/CLOCKS_PER_SEC << endl;
    print(A);
    return 0;
}
