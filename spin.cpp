/*
ID: iamwoji1
LANG: C++
TASK: spin
*/
#include <iostream>
#include <fstream>

using namespace std;

//#define debug

ifstream fin("spin.in");
ofstream fout("spin.out");

int main()
{
    int speed[5];
    int numOfWedge[5];
    int wedgeRec[5][5][2];
    bool shineRec[5][361];
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 360; j++)
        {
            shineRec[i][j] = false;
        }
    }
    for (int i = 0; i < 5; i++)
    {
        #ifdef debug
        cin >> speed[i];
        cin >> numOfWedge[i];
        #else
        fin >> speed[i];
        fin >> numOfWedge[i];
        #endif

        for (int j = 0; j < numOfWedge[i]; j++)
        {
            int start, end;

            #ifdef debug
            cin >> start >> end;
            #else
            fin>>start>>end;
            #endif

            wedgeRec[i][j][0] = start;
            wedgeRec[i][j][1] = end;
        }
    }
    int curTime = 0;
    while (curTime < 360)
    {
        for (int i = 0; i < 5; i++)
        {
            int curSpeed = speed[i]; // speed of this plate
            int curAngle=(curTime*curSpeed)%360;
            for (int j = 0; j < numOfWedge[i]; j++)
            {
                int start = (wedgeRec[i][j][0] + curAngle) % 360;
                int end = (start+wedgeRec[i][j][1])%360;
                //cout<<i<<" "<<j<<" "<<start<<" "<<end<<" "<<curAngle<<" "<<curTime<<endl;
                if (start > end)
                {
                    for (int k = start; k <= 360; k++)
                    {
                        shineRec[i][k] = true;
                    }
                    for (int k = 0; k <= end; k++)
                    {
                        shineRec[i][k] = true;
                    }
                }
                else
                {
                    for (int k = start; k <= end; k++)
                    {
                        shineRec[i][k] = true;
                    }
                }
            }
        }
        for (int ang = 0; ang < 360; ang++)
        {
            //cout<<curTime<<endl;
            //cout<<ang<<" "<<shineRec[0][ang]<<shineRec[1][ang]<<shineRec[2][ang]<<shineRec[3][ang]<<shineRec[4][ang]<<endl;
            if (shineRec[0][ang] == true && shineRec[1][ang] == true && shineRec[2][ang] == true && shineRec[3][ang] == true && shineRec[4][ang] == true)
            {
                #ifdef debug
                cout << curTime << endl;
                #else
                fout<<curTime<<endl;
                #endif

                return 0;
            }
        }
        curTime++;
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 360; j++)
            {
                shineRec[i][j] = false;
            }
        }
    }
    #ifdef debug
    cout<<"none"<<endl;
    #else
    fout<<"none"<<endl;
    #endif
}