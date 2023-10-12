#pragma once

#include <nlohmann/json.hpp>
#include <fstream>

#define PATH_SETTINGS "C:\\openbot\\users\\users\\settings.json"

namespace settings
{
void
get_data(nlohmann::json& data);

void
set_data(nlohmann::json& data);

}
