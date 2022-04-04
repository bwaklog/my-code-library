#include <iostream>
// while loops

using namespace std;

int main()
{
    int i = 1;

    while (i <= 5)
    {
        cout << i << " ";
        ++i;
    }
    cout << endl;

    // sum of positive integers and if -ve then loop terminates
    /*

    int number;
    int sum = 0;

    cout << "Enter a number : ";
    cin >> number;

    while (true)
    {
        cout << "Enter a number : ";
        cin >> number;

        if (number < 0) {
            break;
        }

        sum += number;
    }
    cout << sum <<endl;
    */

    // do while - print 1 to 5
    int j = 1;

    do
    {
        cout << j << " ";
        ++j;
    } while (j <= 5);

    cout << endl;

    for (int i = 1; i <= 5; ++i)
    {
        if (i == 3)
        {
            continue;
        }
        cout << i << " ";
    }

    return 0;
}