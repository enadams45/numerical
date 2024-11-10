#include <bits/stdc++.h>
using namespace std;
void lagrance() {
    double xvar;
    int n;
    cin >> xvar >> n;
    vector<double > x(n,0);
    vector<double>y(n,0);
    for(int i=0; i<n; ++i) {
        cin >> x[i];
    }
     for(int i=0; i<n; ++i) {
        cin >> y[i];
    }
    double yn = 0.0;
    for(int i=0; i<n; ++i) {
            double temp1=1.0, temp2=1.0;
            for (int j = 0; j < n; ++j) {
            if (j != i) {
                temp1 *= (xvar - x[j]);
                temp2 *= (x[i] - x[j]);
            }
        }
            yn+=(temp1/temp2)*y[i];
    }
    cout << yn << endl;

}
int main() {
    lagrance();

}
