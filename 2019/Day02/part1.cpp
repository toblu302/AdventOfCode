#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

int main() {
	// Read data
	string input;
	vector<int> data;
	while(getline(cin, input, ',')) {
		int num = atoi(input.c_str());
		data.push_back(num);
	}

	// Do stuff
	int pointer = 0;
	while(true) {
		int opcode = data.at(pointer);
		if(opcode == 99) {
			break;
		}

		int op1 = data.at(pointer+1);
		int op2 = data.at(pointer+2);
		int op3 = data.at(pointer+3);

		int num1 = data.at(op1);
		int num2 = data.at(op2);

		int res = num1*num2;
		if(opcode == 1) {
			res = num1+num2;
		}
		data.at(op3) = res;

		pointer += 4;
	}

	cout << data.at(0) << endl;
	
	return 0;
}
