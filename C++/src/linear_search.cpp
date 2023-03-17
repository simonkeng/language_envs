#include<iostream>
using namespace std;

int linear_search(int arr[], int n, int key){
    // O(N)
    for (int i=0; i<n; i++){
        if(arr[i] == key){
            return i;
        }
    }
    return -1;
}

int main(){
    int a[] = {1,2,3,4,5,6,7,8,9};
    int n = 20;
    int k = 7;
    int index = linear_search(a, n, k);
    cout << "Index is " << index << endl;
    return 0;
}