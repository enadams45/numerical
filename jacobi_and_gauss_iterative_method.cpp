#include <bits/stdc++.h>
using namespace std;

void jacobi(int a1, int a2, int a3, int b1, int b2, int b3, int c1, int c2, int c3, int d1, int d2, int d3) {
    double x=9, x1 = 0, y=9, y1 = 0, z=9, z1 = 0;
    int count = 0, resIt;
    bool resFound = false;
    double resX, resY, resZ;
    vector <double> difX; vector<double>difY; vector<double> difZ;
    while(count < 20) {
        ++count;
        x = x1, y=y1, z=z1;
        x1 = (d1-b1*y-c1*z)/a1;
        y1 = (d2-a2*x-c2*z)/b2;
        z1 = (d3-a3*x-b3*y)/c3;

        double difx = abs(x-x1), dify = abs(y-y1), difz = abs(z-z1);
        difX.push_back(difx); difY.push_back(dify); difZ.push_back(difz);

        if(resFound==false && difx <= 0.001 && dify <= 0.0001 && difz <= 0.0001) {
            resX = x1; resY = y1; resZ = z1;
            resIt= count;
            resFound = true;
        }
    }
   
    cout << "difX: ";
    for(auto it : difX) {
        cout << it << " ";
    }
    cout << "\n\n";
    
    cout << "difY: ";
    for(auto it : difY) {
        cout << it << " ";
    }
    cout << "\n\n";
    
    cout << "difZ: ";
    for(auto it : difZ) {
        cout << it << " ";
    }
    cout << "\n\n";
    cout << "x: " << resX << "  y: " << resY << "   z: " << resZ << endl;
    cout << "Result found in " << resIt << " iterations" << endl;

}

void gauss(int a1, int a2, int a3, int b1, int b2, int b3, int c1, int c2, int c3, int d1, int d2, int d3) {
    double x=9, x1 = 0, y=9, y1 = 0, z=9, z1 = 0;
    bool resFound = false;
    int count = 0, resIt;
    double resX, resY, resZ;
    vector <double> difX; vector<double>difY; vector<double> difZ;
    while(count < 20) {
        ++count;
        x = x1, y=y1, z=z1;
        x1 = (d1-b1*y1-c1*z1)/a1;
        y1 = (d2-a2*x1-c2*z1)/b2;
        z1 = (d3-a3*x1-b3*y1)/c3;

        double difx = abs(x-x1), dify = abs(y-y1), difz = abs(z-z1);
        difX.push_back(difx); difY.push_back(dify); difZ.push_back(difz);

        if(resFound==false && difx <= 0.001 && dify <= 0.0001 && difz <= 0.0001) {
            resX = x1; resY = y1; resZ = z1;
            resIt = count;
            resFound = true;
        }
    }
   
    cout << "difX: ";
    for(auto it : difX) {
        cout << it << " ";
    }
    cout << "\n\n";
    
    cout << "difY: ";
    for(auto it : difY) {
        cout << it << " ";
    }
    cout << "\n\n";
    
    cout << "difZ: ";
    for(auto it : difZ) {
        cout << it << " ";
    }
    cout << "\n\n";
    cout << "x: " << resX << "  y: " << resY << "   z: " << resZ << endl;
    cout << "Result found in " << resIt << " iterations" << endl;

}


int main() {
    int a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3;
    cin >> a1 >> b1 >> c1 >> d1; 
    cin >> a2 >> b2 >> c2 >> d2;
    cin >> a3 >> b3 >> c3 >> d3;
    cout << endl;
    
    jacobi(a1,a2,a3,b1,b2,b3,c1,c2,c3,d1,d2,d3);
    cout <<"\n\n";
    gauss(a1,a2,a3,b1,b2,b3,c1,c2,c3,d1,d2,d3);

    return 0;
}