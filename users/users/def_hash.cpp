
#include "def_hash.hpp"

#define FNV_PRIME 13
#define FNV_OFFSET 31

namespace settings
{

// TODO: реализация хэш-функции
int
hash_str(const char* txt)
{
	int hash = FNV_PRIME;

	for (; *txt != '\0'; ++txt)
	{
		hash *= (int)(*txt);
		hash += FNV_OFFSET;

	}

	return hash;

}

}
