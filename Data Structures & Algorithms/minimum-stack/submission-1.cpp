class MinStack {
public:
    stack<int> stk;
    stack<int> min;
    MinStack() { 
    }
    
    void push(int val) {
        stk.push(val);
        int low = stk.top();
        if (min.size() > 0) {
            low = min.top();
            if (val < low) {
                low = val;
            }
        }
        min.push(low);
    }
    
    void pop() {
        stk.pop();
        min.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return min.top();
    }
};
