#include <iostream>
using namespace std;

// Function
void printArray(int * arr) {
    // "*" means arr is a reference, not the actual array
    cout <<"In Function"<<sizeof(arr) <<endl;
}


int main() {
    // Static memory allocation:
    int a[100];  // array of size 100
    // integers are 4 bytes
    // 4 bytes * 100 blocks = 400 bytes allocated in "linear" memory

    int arr[] = {1,2,3,4,5,6,7};
    // Calling function
    printArray(arr);

    // Length of my array?
    int n = sizeof(arr) / sizeof(int);
    // 4 bytes * 7 = 28
    // 28 bytes / 4 bytes = 7 values in array

    // Means "program executed successfully"
    return 0;

}
