// 정확성 100
// 효율성 0 - 시간초과 

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    
    while (!prices.empty()){
        int cur = prices.front();
        prices.erase(prices.begin());
        int cnt = 0;
        for(auto i : prices) {
            cnt += 1;
            if (cur > i)
            	break;
        };
        answer.push_back(cnt);
    }
    
    return answer;
}