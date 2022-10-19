#include <iostream>
using namespace std;
int main()
{
    double TV, DVD, RC, SS, CAB, TV_price, DVD_price, RC_price, SS_price, CAB_price, sub_total, tax, total;
    cout << "Welcome to my program!\n";
    cout << "\n" << "Number of TVs sold: ";
    cin >> TV;
    cout << "Number of DVD players sold: ";
    cin >> DVD;
    cout << "Number of Remote Controllers sold: ";
    cin >> RC;
    cout << "Number of Sound Speakers sold: ";
    cin >> SS;
    cout << "Number of Cables sold: ";
    cin >> CAB;
    TV_price = 24000.00 * TV;
    DVD_price = 14500.00 * DVD;
    RC_price = 3000.00 * RC;
    SS_price = 9700.00 * SS;
    CAB_price = 1000.00 * CAB;
    sub_total = TV_price + DVD_price + RC_price + SS_price + CAB_price;
    tax = (sub_total * 8.25)/100.00;
    total = sub_total + tax;
    cout << "\n";
    cout << "Qty    DESCRIPTION              UNIT PRICE      TOTAL PRICE\n";
    cout << TV<< "      TV                       24000.00        "<< TV_price << "\n";
    cout << DVD<<"      DVD Player               14500.00        "<< DVD_price << "\n";
    cout << RC<< "      Remote Controller        3000.00         "<< RC_price << "\n";
    cout << SS<< "      Sound Speakers           9700.00         "<< SS_price << "\n";
    cout << CAB<<"      Cables                   1000.00         "<< CAB_price << "\n";
    cout << "\n";
    cout << "SubTotal                                        "<< sub_total << "\n";
    cout << "Tax                                             "<< tax  << "\n";
    cout << "Total                                           "<< total << "\n";
    return 0;
}
