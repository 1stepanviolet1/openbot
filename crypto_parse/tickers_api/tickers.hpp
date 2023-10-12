#pragma once

#include <nlohmann/json.hpp>
#include <fstream>
#include <string>

#define PATH_OF_TICKERS "C:\\openbot\\crypto_parse\\tickers.json"


class tickers
{
private:
	nlohmann::json _data;

public:
	tickers();

	size_t get(std::string&);

	size_t add(std::string);

	size_t remove(std::string);

private:
	size_t set();

};
