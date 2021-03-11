// HFManager is going to have a couple of jobs in the future, but at the moment
// We're just going to keep it in charge of the call stack.
// HFTest file written & modified - 02/23/2023

#ifndef HFTEST_STACK_MANAGER_H_
#define HFTEST_STACK_MANAGER_H

#include "StackFrame.h"
#include <stack>
#include <memory>

namespace StacksManager {
    void AddStackFrame(std::shared_ptr<StackFrame> stack);
    void ClearStackFrames();

    [[nodiscard]] std::shared_ptr<StackFrame> PopStackFrame();
    [[nodiscard]] int GetTotalStacks();
} // namespace HFManager

#endif // HFTEST_MANAGER_H_