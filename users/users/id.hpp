#pragma once

#include <nlohmann/json.hpp>
#include <string>

#include "settings.hpp"
#include "def_hash.hpp"

#define __ID "id"
#define __ACT_FLAG "ACT_FLAG"
#define __NONE settings::hash_str("None")


namespace id
{

void
check(const std::string, const std::size_t);

int
get(const std::string username);

}
