class DataStream {
public:
int size, val, k;
    DataStream(int value, int k) {
        this->val = value;
        this->k=k;
        size = 0;
    }
    
    bool consec(int num) {
        if (num==val){
            size++;
        }
        else{
            size=0;
        }

        return size>=k;
    }
};

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream* obj = new DataStream(value, k);
 * bool param_1 = obj->consec(num);
 */
