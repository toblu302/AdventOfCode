#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

bool test_noun_word(vector<int> data, int noun, int word) {
	data.at(1) = noun;
	data.at(2) = word;

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

	return data.at(0) == 19690720;
}

int main() {
	// Read data
	string input;
	vector<int> data;
	while(getline(cin, input, ',')) {
		int num = atoi(input.c_str());
		data.push_back(num);
	}

	// Attempt noun/word combinations
	for(int noun=1; noun<100; ++noun) {
		for(int word=1; word<100; ++word) {
			bool correct = test_noun_word(data, noun, word);
			if(correct) {
				cout << 100*noun + word << endl;
			}
		}
	}
	
	return 0;
}
