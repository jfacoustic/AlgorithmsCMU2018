#include <iostream>
#include <cmath>
using namespace std;

class Complex {
	public:
		void add( Complex * a ) {
			x += a->x;
			y += a->y;
		}
		void square() {
			Complex c;
			c.x = x*x - y*y;
			c.y = 2*x*y;
			x = c.x;
			y = c.y;
		}
		double mod() {
			return sqrt(x * x + y*y);
		}
		Complex(double X, double Y) {
			x = X;
			y = Y;
		}
		Complex() {
			x = 0;
			y = 0;
		}
	private:
		double x, y;
};

bool mandel(Complex * a, Complex * b, int r) {

	if(a->mod() >= 2.0) return false;
	if(r <= 0) return true;
	r--;
	a->square();
	a->add(b);
	return mandel(a, b, r);
}

int main() {
	double x, y;
	int r;
	int c = 0;
	while(cin >> x >> y >> r) {
		c++;
		Complex * a = new Complex(0,0);
		Complex * b = new Complex(x,y);
		bool set=mandel(a, b, r);
		if(set) cout << "Case " << c << ": IN" << endl;
		else cout << "Case " << c << ": OUT" << endl;
	}
	return 0;
}
