#include <cassert>
#include <vector>
#include <iostream>
#include <format>

template <typename T>
class Queue {
    private:
        std::vector<T> data;
        T front;
        T back;
        int size;

        void update() {
            front = data.front();
            back = data.back();
            if (data.capacity() > data.size()) {
                data.shrink_to_fit();
            }
            size = data.size();
        }
    
    public:
        Queue() : front(), back(), size(0) {}

        Queue(const Queue& other) : data(other.data), front(other.front), back(other.back), size(other.size) {}

        Queue(std::vector<T> queuedata): data(queuedata), front(queuedata[0]), back(queuedata[queuedata.size()-1]), size(queuedata.size()) {}

        Queue& operator=(const Queue& other) {
            if (this != &other) {
                data = other.data;
                front = other.front;
                back = other.back;
                size = other.size;
            }
            return *this;
        }

        Queue& operator=(const std::vector<T> queuedata) {
            queuedata = queuedata;
            front = queuedata[0];
            back = queuedata[queuedata.size()-1];
            size = queuedata.size()-1;

            return *this;
        }

        std::vector<T> getdata() { return data; }

        int getsize() { return size; }

        void enqueue(T value) {
            data.insert(data.begin(), value);
            update();
        }

        T dequeue() {
            T value = data.back();
            data.pop_back();
            update();

            return value;
        }

};

int main() {
    Queue<int> defaultqueue;
    defaultqueue.enqueue(0);
    Queue<int> copyqueue(defaultqueue);
    assert(defaultqueue.getdata() == copyqueue.getdata());
    Queue<int> readyqueue({1,2,3});
    readyqueue.enqueue(5);
    int size = readyqueue.getsize();
    assert(size == 4);
    for (int i = 0; i < size; i++) {
        std::cout << std::format("{}: {}\n", i+1, readyqueue.dequeue());
    }
    
}