// #include <python3.8/Python.h>
// #include<string>
#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    // Py_Initialize();

    // PyObject *pModule = NULL;
    // PyObject *pFunc = NULL;
    // PyObject *pInstance = NULL;

    // pModule = PyImport_ImportModule("BooleanMinimize");
    // pFunc = PyObject_GetAttrString(pModule, "BooleanMinimize");
    // pInstance = PyEval_CallObject(pFunc, NULL);
    // PyObject_CallMethod(pInstance,"input.pla","test.pla");

    // Py_Finalize();

    // return 0;

    system("pip3 install pipenv");
    system("pipenv install");
    // system("pipenv shell");
    string command = "pipenv run python3 BooleanMinimize.py";
    command += " ";
    command += argv[1];
    command += " ";
    command += argv[2];
    cout << command << endl;
    system(command.c_str());

    return 0;
}