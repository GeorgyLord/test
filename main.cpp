#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;
struct R {
    int a = 0;
    int p = 0;
    int t = 0;
};
void b(int s, const unordered_map<int, vector<int>>& g, vector<bool>& v, int& sz) {
    queue<int> q;
    q.push(s);
    v[s] = true;
    sz = 1;
    while (!q.empty()) {
        int n = q.front();
        q.pop();
        for (int nbr : g.at(n)) {
            if (!v[nbr]) {
                v[nbr] = true;
                sz++;
                q.push(nbr);
            }
        }
    }
}
void s(int n, int m, const vector<pair<int, int>>& e) {
    unordered_map<int, vector<int>> g;
    for (const auto& edge : e) {
        g[edge.first].push_back(edge.second);
        g[edge.second].push_back(edge.first);
    }
    vector<bool> v(n + 1, false);
    R r;
    for (int st = 1; st <= n; st++) {
        if (!v[st]) {
            int sz;
            b(st, g, v, sz);
            int mod = sz % 3;

            if (mod == 0) {
                r.t += sz / 3 * 3;
            }
            else if (mod == 1) {
                if (sz >= 4) {
                    int t = (sz - 4) / 3;
                    int p = 4 / 2;
                    r.t += t * 3;
                    r.p += p * 2;
                }
                else {
                    r.a += 1;
                }
            }
            else if (mod == 2) {
                int t = (sz - 2) / 3;
                r.t += t * 3;
                r.p += 2;
            }
        }
    }
    cout << r.a << endl;
    cout << r.p / 2 << endl;
    cout << r.t / 3 << endl;
}
int main() {
    int n, m;
    cin >> n >> m;
    vector<pair<int, int>> e(m);

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        e[i] = make_pair(a, b);
    }
    s(n, m, e);
}