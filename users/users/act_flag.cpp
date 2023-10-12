#include <string>
#include <nlohmann/json.hpp>
#include <unordered_map>
#include <iostream>

#include "settings.hpp"
#include "act_flag.hpp"

#define __ACT_FLAG "ACT_FLAG"


namespace ACT_FLAG
{

int
get(const std::string username)
{
	nlohmann::json user_base;
	settings::get_data(user_base);

	if (!user_base.contains(username))
		return -1;

	return user_base[username][__ACT_FLAG];

}

int
set(const std::string username, const std::size_t __value)
{
	nlohmann::json user_base;
	settings::get_data(user_base);

	if (!user_base.contains(username))
		return 1;

	user_base[username][__ACT_FLAG] = __value;
	settings::set_data(user_base);

	return 0;

}

}
