#pragma once

#define FNV_PRIME 13
#define FNV_OFFSET 31

namespace settings
{

int
hash_str(const char* txt);

}
