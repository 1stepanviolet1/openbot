#include <nlohmann/json.hpp>
#include <string>

#include "settings.hpp"
#include "id.hpp"
#include "def_hash.hpp"

#define __ID "id"
#define __ACT_FLAG "ACT_FLAG"
#define __NONE settings::hash_str("None")


namespace id
{

void
check(const std::string username, const std::size_t id)
{
	nlohmann::json user_base;
	settings::get_data(user_base);

	bool _f_exist_username = false;
	bool _f_exist_id = false;

	std::string _username;

	std::string _i_username;
	std::size_t _i_id;

	for (auto el = user_base.begin(); el != user_base.end(); ++el)
	{
		_i_username = el.key();
		_i_id = el.value()[__ID];

		if (_i_id == id)
		{
			_f_exist_id = true;
			_username = _i_username;
		}

		if (_i_username == username)
			_f_exist_username = true;

		if (_f_exist_id && _f_exist_username)
			break;

	}

	bool _f_acts = false;

	if (!_f_exist_id && !_f_exist_username)
	{
		nlohmann::json user = {
			{__ID, id},
			{__ACT_FLAG, __NONE}
		};

		user_base[username] = user;
		_f_acts = true;

	}

	else if (_f_exist_id && !_f_exist_username)
	{
		nlohmann::json user(user_base[_username]);
		user_base.erase(_username);
		user_base[username] = user;
		_f_acts = true;

	}

	else if (!_f_exist_id && _f_exist_username)
		throw std::exception("Не может быть ситуации 3 :)");

	if (_f_acts)
		settings::set_data(user_base);

}

int
get(const std::string username)
{
	nlohmann::json user_base;
	settings::get_data(user_base);

	if (!user_base.contains(username))
		return 1;

	return user_base[username][__ID];

}

}