#include "include/StackFrame.h"

bool StackFrame::AddFunctionInfo(FunctionInfo* info) 
{
    LookupTable::iterator it = _lookupTable.find(info->name);
    if (it != _lookupTable.end()) 
    {
        // Increase times seen
        _lookupTable[info->name].second++;
        return true;
    }

    if (_locked) return false;
    if (info->name == _triggerName) 
    {
        _locked = true;
        return false;
    }

    LookupResult entry = std::make_pair(info, 0);
    _lookupTable.insert(std::make_pair(info->name, entry));
}

FunctionInfo* StackFrame::GetFunctionInfo(std::string name) const
{
    LookupTable::const_iterator it = _lookupTable.find(name);
    if (it != _lookupTable.end()) {
        return it->second.first;
    }
    else
        return nullptr;
}

int StackFrame::size() const
{
    return _lookupTable.size();
}