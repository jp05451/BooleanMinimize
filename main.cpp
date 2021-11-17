// #include <python3.8/Python.h>
// #include<string>
#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    //system("pip3 install pipenv");
    system("pipenv install");
    // system("pipenv shell");
    string command = "pipenv run python3 BooleanMinimize.py";
    command += " ";
    command += argv[1];
    command += " ";
    command += argv[2];
    cout << command << endl;
    system(command.c_str());

    system("pipenv --rm");

    return 0;
}