#pragma once

#include <string>
#include <nlohmann/json.hpp>

#include "settings.hpp"

#define __ACT_FLAG "ACT_FLAG"


namespace ACT_FLAG
{

int
get(const std::string username);

int
set(const std::string username, const std::size_t __value);

}
