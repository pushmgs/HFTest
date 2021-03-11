#include "include/StackFrame.h"

// Constructors
Function::Function() {}

Function::Function(std::string& name, FunctionTypes::Params& parameters, FunctionTypes::Type& returnType) 
{
    _info = new FunctionInfo();
    _info->name = name;
    _info->parameters = parameters;
    _info->returnType = returnType;
}

Function::Function(FunctionInfo* stats) 
{
    this->SetFunctionInfo(stats);
}

// Destructor
Function::~Function() 
{
    ClearFunctionInfo();
}

// Methods

// Attaching and detatching FunctionInfo
void Function::ClearFunctionInfo(void) 
{ 
    delete _info; 
}

void Function::SetFunctionInfo(FunctionInfo* stats) 
{ 
    _info = stats; 
}

FunctionInfo* Function::GetFunctionInfo() const 
{ 
    return _info; 
}