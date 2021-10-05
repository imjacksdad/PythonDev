## The Black and Scholes (1973) Stock option formula

# S= Stock price
# X=Strike price
# T=Years to maturity
# r= Risk-free rate
# v=Volatility



    d1 = (Math.log(S / X) + (r + v * v / 2) * T) / (v * Math.sqrt(T));
    d2 = d1 - v * Math.sqrt(T);

    if (CallPutFlag == 'c') {
	result =  S * CND(d1) - X * Math.exp(-r * T) * CND(d2);
    } else {
	result = X * Math.exp(-r * T) * CND(-d2) - S * CND(-d1);
    }
	
    print("in Black76 result-[" + result + "] " );
    print(CallPutFlag + ", $-" + S + ", x-" + X + ", T-" + T + ", r-" + r + ", v-" + v);
		
##The cumulative normal distribution function
public double CND(double X) {
    double L, K, w;
    double a1 = 0.31938153, a2 = -0.356563782, a3 = 1.781477937, a4 = -1.821255978, a5 = 1.330274429;

    L = Math.abs(X);
    K = 1.0 / (1.0 + 0.2316419 * L);
    w = 1.0
	- 1.0
	# Math.sqrt(2.0 * Math.PI)
	* Math.exp(-L * L / 2)
	* (a1 * K + a2 * K * K + a3 * Math.pow(K, 3) + a4
	* Math.pow(K, 4) + a5 * Math.pow(K, 5));

	if (X < 0.0) {
		w = 1.0 - w;
	}
	print(w)
}
		
