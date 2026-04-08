class MinStack {
    std::stack<std::pair<int, int>> s;
public:
    MinStack() {
        
    }
    
    void push(int val) {
        if (s.size() == 0) {
            s.push({val, val});
        } else {
            s.push({val, std::min(val, s.top().second)});
        }
    }
    
    void pop() {
        s.pop();
    }
    
    int top() {
        return s.top().first;
    }
    
    int getMin() {
        return s.top().second;
    }
};
