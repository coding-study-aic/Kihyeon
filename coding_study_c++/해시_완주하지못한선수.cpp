#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";

    // 알파벳 순으로 정렬
    sort(completion.begin(), completion.end());
    sort(participant.begin(), participant.end());
    
    for(int i = 0; i<participant.size(); i++){
        // 비교
        if (completion[i] != participant[i]){
            return participant[i];
        }
        
    }
    
    if (answer == "")
        return participant[participant.size()-1];
    
    return answer;
}