#include <iostream>
#include <vector>


bool goodRectangle(int N, int M, int R, int C, int I, int J, const std::vector<std::vector<char>>& room)
{
    for(int i = I; i < I + R; ++i)
    {
        if(i >= N) return false;

        for(int j = J; j < J + C; ++j)
        {
            if(j >= M || room[i][j] == '#') return false;
        }
    }

    return true;
}

int cinema(int N, int M, int R, int C, const std::vector<std::vector<char>>& room)
{
    int counter = 0;

    for(int i = 0; i < N; ++i)
    {
        for(int j = 0; j < M; ++j)
        {
            if (goodRectangle(N, M, R, C, i, j, room))
            {
                counter++;
            }
        }
    }

    return counter;
}




int main()
{
    int N, M, R, C;
    std::cin >> N >> M;
    std::cin >> R >> C;
    
    std::vector<std::vector<char>> room;
    room.resize(N);
    for(int i = 0; i < N; ++i)
    {
        room[i].resize(M);
    }

    for(int i = 0; i < N; ++i)
    {
        for(int j = 0; j < M; ++j)
        {
            std::cin >> room[i][j];
        }
    }


    std::cout << cinema(N, M, R, C, room);


    return 0;
}