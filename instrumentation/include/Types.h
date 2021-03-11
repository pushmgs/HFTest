//
//

#include <map>
#include <string>

#include "FunctionInfo.h"

namespace FunctionTypes
{
    // Map of parameter name -> type name
    typedef std::map<std::string, std::string> Params;
    
    // Used when dealing with things such as return types, function parameters, etc...
    typedef void* Type;
}

namespace FunctionUtil
{
    // ...
}