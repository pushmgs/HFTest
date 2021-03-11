//

#include "include/StacksManager.h"

namespace StacksManager {
    // Adds a stack frame to the manager
    void AddStackFrame(std::shared_ptr<StackFrame> stack) 
    { 
        _stackframes.push(stack); 
    }

    // Returns the item on the top and pops the stack
    [[nodiscard]] std::shared_ptr<StackFrame> PopStackFrame() 
    { 
        std::shared_ptr<StackFrame> frame = _stackframes.top();
        _stackframes.pop();

        return frame;
    }

    // Gets quantity of stacks held by the stacks manager
    [[nodiscard]] int GetTotalStacks()
    { 
        return _stackframes.size(); 
    }

    // Deallocate all of our frames
    void ClearStackFrames() {
        while (!_stackframes.empty()) {
            _stackframes.pop();
        }
    }

    // So that we can access this globally...
    namespace {
        std::stack<std::shared_ptr<StackFrame>> _stackframes;
    } // namespace
}