#include <iostream>
#include <vector>
#include <algorithm>

bool all_transported(std::vector<bool> arr)
{
    for (int i=0; i < arr.size(); i++)
        if (arr[i] == false)
            return false;
    return true;
}

int raft(int K, std::vector<int> weights)
{
    int min = weights[0];

    std::vector<bool> transported;
    for (int i = 0; i < weights.size(); i++)
        transported.push_back(false);

    while (true)
    {
        for (int t = 0; t < K; t++)
        {
            int sum = 0;
            for(int i = 0; i < weights.size(); i++)
            {
                if (sum + weights[i] <= min && transported[i] == false)
                {
                    sum += weights[i];
                    transported[i] = true;
                }
            }
        }
            
        if (all_transported(transported))
            return min;
        
        min += 1;
        for(int j = 0; j < transported.size(); j++)
            transported[j] = false;
    }
}

                    


int main()
{
    int N, K;
    std::cin >> N >> K;

    std::vector<int> weights;
    for(int i = 0; i < N; i++)
    {
        int num;
        std::cin >> num;
        weights.push_back(num);
    }
    std::sort(weights.begin(), weights.end(), std::greater<int>());
    
    std::cout << "\n" << raft(K, weights);
}