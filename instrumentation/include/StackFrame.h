// Keeps a miniature, more lightweight callstack that is populated
// and emptied between the detection of a particular function signature
// HFTest file written & modified - 02/23/2023

#ifndef HFTEST_STACK_H_
#define HFTEST_STACK_H_

#include <string>
#include <unordered_map>
#include <utility>

#include "FunctionInfo.h"

// Lookup tables could be a recurring structure
typedef std::pair<FunctionInfo*, int> LookupResult;
typedef std::unordered_map<std::string, LookupResult> LookupTable;

class StackFrame {
public:
    StackFrame(std::string triggerName) : _triggerName(triggerName) {}
    StackFrame() {}

    bool AddFunctionInfo(FunctionInfo* func);
    [[nodiscard]] FunctionInfo* GetFunctionInfo(std::string name) const;

    int size() const;
private:
    std::string _triggerName;
    LookupTable _lookupTable;
    bool _locked;
};

#endif // HFTEST_CALLSTACK_DATA_H_