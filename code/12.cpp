#include <iostream>
using namespace std;

// Node for doubly linked list
struct Node {
    int data;
    Node* next;
    Node* prev;
};

// Class for binary number operations using a doubly linked list
class BinaryNumber {
private:
    Node* head;
    Node* tail;

public:
    // Constructor
    BinaryNumber() : head(nullptr), tail(nullptr) {}

    // Function to append a bit (0 or 1) to the list at the end
    void append(int bit) {
        Node* newNode = new Node();
        newNode->data = bit;
        newNode->next = nullptr;
        newNode->prev = tail;
        if (tail) {
            tail->next = newNode;
        } else {
            head = newNode;
        }
        tail = newNode;
    }

    // Function to display the binary number
    void display() const {
        Node* temp = head;
        while (temp) {
            cout << temp->data;
            temp = temp->next;
        }
        cout << endl;
    }

    // Function to compute the 1's complement
    BinaryNumber onesComplement() {
        Node* temp = head;
        BinaryNumber result;
        while (temp) {
            temp->data = 1 - temp->data;  // Flip bits (0 to 1, 1 to 0)
            temp = temp->next;
        }
        return result;
    }

    // Function to compute the 2's complement
    BinaryNumber twosComplement() {
        // Step 1: Compute 1's complement
        BinaryNumber result2;
        BinaryNumber result = onesComplement();

        // Step 2: Add 1 to the least significant bit (LSB)
        Node* temp = tail;
        int carry = 1;
        while (temp && carry) {
            int sum = temp->data + carry;
            temp->data = sum % 2;
            carry = sum / 2;
            temp = temp->prev;
        }

        // If there's still a carry, add a new node at the beginning
        if (carry) {
            Node* newNode = new Node();
            newNode->data = carry;
            newNode->next = head;
            newNode->prev = nullptr;
            head->prev = newNode;
            head = newNode;
        }
        return result2;
    }

    // Function to add two binary numbers
    BinaryNumber addBinary(const BinaryNumber& other) {
        BinaryNumber result;
        Node* p1 = this->tail;
        Node* p2 = other.tail;
        int carry = 0;

        while (p1 || p2 || carry) {
            int bit1 = p1 ? p1->data : 0;
            int bit2 = p2 ? p2->data : 0;
            int sum = bit1 + bit2 + carry;
            cout<<bit1<<":"<<bit2<<":"<<sum<<endl;

            result.appendFront(sum % 2);  // Add to front as we're building from LSB to MSB
            carry = sum / 2;

            if (p1) p1 = p1->prev;
            if (p2) p2 = p2->prev;
        }

        return result;
    }

    // Helper function to add a node at the front of the list
    void appendFront(int bit) {
        cout<<"bit:"<<bit<<endl;
        Node* newNode = new Node();
        newNode->data = bit;
        newNode->next = head;
        newNode->prev = nullptr;
        if (head) {
            head->prev = newNode;
        } else {
            tail = newNode;
        }
        head = newNode;
    }
};

// Test the program
int main() {
    BinaryNumber bin1, bin2;

    // Input binary number 1
    cout << "Enter binary number 1: ";
    string binary1;
    cin >> binary1;
    for (char bit : binary1) {
        bin1.append(bit - '0');
    }

    // Input binary number 2
    cout << "Enter binary number 2: ";
    string binary2;
    cin >> binary2;
    for (char bit : binary2) {
        bin2.append(bit - '0');
    }

    // Display original numbers
    cout << "\nBinary Number 1: ";
    bin1.display();
    cout << "Binary Number 2: ";
    bin2.display();

    // 1's Complement of bin1
    cout << "\n1's Complement of Binary Number 1: ";
    bin1.onesComplement();
    bin1.display();

    // 2's Complement of bin1
    cout << "2's Complement of Binary Number 1: ";
    bin1.twosComplement();
    bin1.display();

    // Add bin1 and bin2
    BinaryNumber result = bin1.addBinary(bin2);
    cout << "Sum of Binary Number 1 and Binary Number 2: ";
    result.display();

    return 0;
}
