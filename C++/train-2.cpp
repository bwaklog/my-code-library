#include <iostream>
// if and else statements
using namespace std;

int main()
{
    int num = 0;
    cout << "Enter an integer : ";
    cin >> num;

    // check if it is positive
    if (num != 0) {
        if (num > 0) {
            cout << "Positive" << endl;
        }
        else {
            cout << "Negative" << endl;
        }
    }
    else {
        cout << "The number is 0" << endl;
    }

    return 0;
}
