// Structure and tools for function information
// Written and modified 03/10/2023

#ifndef HFTEST_FUNCTION_INFO_DATA_H_
#define HFTEST_FUNCTION_INFO_DATA_H_

#include <string>
#include <map>

#include "Types.h"

struct FunctionInfo {
    // Function name as seen in codebase
    std::string name;

    // Data type & associated parameter name
    FunctionTypes::Params parameters;
    
    // Return type of the function
    FunctionTypes::Type returnType;
};

class Function {
public:
    Function() {}
    ~Function();
    // Assign FunctionInfo in constructor
    Function(std::string& name, FunctionTypes::Params& params, FunctionTypes::Type& type);
    Function(FunctionInfo* info);

    // Attach external function information
    void ClearFunctionInfo(void);
    void SetFunctionInfo(FunctionInfo* info);
    FunctionInfo* GetFunctionInfo() const;
private:
    FunctionInfo* _info;
};

#endif