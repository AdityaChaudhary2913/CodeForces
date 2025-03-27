#include <iostream>
#include <vector>
#include <unordered_map>
#include <numeric>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    
    while(t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        
        // Create a mapping from value to its last (rightmost) 1-indexed position.
        unordered_map<int, int> dct;
        for (int i = n - 1; i >= 0; i--) {
            if (dct.find(a[i]) == dct.end()) {
                dct[a[i]] = i + 1;
            }
        }
        
        int ans = -1;
        // Iterate over all pairs and update ans if gcd(x, y) == 1.
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (gcd(a[i], a[j]) == 1) {
                    ans = max(ans, dct[a[i]] + dct[a[j]]);
                }
            }
        }
        
        cout << ans << "\n";
    }
    
    return 0;
}
