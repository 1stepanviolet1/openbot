
//#define DEBUG

#include "id.hpp"
#include "act_flag.hpp"
#include "def_hash.hpp"


extern "C" __declspec(dllexport) int
hash_str(const char text[]) // импортируемая хэш-функция (ненадёжная)
{
	return settings::hash_str(text);

}


extern "C" __declspec(dllexport) void
check_username_id(const char _username[], const int _id)
{
	id::check(_username, _id);
	
}


extern "C" __declspec(dllexport) int
get_id(const char _username[])
{
	return id::get(_username);

}


extern "C" __declspec(dllexport) int
get_act_flag(const char _username[])
{
	return ACT_FLAG::get(_username);

}


extern "C" __declspec(dllexport) int
set_act_flag(const char _username[], const int _val)
{
	return ACT_FLAG::set(_username, _val);

}


#ifdef DEBUG

#include "logger.hpp"


int main(std::size_t, char **)
{
	//std::string username = "user1";
	//std::size_t id = 2;

	try
	{
		set_act_flag("user1", hash_str("Trans"));
		set_act_flag("user2", hash_str("None"));
		
		log(get_act_flag("user1"))

		log(get_act_flag("user2"))

	}
	catch (const std::exception &err)
	{
		std::cerr << err.what() << std::endl;

	}


	return 0;

}

#endif // DEBUG
