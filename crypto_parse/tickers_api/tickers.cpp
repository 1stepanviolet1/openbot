#include <nlohmann/json.hpp>
#include <fstream>
#include <string>

#include "tickers.hpp"


tickers::tickers()
{
	std::ifstream file_r;
	file_r.open(PATH_OF_TICKERS);

	if (!file_r.is_open())
	{
		file_r.close();
		throw std::exception("file tickets.json is not opened");

	}

	file_r >> this->_data;

	file_r.close();

}

size_t 
tickers::add(std::string _ticker)
{
	this->_data.push_back(_ticker);
	this->set();

	return 0;

}

size_t 
tickers::get(std::string &_tickers)
{
	_tickers.clear();

	for (auto _tick = this->_data.begin(); _tick != this->_data.end(); ++_tick)
	{
		std::string _ticker = _tick.value();
		_tickers += _ticker + ' ';

	}

	_tickers.pop_back();

	return 0;

}

size_t 
tickers::set()
{
	std::ofstream file_w;
	file_w.open(PATH_OF_TICKERS);

	if (!file_w.is_open())
	{
		file_w.close();
		return 1;

	}

	file_w << this->_data.dump(2);

	file_w.close();

	return 0;

}

size_t 
tickers::remove(std::string _rem_ticker)
{
	bool act_flag = false;

	for (auto _tick = this->_data.begin(); _tick != this->_data.end(); ++_tick)
	{
		std::string _ticker = _tick.value();

		if (_ticker == _rem_ticker)
		{
			this->_data.erase(_tick);
			act_flag = true;
			break;

		}

	}

	if (!act_flag)
		return 1;
	
	this->set();


	return 0;

}
