#include <iostream>

using namespace std;

class calendar {
public:
	calendar(int nowyear, int nowmonth) {
		this->year = nowyear;
		this->month = nowmonth-1;
	}
	int getday() {
		if(this->month !=2)
			return days[this->month];
		else {
			if (!(this->year % 4) && ((this->year % 100) || !(this->year % 400)))
				return days[this->month] + 1;
			else
				return days[this->month];
		}
	}
private:
	int year = 0, month = 0;
	int days[12] = {31, 28, 31, 30, 31,30,31,31,30,31,30,31 };
};

int main(void) {
	int y, m;
	cout << "---Calendar day calculator---\nINPUT YEAR:: ";
	cin >> y;
	cout << "INPUT MONTH(1~12):: ";
	cin >> m;
	calendar thisyear = calendar(y, m);
	cout << "YEAR :: " << y << " MONTH :: " << m << " HAS "<<thisyear.getday() <<" DAYS\n";
}