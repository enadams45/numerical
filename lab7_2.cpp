#include <bits/stdc++.h>
using namespace std;
void newton_forward() {
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

        vector<vector<double>> del(n-1,vector<double>(n-1,0));
        double h = x[1]-x[0];
        double s = (xvar-x[n-1])/h;

        for(int i=0; i<n; ++i) {
            for(int j=0; j<n; ++j) {

            }
        }

        cout << yn << endl;

}
int main() {
   newton_forward();

}
