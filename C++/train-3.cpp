#include <iostream>
using namespace std;
// for loops

int main()
{
    for (int i = 1; i <= 5; ++i)
    {
        cout << i << " ";
    }
    cout << endl;
    for (int i = 1; i <= 5; ++i)
    {
        cout << "Hello World!" << endl;
    }
    cout << endl;
    // sum of first n nautral numbers
    /*
    int num, sum;
    sum = 0;

    cout << "Enter n : ";
    cin >> num;

    for (int i = 1; i <= num; ++i)
    {
        sum += i;
    }
    cout << "Sum  = " << sum << endl;
    */

   // range based loop
    int num_array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    for (int n : num_array)
    {
        cout << n << " ";
    }

    // infinite loops
    /*
    for(int i = 1; i > 0; i++) {
        // block of code
    }
    */

    return 0;
}