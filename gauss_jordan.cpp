#include <iostream>
#include <vector>
#include <cmath> // for abs()
#include <iomanip> // for setting precision

using namespace std;

vector<double> gaussJordan(vector<vector<double>>& a, vector<double>& b) {
    int n = b.size();

    // Gauss-Jordan elimination process
    for (int k = 0; k < n; k++) {
        // Partial pivoting: Find the row with the largest absolute value in column k
        int maxIndex = k;
        for (int i = k + 1; i < n; i++) {
            if (abs(a[i][k]) > abs(a[maxIndex][k])) {
                maxIndex = i;
            }
        }

        // Swap rows if needed
        if (maxIndex != k) {
            swap(a[k], a[maxIndex]);
            swap(b[k], b[maxIndex]);
        }

        // Make the pivot element 1
        double pivot = a[k][k];
        if (pivot != 0) {
            for (int j = 0; j < n; j++) {
                a[k][j] /= pivot;
            }
            b[k] /= pivot;
        } else {
            cout << "Matrix is singular or nearly singular!" << endl;
            return vector<double>();
        }

        // Make all other elements in the current column 0
        for (int i = 0; i < n; i++) {
            if (i != k) {
                double factor = a[i][k];
                for (int j = 0; j < n; j++) {
                    a[i][j] -= factor * a[k][j];
                }
                b[i] -= factor * b[k];
            }
        }
    }

    return b;
}

int main() {
    vector<vector<double>> a = {{2, 1, -1}, {-3, -1, 2}, {-2, 1, 2}};
    vector<double> b = {8, -11, -3};

    vector<double> result = gaussJordan(a, b);

    if (!result.empty()) {
        cout << "Solution: ";
        for (double x : result) {
            cout << fixed << setprecision(4) << x << " ";
        }
        cout << endl;
    }

    return 0;
}
