#include <nlohmann/json.hpp>
#include <fstream>

#define PATH_SETTINGS "C:\\openbot\\users\\users\\settings.json"

#include "settings.hpp"


namespace settings
{

void
get_data(nlohmann::json &data)
{
	std::ifstream file_r;
	file_r.open(PATH_SETTINGS);

	if (!file_r.is_open())
	{
		file_r.close();
		throw std::exception("Неудачное открытие файла username_id.json на чтение");
		return;

	}

	file_r >> data;
	file_r.close();

}


void
set_data(nlohmann::json &data)
{
	std::ofstream file_w;
	file_w.open(PATH_SETTINGS);

	if (!file_w.is_open())
	{
		file_w.close();
		throw std::exception("Неудачное открытие файла username_id.json на запись");
		return;

	}


	file_w << data.dump(2);
	file_w.close();

}

}


