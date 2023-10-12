
//#define DEBUG

#include "tickers.hpp"
#include <math.h>


//extern "C" __declspec(dllexport) const char *
//get_tickers()
//{
//	tickers _ticks;
//	std::string str_tickers;
//	_ticks.get(str_tickers); // "BTC DOGE ETH USDT"
//
//	const size_t SIZE = str_tickers.length();
//	char * _tickers = new char[SIZE + 1];
//	
//	for (size_t i = 0; i < SIZE; ++i)
//		_tickers[i] = str_tickers[i];
//
//	_tickers[SIZE] = '\0';
//
//	return _tickers;
//
//}

extern "C" __declspec(dllexport) const char *
get_tickers()
{
	tickers _ticks;
	std::string str_tickers;
	_ticks.get(str_tickers); // "BTC DOGE ETH USDT"

	return str_tickers.data();

}


extern "C" __declspec(dllexport) int
add_ticker(char _ticker[])
{
	tickers _ticks;
	return (int)_ticks.add(_ticker);

}


extern "C" __declspec(dllexport) int
remove_ticker(char _ticker[])
{
	tickers _ticks;
	return (int)_ticks.remove(_ticker);
}



#ifdef DEBUG

#include "logger.hpp"


int main(size_t, char**)
{
	tickers _tickers;

	std::string ticks;
	_tickers.get(ticks);

	log(ticks)


	return 0;

}

#endif // DEBUG
